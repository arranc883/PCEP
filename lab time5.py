d1 = {'Adam Smith':'A','Judy Paxton':'B+'}
d2 = {'Mary Louis':'A','Patrcik White':'C'}
d1.update(d2)
print(d1)

A = {'Tamil':92,'English':56,'maths':88,'Science':97, 'Social':89}
B = {'Tamil':78,'English':68,'maths':88,'Science':97, 'Social':56}


for (key,values) in set(A.items()) & set(B.items()):
    print('%s: %s is present in both A and B'% (key,values))