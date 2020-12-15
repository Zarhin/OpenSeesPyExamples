# -*- conding: utf-8 -*-
# author: zarhin

import numpy as np
import part
import opensees_tools as opt
import opensees_to_gid as otg
import openseespy.postprocessing.Get_Rendering as opg

# part
x = [-1.5, -0.5, 0.0, 0.5, 1.5]
y = [-0.5, 0.0, 1.5, 2.0, 2.5]
# rec & line
part.Node.reset()
part.Element.reset()
rec1 = part.Rectangle()
rec2 = part.Rectangle()
line = part.Line()
rec1.create_by_coord(((x[0], y[1]), (x[1], y[3])))
rec2.create_by_coord(((x[3], y[1]), (x[4], y[3])))
line.create_by_coord(((x[2], y[0]), (x[2], y[-1])))
# seed
# general seed
rec1.set_seed(1.0)
rec2.set_seed(1.0)
line.set_seed(1.0)
# mesh
rec1.mesh()
rec2.mesh()
line.mesh()

# model
opt.opsfunc('wipe')
# soil model
opt.opsfunc('model', 'basic', '-ndm', 2, '-ndf', 2)

# node
for node in rec1.nodes + rec2.nodes:
    opt.opsfunc('node', node.tag, *node.coord)

# material
opt.opsfunc('nDMaterial', 'PressureDependMultiYield02', 5, 2, 1.8, 9.6e3,
            2.7e4, 36, 0.1, 101.0, 0.0, 26, 0.067, 0.23, 0.06, 0.27, 20,
            5.0, 3.0, 1.0, 0.0, 0.77, 0.9, 0.02, 0.7, 101.0)
# create wrapper material for initial state analysis
opt.opsfunc('nDMaterial', 'InitialStateAnalysisWrapper', 1, 5, 2)

# two-dimensional contact material
opt.opsfunc('nDMaterial', 'ContactMaterial2D', 2, 0.1, 1000.0, 0.0, 0.0)

# soil element
for element in rec1.elements + rec2.elements:
    nodes = [node.tag for node in element.nodes]
    opt.opsfunc('element', 'quad', element.tag, *nodes, 1.0, 'PlaneStrain',
                1, 0.0, 0.0, 0.0, -9.81 * 1.8)

# soil boundary
node_location = opt.location()
for node in node_location[[0, -1], :].T:
    opt.opsfunc('fix', node[0], 1, 0)
    opt.opsfunc('fix', node[1], 1, 0)
for node in node_location[:, 0]:
    opt.opsfunc('fix', node, 0, 1)
    
# lagrange multiplier node
opt.opsfunc('node', 17, 0.0, 0.0)
opt.opsfunc('node', 18, 0.0, 0.0)
opt.opsfunc('node', 19, 0.0, 0.0)
opt.opsfunc('node', 20, 0.0, 0.0)
opt.opsfunc('node', 21, 0.0, 0.0)
opt.opsfunc('node', 22, 0.0, 0.0)


# beam model
opt.opsfunc('model', 'basic', '-ndm', 2, '-ndf', 3)

# beam parameters
D = 1.0
area = np.pi * D ** 2 / 4.0
I = np.pi * D ** 4 / 64.0
thick = 1.0
beamE = 200000000
numIntPts = 3

# node
for node in line.nodes:
    opt.opsfunc('node', node.tag, *node.coord)

# beam element
opt.opsfunc('geomTransf', 'Linear', 1)
# section
opt.opsfunc('section', 'Elastic', 1, beamE, area, I)
opt.opsfunc('beamIntegration', 'Legendre', 1, 1, numIntPts)
# element
for element in line.elements:
    nodes = [node.tag for node in element.nodes]
    opt.opsfunc('element', 'dispBeamColumn', element.tag, *nodes, 1, 1)

# boundary
bottom_node = part.Node.search((x[2], y[0]))
opt.opsfunc('fix', bottom_node.tag, 0, 1, 0)

# contact element
# set gap and force tolerances for beam contact elements
gapTol = 1.0e-10
forceTol = 1.0e-10

# contact element
contact_element = []
opt.opsfunc('element', 'BeamContact2D', 8, 15, 16, 6, 17, 2, thick, gapTol,
            forceTol)
opt.opsfunc('element', 'BeamContact2D', 9, 15, 16, 11, 18, 2, thick, gapTol,
            forceTol)
opt.opsfunc('element', 'BeamContact2D', 10, 14, 15, 4, 19, 2, thick, gapTol,
            forceTol)
opt.opsfunc('element', 'BeamContact2D', 11, 14, 15, 9, 20, 2, thick, gapTol,
            forceTol)
opt.opsfunc('element', 'BeamContact2D', 12, 13, 14, 2, 21, 2, thick, gapTol,
            forceTol)
opt.opsfunc('element', 'BeamContact2D', 13, 13, 14, 7, 22, 2, thick, gapTol,
            forceTol)
opt.opsfunc('printGID', 'model.msh')

# recorder
node_list = opt.opsfunc('getNodeTags')
opt.opsfunc('recorder', 'Node', '-file', 'disp.txt', '-time', '-nodeRange',
            1, 22, '-dof', 1, 2, 'disp')

# define analysis parameters for gravity phase
opt.opsfunc('constraints', 'Transformation')
opt.opsfunc('test', 'NormDispIncr', 1e-5, 15, 1)
opt.opsfunc('algorithm', 'Newton')
opt.opsfunc('numberer', 'RCM')
opt.opsfunc('system', 'SparseGeneral')
opt.opsfunc('integrator', 'LoadControl', 0.1)
opt.opsfunc('analysis', 'Static')

opt.opsfunc('InitialStateAnalysis', 'on')
opt.opsfunc('updateMaterialStage', '-material', 1, '-stage', 0)
opt.opsfunc('setParameter', '-val', 0, '-eleRange', 8, 13, 'friction')
opt.opsfunc('analyze', 4)
opt.opsfunc('updateMaterialStage', '-material', 1, '-stage', 1)
opt.opsfunc('analyze', 4)
# designate end of initial state analysis \
# (zeros displacements, keeps state variables)
opt.opsfunc('InitialStateAnalysis', 'off')
# turn on frictional behavior for beam contact elements
opt.opsfunc('setParameter', '-val', 1, '-eleRange', 8, 13, 'friction')
opt.opsfunc('analyze', 4)

opt.opsfunc('wipeAnalysis')
opt.opsfunc('loadConst', '-time', 0.0)

opg.createODB('2DContact', 'Static', Nmodes=3)

# recorder
node_list = opt.opsfunc('getNodeTags')
opt.opsfunc('recorder', 'Node', '-file', 'disp.txt', '-time', '-nodeRange',
            1, 22, '-dof', 1, 2, 'disp')

# load
opt.opsfunc('timeSeries', 'Constant', 1)
opt.opsfunc('pattern', 'Plain', 1, 1, '{')
opt.opsfunc('load', 16, 10, 0, 0, '}')

# analysis
opt.opsfunc('constraints', 'Transformation')
opt.opsfunc('test', 'NormDispIncr', 1e-5, 15, 1)
opt.opsfunc('algorithm', 'Newton')
opt.opsfunc('numberer', 'RCM')
opt.opsfunc('system', 'SparseGeneral')
opt.opsfunc('integrator', 'LoadControl', 0.1)
opt.opsfunc('analysis', 'Static')
opt.opsfunc('analyze', 10)

opt.opsfunc('printModel', '-node', 16)
# wipe
opt.opsfunc('wipe')

disp = np.loadtxt('disp.txt')
otg.node_result(node_list, [disp], ['Displacement'], 'Static')
# opg.plot_modeshape(2, 300, Model='2DContact')
# opg.plot_deformedshape(Model='2DContact', LoadCase='Static')
