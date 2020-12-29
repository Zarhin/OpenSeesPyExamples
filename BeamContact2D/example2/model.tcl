wipe
model basic -ndm 2 -ndf 2
node 1 -1.5 0.0
node 2 -0.5 0.0
node 3 -1.5 1.0
node 4 -0.5 1.0
node 5 -1.5 2.0
node 6 -0.5 2.0
node 7 0.5 0.0
node 8 1.5 0.0
node 9 0.5 1.0
node 10 1.5 1.0
node 11 0.5 2.0
node 12 1.5 2.0
nDMaterial PressureDependMultiYield02 5 2 1.8 9600.0 27000.0 36 0.1 101.0 0.0 26 0.067 0.23 0.06 0.27 20 5.0 3.0 1.0 0.0 0.77 0.9 0.02 0.7 101.0
nDMaterial InitialStateAnalysisWrapper 1 5 2
nDMaterial ContactMaterial2D 2 0.1 1000.0 0.0 0.0
element quad 1 1 2 4 3 1.0 PlaneStrain 1 0.0 0.0 0.0 -17.658
element quad 2 3 4 6 5 1.0 PlaneStrain 1 0.0 0.0 0.0 -17.658
element quad 3 7 8 10 9 1.0 PlaneStrain 1 0.0 0.0 0.0 -17.658
element quad 4 9 10 12 11 1.0 PlaneStrain 1 0.0 0.0 0.0 -17.658
fix 1 1 0
fix 8 1 0
fix 3 1 0
fix 10 1 0
fix 5 1 0
fix 12 1 0
fix 1 0 1
fix 2 0 1
fix 7 0 1
fix 8 0 1
node 17 0.0 0.0
node 18 0.0 0.0
node 19 0.0 0.0
node 20 0.0 0.0
node 21 0.0 0.0
node 22 0.0 0.0
model basic -ndm 2 -ndf 3
node 13 0.0 -0.5
node 14 0.0 0.5
node 15 0.0 1.5
node 16 0.0 2.5
geomTransf Linear 1
section Elastic 1 200000000 0.7853981633974483 0.04908738521234052
beamIntegration Legendre 1 1 3
element dispBeamColumn 5 13 14 1 1
element dispBeamColumn 6 14 15 1 1
element dispBeamColumn 7 15 16 1 1
fix 13 0 1 0
element BeamContact2D 8 15 16 6 17 2 1.0 1e-10 1e-10
element BeamContact2D 9 15 16 11 18 2 1.0 1e-10 1e-10
element BeamContact2D 10 14 15 4 19 2 1.0 1e-10 1e-10
element BeamContact2D 11 14 15 9 20 2 1.0 1e-10 1e-10
element BeamContact2D 12 13 14 2 21 2 1.0 1e-10 1e-10
element BeamContact2D 13 13 14 7 22 2 1.0 1e-10 1e-10
printGID model.msh
getNodeTags
recorder Node -file disp.txt -time -nodeRange 1 22 -dof 1 2 disp
constraints Transformation
test NormDispIncr 1e-05 15 1
algorithm Newton
numberer RCM
system SparseGeneral
integrator LoadControl 0.1
analysis Static
InitialStateAnalysis on
updateMaterialStage -material 1 -stage 0
setParameter -val 0 -eleRange 8 13 friction
analyze 4
updateMaterialStage -material 1 -stage 1
analyze 4
InitialStateAnalysis off
setParameter -val 1 -eleRange 8 13 friction
analyze 4
wipe
