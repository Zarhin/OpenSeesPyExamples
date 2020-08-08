# -*- coding: utf-8
# author: zarhin
# date: 2020/8/6 16:04

import openseesfunction as ops
import part


p1 = part.Point([0.0, 0.0])
p2 = part.Point([10.0, 1.0])
p3 = part.Point([0.0, 1.0])
p4 = part.Point([10.0, 2.0])

# part 1
part.Node.reset()
part.Element.reset()
rec1 = part.Rectangle([p1, p2])
rec1.set_seed(general_size=1.0)
rec1_nodes, rec1_elements = rec1.mesh()

# part 2
rec2 = part.Rectangle([p3, p4])
rec2.set_seed(general_size=1.0)
rec2_nodes, rec2_elements = rec1.mesh()

# build opensees model
ops.opsfunc('wipe')

# model
ops.opsfunc('model', 'basic', '-ndm', 2, '-ndf', 2)

# node
nodes = rec1_nodes + rec2_nodes
for node in nodes:
    ops.Node(node.coord, tag=node.tag)
