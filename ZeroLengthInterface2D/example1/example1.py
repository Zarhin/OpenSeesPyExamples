# -*- coding: utf-8
# author: zarhin
# email: lizaixianvip@163.com

import numpy as np
import part
import opensees_tools as ops
import opensees_to_gid as otg

# point
p0 = part.Point([0.0, 0.0])
p1 = part.Point([10.0, 0.0])
p2 = part.Point([4.0, 0.0])
p3 = part.Point([6.0, 1.0])

# rectangle
rec = part.Rectangle([p2, p3])
line = part.Line([p0, p1])

# mesh
rec.set_seed(1)
rec.set_seed(2, direction='horizontal')
rec.mesh()
line.set_seed(2)
line.mesh()

# soil model
ops.opsfunc('wipe')
ops.opsfunc('model', 'basic', '-ndm', 2, '-ndf', 2)

# soil nodes
for node in rec.nodes:
    ops.opsfunc('node', node.tag, *node.coord)

# soil material
ops.opsfunc('nDMaterial', 'ElasticIsotropic', 1, 1.0e10, 0.49, 6.75)

# soil element
for element in rec.elements:
    nodes = [node.tag for node in element.nodes]
    ops.opsfunc('element', 'quad', element.tag, *nodes, 1.0, 'PlaneStrain', 1)

# load
ops.opsfunc('timeSeries', 'Linear', 1)
ops.opsfunc('pattern', 'Plain', 1, 1)
for node in part.Node.search([4.0, 1.0], [6.0, 1.0]):
    ops.opsfunc('load', node.tag, 0.0, -10.0)


# pile model
ops.opsfunc('model', 'basic', '-ndm', 2, '-ndf', 3)

# pile node
for node in line.nodes:
    ops.opsfunc('node', node.tag, *node.coord)

# boundary
ops.opsfunc('fix', line.nodes[0].tag, 1, 1, 0)
ops.opsfunc('fix', line.nodes[-1].tag, 0, 1, 0)

# pile element
ops.opsfunc('geomTransf', 'Linear', 1)
for element in line.elements:
    nodes = [node.tag for node in element.nodes]
    ops.opsfunc('element', 'elasticBeamColumn', element.tag, *nodes, 3600,
                4227, 1080000, 1)

# contact element
soil_node = part.Node.search([4.0, 0.0], [6.0, 0.0], rec.nodes)
pile_node = part.Node.search([0.0, 0.0], [10.0, 0.0], line.nodes)
nodes = soil_node + pile_node[-1::-1]
ele = part.Element(nodes, id0='contact')
ops.opsfunc('element', 'zeroLengthInterface2D', ele.tag, '-sNdNum',
            len(soil_node), '-mNdNum', len(pile_node), '-dof', 2, 3,
            '-Nodes', *[node.tag for node in ele.nodes], 1e8, 1e8, 16)
# print gid
ops.opsfunc('printGID', 'example1.msh')


# recorder
node_list = ops.opsfunc('getNodeTags')
ops.opsfunc('recorder', 'Node', '-file', 'disp.txt', '-node', *node_list,
            '-dof', 1, 2, 3, 'disp')
ops.opsfunc('recorder', 'Element', '-file', 'ele.txt', '-ele', 8, 'gap')

# analysis option
ops.opsfunc('integrator', 'LoadControl', 0.01)
ops.opsfunc('test', 'EnergyIncr', 1.0e6, 100, 5)
ops.opsfunc('algorithm', 'Newton')
ops.opsfunc('numberer', 'RCM')
ops.opsfunc('constraints', 'Plain')
ops.opsfunc('system', 'ProfileSPD')
ops.opsfunc('analysis', 'Static')
ops.opsfunc('analyze', 100)
print(ops.opsfunc('eleResponse', 8, 'force'))
# ops.opsfunc('printModel', 'ele')
# ops.opsfunc('printModel', 'node')

ops.opsfunc('wipe')

disp = np.loadtxt('disp.txt')
otg.node_result(node_list, [disp], ['Displacement'], 'Static', False,
                'example1.res')
