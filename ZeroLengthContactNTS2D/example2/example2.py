# -*- coding: utf-8
# author: zarhin
# date: 2020/8/6 16:04

import part
import openseesfunction as ops

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
rec2_nodes, rec2_element = rec1.mesh()

# opensees model
ops.opsfunc('wipe')
ops.opsfunc('model', 'basic', '-ndm', 2, '-ndf', 2)

# opensees nodes
nodes = rec1_nodes + rec2_nodes
for node in nodes:
    ops.Node(node.coord, tag=node.tag)

