import random
import math

f=open("../../small_dataset/LHSvertices.csv", "r")
g=open("../../small_dataset/deadlines.csv", "w+")

U=dict()
T=300

for line in f:
  vals=line.split(",")
  r=random.uniform(0,1)
  r=math.ceil(r*T)
  g.write(vals[0]+","+str(T)+"\n")


