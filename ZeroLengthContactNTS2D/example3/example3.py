# -*- coding: utf-8
# author: zarhin
# email: lizaixianvip@163.com

import numpy as np
import part
import openseesfunction as ops
import opensees_to_gid as otg

# points
p0 = part.Point([-10, -10])
p1 = part.Point([-0.5, 0])
p2 = part.Point([-0.5, -10])
p3 = part.Point([0.5, 3.0])
p4 = part.Point([0.5, -10.0])
p5 = part.Point([10, 0.0])

# rectangle
rec1 = part.Rectangle([p0, p1])
rec2 = part.Rectangle([p2, p3])
rec3 = part.Rectangle([p4, p5])

# mesh
part.Node.reset()
part.Element.reset()

rec1.set_seed(1.0)
rec1.set_seed(point_num=11, bias_ratio=1.2, direction='horizontal',
              flip_para=True)
rec1.nodes, rec1.elements = rec1.mesh()

rec2.set_seed(0.5)
rec2.set_seed(point_num=4, direction='horizontal')
rec2.nodes, rec2.elements = rec2.mesh()

rec3.set_seed(1.0)
rec3.set_seed(point_num=11, bias_ratio=1.2, direction='horizontal')
rec3.nodes, rec3.elements = rec3.mesh()

# opensees model
ops.opsfunc('wipe')
ops.opsfunc('model', 'basic', '-ndm', 2, '-ndf', 2)

# node
nodes = rec1.nodes + rec2.nodes + rec3.nodes
for node in nodes:
    ops.opsfunc('node', node.tag, *node.coord)

# material
# nDMaterial('ElasticIsotropic', matTag, E, nu, rho=0.0)
ops.opsfunc('nDMaterial', 'ElasticIsotropic', 1, 2.24e5, 0.4, 0.0)
ops.opsfunc('nDMaterial', 'ElasticIsotropic', 2, 3.25e7, 0.2, 0.0)

# element
# soil element
elements = rec1.elements + rec3.elements
for element in elements:
    nodes = [node.tag for node in element.nodes]
    # element('quad', eleTag, *eleNodes, thick, type, matTag, <pressure=0.0,
    #   rho=0.0, b1=0.0, b2=0.0>)
    ops.opsfunc('element', 'quad', element.tag, *nodes, 1.0, 'PlaneStrain',
                1, 0.0, 2.0, 0.0, 0.0)
# concrete element
for element in rec2.elements:
    nodes = [node.tag for node in element.nodes]
    ops.opsfunc('element', 'quad', element.tag, *nodes, 1.0, 'PlaneStrain',
                2, 0.0, 2.5, 0.0, 0.0)

# contact element
contact_nodes1 = part.Node.search([-0.5, -10.0], [-0.5, 0], rec1.nodes)
contact_nodes2 = part.Node.search([-0.5, -10.0], [-0.5, 0], rec2.nodes)
contact_nodes3 = part.Node.search([0.5, -10.0], [0.5, 0], rec2.nodes)
contact_nodes4 = part.Node.search([0.5, -10.0], [0.5, 0], rec3.nodes)
ele1 = part.Element(contact_nodes1 + contact_nodes2[-1::-1], id0='contact01')
ops.opsfunc('element', 'zeroLengthContactNTS2D', ele1.tag, '-sNdNum',
            len(contact_nodes1), '-mNdNum', len(contact_nodes2), '-Nodes',
            *[node.tag for node in ele1.nodes], 1.0e10, 1.0e10, 0.0)
ele2 = part.Element(contact_nodes4[-1::-1] + contact_nodes3, id0='contact2')
ops.opsfunc('element', 'zeroLengthContactNTS2D', ele2.tag, '-sNdNum',
            len(contact_nodes4), '-mNdNum', len(contact_nodes3), '-Nodes',
            *[node.tag for node in ele2.nodes], 1.0e10, 1.0e10, 0.0)

# boundary
bottom_boundary = part.Node.search([-10, -10], [10, -10])
for node in bottom_boundary[1:-1:1]:
    ops.opsfunc('fix', node.tag, 0, 1)
ops.opsfunc('fix', bottom_boundary[0].tag, 1, 1)
ops.opsfunc('fix', bottom_boundary[-1].tag, 1, 1)
# left side nodes
for node in part.Node.search([-10, -9.8], [-10, 0]):
    ops.opsfunc('fix', node.tag, 1, 0)
for node in part.Node.search([10, -9.8], [10, 0]):
    ops.opsfunc('fix', node.tag, 1, 0)

# load pattern
ops.opsfunc('timeSeries', 'Constant', 1)
ops.opsfunc('pattern', 'Plain', 1, 1, '{')
load_node = part.Node.search([-0.48, 3.0], [0.48, 3.0])
for node in load_node:
    ops.opsfunc('load', node.tag, 500, 0.0)
ops.opsfunc('}')

# print model
ops.opsfunc('printGID', 'example3.msh')

# recorder
node_list = ops.opsfunc('getNodeTags')
ops.opsfunc('recorder', 'Node', '-file', 'disp.txt', '-node',
            *node_list, '-dof', 1, 2, 'disp')


# analysis option
# ops.opsfunc('integrator', 'DisplacementControl', load_node[0].tag, 1, -1.0e-3)
ops.opsfunc('integrator', 'LoadControl', 0.01)
ops.opsfunc('test', 'EnergyIncr', 1.0e-6, 100, 5)
ops.opsfunc('algorithm', 'Newton')
ops.opsfunc('numberer', 'RCM')
ops.opsfunc('constraints', 'Transformation')
ops.opsfunc('system', 'ProfileSPD')
ops.opsfunc('analysis', 'Static')
ops.opsfunc('analyze', 100)

ops.opsfunc('printModel', 'node', *[node.tag for node in load_node])
ops.opsfunc('wipe')
ops.opsfunc()
# load node displacement result
disp = np.loadtxt('disp.txt')
otg.node_result(node_list, [disp], ['Displacement'], 'Static Analysis',
                time_column=False, file_name='example3.res')