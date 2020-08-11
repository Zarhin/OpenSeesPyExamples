wipe
model basic -ndm 2 -ndf 2
node 1 0.0 0.0
node 2 1.0 0.0
node 3 2.0 0.0
node 4 3.0 0.0
node 5 4.0 0.0
node 6 5.0 0.0
node 7 6.0 0.0
node 8 7.0 0.0
node 9 8.0 0.0
node 10 9.0 0.0
node 11 10.0 0.0
node 12 0.0 1.0
node 13 1.0 1.0
node 14 2.0 1.0
node 15 3.0 1.0
node 16 4.0 1.0
node 17 5.0 1.0
node 18 6.0 1.0
node 19 7.0 1.0
node 20 8.0 1.0
node 21 9.0 1.0
node 22 10.0 1.0
node 23 0.0 1.0
node 24 1.0 1.0
node 25 2.0 1.0
node 26 3.0 1.0
node 27 4.0 1.0
node 28 5.0 1.0
node 29 6.0 1.0
node 30 7.0 1.0
node 31 8.0 1.0
node 32 9.0 1.0
node 33 10.0 1.0
node 34 0.0 2.0
node 35 1.0 2.0
node 36 2.0 2.0
node 37 3.0 2.0
node 38 4.0 2.0
node 39 5.0 2.0
node 40 6.0 2.0
node 41 7.0 2.0
node 42 8.0 2.0
node 43 9.0 2.0
node 44 10.0 2.0
fix 1 1 1
fix 12 1 1
fix 23 1 1
fix 34 1 1
nDMaterial ElasticIsotropic 1 100000.0 0.25 6.75
element quad 1 1 2 13 12 1.0 PlaneStrain 1
element quad 2 2 3 14 13 1.0 PlaneStrain 1
element quad 3 3 4 15 14 1.0 PlaneStrain 1
element quad 4 4 5 16 15 1.0 PlaneStrain 1
element quad 5 5 6 17 16 1.0 PlaneStrain 1
element quad 6 6 7 18 17 1.0 PlaneStrain 1
element quad 7 7 8 19 18 1.0 PlaneStrain 1
element quad 8 8 9 20 19 1.0 PlaneStrain 1
element quad 9 9 10 21 20 1.0 PlaneStrain 1
element quad 10 10 11 22 21 1.0 PlaneStrain 1
element quad 11 23 24 35 34 1.0 PlaneStrain 1
element quad 12 24 25 36 35 1.0 PlaneStrain 1
element quad 13 25 26 37 36 1.0 PlaneStrain 1
element quad 14 26 27 38 37 1.0 PlaneStrain 1
element quad 15 27 28 39 38 1.0 PlaneStrain 1
element quad 16 28 29 40 39 1.0 PlaneStrain 1
element quad 17 29 30 41 40 1.0 PlaneStrain 1
element quad 18 30 31 42 41 1.0 PlaneStrain 1
element quad 19 31 32 43 42 1.0 PlaneStrain 1
element quad 20 32 33 44 43 1.0 PlaneStrain 1
element zeroLengthInterface2D 21 -sNdNum 11 -mNdNum 11 -dof 2 2 -Nodes 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 1000000000.0 0 0
timeSeries Constant 1
pattern Plain 1 1 {
load 44 0.0 -100 }
printGID example2.msh
getNodeTags
recorder Node -file disp.txt -node 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 -dof 1 2 disp
integrator DisplacementControl 44 2 -0.001
test EnergyIncr 1e-06 100 5
algorithm Newton
numberer RCM
constraints Transformation
system ProfileSPD
analysis Static
analyze 500
printModel node 44 22
wipe
