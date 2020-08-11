# -*- coding: utf-8
# author: zarhin
# date: 2020/8/6 16:04

import numpy as np
import part
import openseesfunction as ops
import opensees_to_gid as otg

p0 = part.Point([0.0, 0.0])
p1 = part.Point([10.0, 1.0])
p2 = part.Point([0.0, 1.0])
p3 = part.Point([10.0, 2.0])

# part 1
part.Node.reset()
part.Element.reset()
rec1 = part.Rectangle([p0, p1])
rec1.set_seed(1.0)
rec1_nodes, rec1_element = rec1.mesh()

# part 2
rec2 = part.Rectangle([p2, p3])
rec2.set_seed(1.0)
rec2_nodes, rec2_element = rec2.mesh()

# opensees model
ops.opsfunc('wipe')
ops.opsfunc('model', 'basic', '-ndm', 2, '-ndf', 2)

# opensees nodes
nodes = rec1_nodes + rec2_nodes
for node in nodes:
    ops.Node(node.coord, tag=node.tag)

# boundary
for node in part.Node.search([0.0, 0.0], [0.0, 2.0]):
    ops.opsfunc('fix', node.tag, 1, 1)

# material
# Material "Material01":    matTag    E    v    rho
ops.opsfunc('nDMaterial', 'ElasticIsotropic', 1, 1e5, 0.25, 6.75)

# elements
elements = rec1_element + rec2_element
for element in elements:
    nodes = [node.tag for node in element.nodes]
    ops.opsfunc('element', 'quad', element.tag, *nodes, 1.0, 'PlaneStrain', 1)

# contact nodes
slave_nodes = part.Node.search([0.0, 1.0], [10.0, 1.0], rec1_nodes)
master_nodes = part.Node.search([0.0, 1.0], [10.0, 1.0], rec2_nodes)
contact_nodes = slave_nodes[-1::-1] + master_nodes
ele = part.Element(contact_nodes, id0='contact')
ops.opsfunc('element', 'zeroLengthInterface2D', ele.tag, '-sNdNum',
            len(slave_nodes), '-mNdNum', len(master_nodes), '-dof', 2, 2,
            '-Nodes', *[node.tag for node in ele.nodes], 1e9, 0, 0)

# load pattern
ops.opsfunc('timeSeries', 'Constant', 1)
ops.opsfunc('pattern', 'Plain', 1, 1, '{')
load_node = part.Node.search([10.0, 2.0])
load_node = load_node[0]
ops.opsfunc('load', load_node.tag, 0.0, -100, '}')

# recorder
ops.opsfunc('printGID', 'example2.msh')
node_list = ops.opsfunc('getNodeTags')
ops.opsfunc('recorder', 'Node', '-file', 'disp.txt', '-node', *node_list,
            '-dof', 1, 2, 'disp')

# analysis option
ops.opsfunc('integrator', 'DisplacementControl', load_node.tag, 2, -1.0e-3)
ops.opsfunc('test', 'EnergyIncr', 1.0e-6, 100, 5)
ops.opsfunc('algorithm', 'Newton')
ops.opsfunc('numberer', 'RCM')
ops.opsfunc('constraints', 'Transformation')
ops.opsfunc('system', 'ProfileSPD')
ops.opsfunc('analysis', 'Static')
ops.opsfunc('analyze', 500)

ops.opsfunc('printModel', 'node', load_node.tag, 22)
ops.opsfunc('wipe')
# ops.opsfunc()

disp = np.loadtxt('disp.txt')
otg.node_result(node_list, [disp], ['Displacement'], 'Static Analysis',
                time_column=False, file_name='example2.res')
