import random
f=open("../../small_dataset/Aevalues.csv", "r")
g=open("../../small_dataset/NonIntAevalues.csv", "w+")

for line in f:
  vals=line.split(",")
  for i in xrange(1, len(vals)):
    edge=vals[0]
    resource=vals[i].split("\n")[0]
    r=random.uniform(0,1)
    g.write(edge + "," + resource + "," + str(r) + "\n")
g.close()
