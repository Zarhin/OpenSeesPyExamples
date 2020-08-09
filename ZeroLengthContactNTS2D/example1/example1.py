# -*- coding: utf-8
# author: zarhin
# date: 2020/8/6 16:01

import numpy as np
import openseesfunction as ops
import opensees_to_gid as otg

ops.opsfunc('wipe')

ops.opsfunc('model', 'basic', '-ndm', 2, '-ndf', 2)
# nDMaterial ElasticIsotropic $matTag $E $v <$rho>
ops.opsfunc('nDMaterial', 'ElasticIsotropic', 1, 1.0e10, 0.49, 6.75)

# ################################
# build the model
# #################################
# y
# |
# 7-------6
# | slave |
# 8-------5
# 4-------3
# | master|
# 1-------2---->x
#

ops.opsfunc('node', 1, 0.0, 0.0)
ops.opsfunc('node', 2, 1.0, 0.0)
ops.opsfunc('node', 3, 1.0, 1.0)
ops.opsfunc('node', 4, 0.0, 1.0)
ops.opsfunc('node', 5, 1.0, 1.0)
ops.opsfunc('node', 6, 1.0, 2.0)
ops.opsfunc('node', 7, 0.0, 2.0)
ops.opsfunc('node', 8, 0.0, 1.0)

ops.opsfunc('element', 'quad', 1, 1, 2, 3, 4, 1, 'PlaneStrain', 1)
ops.opsfunc('element', 'quad', 2, 5, 6, 7, 8, 1, 'PlaneStrain', 1)


kn = 1e8
kt = 0
phi = 16.0
# element ZeroLengthContactNTS2D eleTag? -sNdNum sNode? -mNdNum mNode?
# -Nodes Nodes? Kn? Kt? phi?
ops.opsfunc('element', 'zeroLengthContactNTS2D', 3, '-sNdNum', 2, '-mNdNum',
            2, '-Nodes', 3, 4, 8, 5, kn, kt, phi)

mass = {}
node_list = ops.opsfunc('getNodeTags')
for node in node_list:
    mass[node] = ops.opsfunc('nodeMass', node, 1, 2)

print(mass)

ops.opsfunc('fix', 1, 1, 1)
ops.opsfunc('fix', 2, 0, 1)

# gravity loads
ops.opsfunc('timeSeries', 'Constant', 1)
ops.opsfunc('pattern', 'Plain', 1, 1, '{')
ops.opsfunc('load', 6, 0.0, -10.0)
ops.opsfunc('load', 7, 0.0, -10.0, '}')

ops.opsfunc('printGID', 'model.msh')
# --------------------------------------------------------------------
# Start of static analysis (creation of the analysis & analysis itself)
# --------------------------------------------------------------------

ops.opsfunc('recorder', 'Node', '-file', 'disp.txt', '-time', '-nodeRange', 1,
            8, '-dof', 1, 2, 'disp')

# Load control with variable load steps
#                      init  Jd   min   max
# integrator LoadControl  0.01   1   1.0   10.0
ops.opsfunc('integrator', 'LoadControl', 0.01)

# Convergence test
#                tolerance maxIter displayCode
ops.opsfunc('test', 'EnergyIncr', 1.0e-6, 100, 5)

# Solution algorithm
ops.opsfunc('algorithm', 'Newton')

# DOF numberer
ops.opsfunc('numberer', 'RCM')

# Cosntraint handler
ops.opsfunc('constraints', 'Plain')

# System of equations solver
ops.opsfunc('system', 'ProfileSPD')

# Analysis for gravity load
ops.opsfunc('analysis', 'Static')

# Perform the analysis
ops.opsfunc('analyze', 100)
nodes = ops.opsfunc('getNodeTags')
ops.opsfunc('printModel', 'ele')
ops.opsfunc('printModel', 'node')
ops.opsfunc('wipe')
#
disp = np.loadtxt('disp.txt')
otg.node_result(nodes, [disp], ['displacement'], 'static analysis',
                'model.res')
