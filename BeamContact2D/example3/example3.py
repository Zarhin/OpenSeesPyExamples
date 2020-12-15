# -*-coding: utf-8 -*-
# author: zarhin

import openseespy.opensees as ops
import openseespy.postprocessing.Get_Rendering as opg
import opensees_to_gid as otg
import numpy as np

ops.wipe()
ops.model('basic', '-ndm', 2, '-ndf', 2)
# node
ops.node(1, -0.5, 0.5)
ops.node(2, 0.5, 0.5)
ops.node(3, 0.5, 1.5)
ops.node(4, -0.5, 1.5)

ops.fix(1, 1, 0)
# ops.fix(2, 1, 0)

# contact node
ops.node(10, -0.0, 0.0)
ops.node(11, 0.0, 0.0)

# material
ops.nDMaterial('ElasticIsotropic', 1, 200000, 0.49, 1.9)
# element
ops.element('quad', 1, 1, 2, 3, 4, 1.0, 'PlaneStrain', 1, 0.0, 0.0, 0.0,
            -0.0)

ops.model('basic', '-ndm', 2, '-ndf', 3)

# node
ops.node(5, -2.0, 0.0)
ops.node(6, -1.0, 0.0)
ops.node(7, -0.0, 0.0)
ops.node(8, 1.0, 0.0)
ops.node(9, 2.0, 0.0)

# boundary
ops.fix(5, 1, 1, 0)
ops.fix(9, 0, 1, 0)

# element
ops.geomTransf('Linear', 1)
ops.element('elasticBeamColumn', 2, 5, 6, 0.5, 2e5, 0.049, 1)
ops.element('elasticBeamColumn', 3, 6, 7, 0.5, 2e5, 0.049, 1)
ops.element('elasticBeamColumn', 4, 7, 8, 0.5, 2e5, 0.049, 1)
ops.element('elasticBeamColumn', 5, 8, 9, 0.5, 2e5, 0.049, 1)

# contact material
ops.nDMaterial('ContactMaterial2D', 2, 0.1, 100000.0, 0.0, 0.0)

# contact element
ops.element('BeamContact2D', 6, 6, 7, 1, 10, 2, 0.5, 1e-10, 1e-10)
ops.element('BeamContact2D', 7, 7, 8, 2, 11, 2, 0.5, 1e-10, 1e-10)

# recorder
ops.printGID('model.msh')
node_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ops.recorder('Node', '-file', 'disp.txt', '-time', '-node', *node_list,
             '-dof', 1, 2, 'disp')
# load
ops.timeSeries('Constant', 1)
ops.pattern('Plain', 1, 1)
ops.load(3, 0, -1000)
ops.load(4, 0, -1000)
a = ops.nodeBounds()
print(a)
opg.plot_model()
# analysis
ops.constraints('Transformation')
ops.test('NormDispIncr', 1e-4, 15, 1)
ops.algorithm('Newton')
ops.numberer('RCM')
ops.system('SparseGeneral')
ops.integrator('LoadControl', 1)
ops.analysis('Static')

# set contact elements to be frictionless for gravity analysis
ops.setParameter('-val', 0, '-eleRange', 6, 7, 'friction')
ops.analyze(5)

ops.setParameter('-val', 1, '-eleRange', 6, 7, 'friction')
ops.analyze(5)

ops.wipe()
disp = np.loadtxt('disp.txt')
otg.node_result(node_list, [disp], ['Disp'], 'Load')