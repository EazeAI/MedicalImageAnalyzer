import matplotlib.pyplot as plt
import numpy


pred=[ 0,0,1,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,
  0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,
  0,1,0,0,0,0,1,0,0,0,0,0,0,0]

act=[ 1,0,1,1,0,0,0,1,0,1,0,0,0,1,0,1,0,0,
  0,0,1,1,1,1,1,0,0,0,0,0,0,1,0,1,1,0,
  0,0,1,0,0,0,1,0,0,1,1,0,1,0]

normal=0
nodule=0
nod_nor=0
nor_nod=0
for i,j in zip(pred,act):
    if i==j and j==0:
        normal+=1
    elif i==j and j==1:
        nodule+=1
    elif i!=j and j==0:
        nor_nod+=1
    elif i!=j and j==1:
        nod_nor+=1

print (normal)
print (nodule)
print (nod_nor)
print (nor_nod)