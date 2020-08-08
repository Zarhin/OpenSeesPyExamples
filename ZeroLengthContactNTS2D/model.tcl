wipe
model basic -ndm 2 -ndf 2
nDMaterial ElasticIsotropic 1 10000000000.0 0.49 6.75
node 1 0.0 0.0
node 2 1.0 0.0
node 3 1.0 1.0
node 4 0.0 1.0
node 5 1.0 1.0
node 6 1.0 2.0
node 7 0.0 2.0
node 8 0.0 1.0
element quad 1 1 2 3 4 1 PlaneStrain 1
element quad 2 5 6 7 8 1 PlaneStrain 1
element zeroLengthContactNTS2D 3 -sNdNum 2 -mNdNum 2 -Nodes 3 4 8 5 100000000.0 0 16.0
fix 1 1 1
fix 2 0 1
timeSeries Constant 1
pattern Plain 1 1 {
load 6 0.0 -10.0
load 7 0.0 -10.0 }
recorder Node -file disp.txt -time -nodeRange 1 8 -dof 1 2 disp
integrator LoadControl 0.01
test EnergyIncr 1e-06 100 5
algorithm Newton
numberer RCM
constraints Plain
system ProfileSPD
analysis Static
analyze 100
printModel ele
printModel node
