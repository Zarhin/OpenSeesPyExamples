# -*- coding: utf-8 -*-
# author: zarhin

import part
import opensees_tools as opt
import numpy as np

# part
# x = [-10.5, -0.5, 0.0, 0.5, 10.5]
# y = [-20.5, -20.0, 0.0, 0.5, 3.0]
x = [-1.5, -0.5, 0.0, 0.5, 1.5]
y = [0, 2, 3]
# rec & line
part.Node.reset()
part.Element.reset()
rec1 = part.Rectangle()
rec2 = part.Rectangle()
line = part.Line()
rec1.create_by_coord(((x[0], y[1]), (x[1], y[2])))
rec2.create_by_coord(((x[3], y[1]), (x[4], y[2])))
line.create_by_coord(((x[2], y[0]), (x[2], y[-1])))
# seed
# general seed
rec1.set_seed(1.0)
rec2.set_seed(1.0)
line.set_seed(1.0)
# horizontal seed
rec1.set_seed(point_num=11, bias_ratio=1.2,
              flip_para=True, direction='horizontal')
rec2.set_seed(point_num=11, bias_ratio=1.2, direction='horizontal')
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

# beam model
opt.opsfunc('model', 'basic', '-ndm', 2, '-ndf', 3)

# beam parameters
D = 1.0
area = np.pi * D ** 2 / 4.0
I = np.pi * D ** 4 / 64.0
thick = 0.5
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
opt.location(figure=True)
# contact element
# set gap and force tolerances for beam contact elements
gapTol = 1.0e-10
forceTol = 1.0e-10
