import sys
import scipy.stats as stats
from collections import defaultdict
import numpy as np
from cvxopt import matrix
import random

#1-fname
#2-T
#3-B file
#4-P file

bfile = sys.argv[1]
pfile = sys.argv[2]
afile = sys.argv[3]
nonint = sys.argv[4]
K=3785 #total number of resources
T=300 #Total time steps

ROOT="./small_dataset/"
CSV=".csv"

f=open(ROOT + "Wevalues" + CSV, "r")

vals=list()
I=list()
J=list()

We=list()
for line in f:
    vals=line.split(",")
    We.append(float(vals[1].split("\n")[0]))

W=We*T #Weights vector

g=open(ROOT + pfile + CSV, "r")
b=list()

J=0
for line in g:
    b.append(float(line.split("\n")[0]))
    J+=1
g.close()

J/=T

g=open(ROOT + bfile + CSV, "r")
cnt=0
for line in g:
    b.append(float(line.split("\n")[0]))
    cnt+=1
g.close()

#construct A matrix in sparse format
valsl=list()
Il=list()
Jl=list()

vertices=dict()

count=0
f=open(ROOT + "RHSvertices_withTags" + CSV, "r")
for line in f:
    vals=line.split(",")
    vertices[vals[0]]=count
    count+=1
f.close()


edges=defaultdict(list)
f=open(ROOT + "edgeNumbers" + CSV, "r")
E=0
for line in f:
    vals=line.split(",")
    v=vertices[vals[1]]
    edges[v].append(vals[0])
    E+=1
f.close()


edgesK=defaultdict(list)
f=open(ROOT + afile + CSV, "r")
for line in f:
    vals=line.split(",")
    first = True
    for val in vals:
        if first:
            first=False
            continue
        edgesK[val.split("\n")[0]].append(vals[0])

#Top half of the A matrix
for j in xrange(J):
    for t in xrange(T):
        for ed in edges[j]:
            valsl.append(1.0)
            Il.append(J*t+j)
            Jl.append(E*t+int(ed)-1)

#Bottom half of the A matrix
for k in xrange(K):
    for t in xrange(T):
        valsl.append(0.0)
        Il.append(J*T + k)
        Jl.append(1)

f=open(ROOT+"NonIntAevalues"+CSV, "r")
nonIntValue=dict()
for line in f:
    vals=line.split(",")
    if vals[0] not in nonIntValue:
        nonIntValue[vals[0]]=dict()
    nonIntValue[vals[0]][vals[1]]=float(vals[2].split("\n")[0])
f.close()

for k in xrange(K):
    for t in xrange(T):
        for ed in edgesK[k]:
            if nonint=="NO":
                valsl.append(1.0)
            else:
                valsl.append(nonIntValue[ed][k]) 
            Il.append(J*T + k)
            Jl.append(t*int(ed))
print "Write to file"

fname = bfile + pfile + afile + nonint
ROOT = ROOT + "LP/"
f = open(ROOT + "vals_" + fname + CSV, "w+")
np.array(valsl).tofile(f, sep=",")
f.close()
f = open(ROOT + "I_" + fname + CSV, "w+")
np.array(Il).tofile(f, sep=",")
f.close()
f = open(ROOT + "J_" + fname + CSV, "w+")
np.array(Jl).tofile(f, sep=",")
f.close()
f = open(ROOT + "b_" + fname + CSV, "w+")
b=matrix(b)
np.array(b).tofile(f, sep=",")
f.close()
f = open(ROOT + "c_" + fname + CSV, "w+")
W=matrix(W)
np.array(W).tofile(f, sep=",")
f.close()

'''
f=open(ROOT + "valsl_" + bfile + pfile + afile + CSV, "w+")
for val in valsl:
    f.write(str(val) + "\n")
f.close()

f=open(ROOT + "Il_" + bfile + pfile + afile + CSV, "w+")
for val in Il:
    f.write(str(val) + "\n")
f.close()

f=open(ROOT + "Jl_" + bfile + pfile + afile + CSV, "w+")
for val in Jl:
    f.write(str(val) + "\n")
f.close()
'''
