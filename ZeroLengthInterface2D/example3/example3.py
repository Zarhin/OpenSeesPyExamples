# -*-coding:utf-8
# author: zarhin
# email: lizaixainvip@163.com
# date: 2020.08.12

import numpy as np
import part
import opensees_tools as ops
import opensees_to_gid as otg

# points
p1 = part.Point([-10, -10])
p2 = part.Point([-0.5, 0.0])
p3 = part.Point([0.0, -10])
p4 = part.Point([0.0, 3.0])
p5 = part.Point([0.5, -10])
p6 = part.Point([10, 0.0])

# part
rec1 = part.Rectangle([p1, p2])
line = part.Line([p3, p4])
rec2 = part.Rectangle([p5, p6])

# mesh
part.Element.reset()
part.Node.reset()
rec1.set_seed(1.0)
rec1.set_seed(point_num=11, bias_ratio=1.2, flip_para=True,
              direction='horizontal')
rec1.mesh()
line.set_seed(0.5)
line.mesh()
rec2.set_seed(1.0)
rec2.set_seed(point_num=11, bias_ratio=1.2, flip_para=False,
              direction='horizontal')
rec2.mesh()

# opensees model
# soil model
ops.opsfunc('wipe')
ops.opsfunc('model', 'basic', '-ndm', 2, '-ndf', 2)

# soil node
for node in rec1.nodes + rec2.nodes:
    ops.opsfunc('node', node.tag, *node.coord)

# material
ops.opsfunc('nDMaterial', 'ElasticIsotropic', 1, 2.24e5, 0.4, 2.0)

# soil elements
for element in rec1.elements + rec2.elements:
    nodes = [node.tag for node in element.nodes]
    ops.opsfunc('element', 'quad', element.tag, *nodes, 1.0, 'PlaneStrain', 1)

# boundary
bottom_nodes = part.Node.search([-10, -10], [10, -10],
                                rec1.nodes + rec2.nodes)
side_nodes = part.Node.search([-10.0, -9.8], [-10, 0])
side_nodes = side_nodes + part.Node.search([10, -9.8], [10, 0])
ops.opsfunc('fix', bottom_nodes[0].tag, 1, 1)
ops.opsfunc('fix', bottom_nodes[-1].tag, 1, 1)
for node in bottom_nodes[1:-1:1]:
    ops.opsfunc('fix', node.tag, 0, 1)
for node in side_nodes:
    ops.opsfunc('fix', node.tag, 1, 0)


# pile model
ops.opsfunc('model', 'basic', '-ndm', 2, '-ndf', 3)

# Pile Material Parameter
IZ = 3.1415926 * 1.0 ** 4 / 64.0
AREA = 3.1415926 * 1.0 ** 2 / 4.0
E = 3.25e7

# geomTransf
ops.opsfunc('geomTransf', 'Linear', 1)

# pile node
translation = np.array([0.5, 0.0])
arm_nodes = []
arm_elements = []
for node in line.nodes:
    node1 = part.Node(node.coord + translation)
    node2 = part.Node(node.coord - translation)
    arm_nodes += [node1, node2]
    # nodes
    ops.opsfunc('node', node.tag, *node.coord)
    ops.opsfunc('node', node1.tag, *node1.coord)
    ops.opsfunc('node', node2.tag, *node2.coord)
    # rigid arm
    ele1 = part.Element([node, node1])
    ele2 = part.Element([node, node2])
    arm_elements += [ele1, ele2]
    ops.opsfunc('element', 'elasticBeamColumn', ele1.tag, node.tag,
                node1.tag, AREA * 1E3, E * 1e3, IZ * 1e3, 1)
    ops.opsfunc('element', 'elasticBeamColumn', ele2.tag, node.tag,
                node2.tag, AREA * 1E3, E * 1e3, IZ * 1e3, 1)

# pile elements
for element in line.elements:
    nodes = [node.tag for node in element.nodes]
    ops.opsfunc('element', 'elasticBeamColumn', element.tag, *nodes, AREA,
                3.25e7, IZ, 1)

# boundary
pile_bottom_node = part.Node.search([0.0, -10.0])
ops.opsfunc('fix', pile_bottom_node.tag, 0, 1, 0)

# contact element
left_arm_nodes = part.Node.search([-0.5, -10], [-0.5, 0], arm_nodes)
left_soil_nodes = part.Node.search([-0.5, -10], [-0.5, 0], rec1.nodes)
right_arm_nodes = part.Node.search([0.5, -10], [0.5, 0], arm_nodes)
right_soil_nodes = part.Node.search([0.5, -10], [0.5, 0], rec2.nodes)
# left contact element
left_contact_nodes = left_soil_nodes + left_arm_nodes[-1::-1]
ele1 = part.Element(left_contact_nodes, id0='left_contact')
ops.opsfunc('element', 'zeroLengthInterface2D', ele1.tag, '-sNdNum',
            len(left_soil_nodes), '-mNdNum', len(left_arm_nodes), '-dof',
            2, 3, '-Nodes', *[node.tag for node in left_contact_nodes],
            1e8, 1e8, 0.0)
# right contact element
right_contact_nodes = right_soil_nodes[-1::-1] + right_arm_nodes
ele2 = part.Element(right_contact_nodes, id0='right_contact')
ops.opsfunc('element', 'zeroLengthInterface2D', ele2.tag, '-sNdNum',
            len(right_soil_nodes), '-mNdNum', len(right_arm_nodes), '-dof',
            2, 3, '-Nodes', *[node.tag for node in right_contact_nodes],
            1e8, 1e8, 16)

# print gid
ops.opsfunc('printGID', 'example3.msh')

# load
ops.opsfunc('timeSeries', 'Linear', 1)
ops.opsfunc('pattern', 'Plain', 1, 1)
load_node = part.Node.search([0.0, 3.0])
ops.opsfunc('load', load_node.tag, -1000.0, 0.0, 0.0)


# recorder
node_list = ops.opsfunc('getNodeTags')
ops.opsfunc('recorder', 'Node', '-file', 'disp.txt', '-node', *node_list,
            '-dof', 1, 2, 3, 'disp')

# analysis option
ops.opsfunc('integrator', 'LoadControl', 0.01)
# ops.opsfunc('test', 'EnergyIncr', 1, 100, 5)
ops.opsfunc('test', 'FixedNumIter', 5, 5)
ops.opsfunc('algorithm', 'Newton')
ops.opsfunc('numberer', 'RCM')
ops.opsfunc('constraints', 'Plain')
ops.opsfunc('system', 'ProfileSPD')
ops.opsfunc('analysis', 'Static')
ops.opsfunc('analyze', 100)

ops.opsfunc('printModel', 'node', load_node.tag)

ops.opsfunc('wipe')
ops.opsfunc()

disp = np.loadtxt('disp.txt')
otg.node_result(node_list, [disp], ['Displacement'], 'Static', False,
                'example3.res')
