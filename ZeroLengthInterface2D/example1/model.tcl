wipe
model basic -ndm 2 -ndf 2
node 1 4.0 0.0
node 2 6.0 0.0
node 3 4.0 1.0
node 4 6.0 1.0
nDMaterial ElasticIsotropic 1 10000000000.0 0.49 6.75
element quad 1 1 2 4 3 1.0 PlaneStrain 1
timeSeries Linear 1
pattern Plain 1 1
load 3 0.0 -10.0
load 4 0.0 -10.0
model basic -ndm 2 -ndf 3
node 5 0.0 0.0
node 6 2.0 0.0
node 7 4.0 0.0
node 8 6.0 0.0
node 9 8.0 0.0
node 10 10.0 0.0
fix 5 1 1 0
fix 10 0 1 0
geomTransf Linear 1
element elasticBeamColumn 2 5 6 3600 4227 1080000 1
element elasticBeamColumn 3 6 7 3600 4227 1080000 1
element elasticBeamColumn 4 7 8 3600 4227 1080000 1
element elasticBeamColumn 5 8 9 3600 4227 1080000 1
element elasticBeamColumn 6 9 10 3600 4227 1080000 1
element zeroLengthInterface2D 7 -sNdNum 2 -mNdNum 6 -dof 2 3 -Nodes 1 2 10 9 8 7 6 5 100000000.0 100000000.0 16
printGID example1.msh
getNodeTags
recorder Node -file disp.txt -node 1 2 3 4 5 6 7 8 9 10 -dof 1 2 3 disp
recorder Element -file ele.txt -ele 8 gap
integrator LoadControl 0.01
test EnergyIncr 1000000.0 100 5
algorithm Newton
numberer RCM
constraints Plain
system ProfileSPD
analysis Static
analyze 100
eleResponse 8 force
wipe
