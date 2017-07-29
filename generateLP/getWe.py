import math
f=open("small_dataset/RHSvertices_withTags.csv", "r")
g=open("small_dataset/LHSvertices.csv", "r")

h=open("small_dataset/edgeNumbers.csv", "r")

edgeNumbers = dict()
for line in h:
  vals=line.split(",")
  edgeNumbers[vals[1]+vals[2].split("\n")[0]]=vals[0]
h.close()

lhsLocation=dict()
rhsLocation=dict()

for line in f:
  vals=line.split(",")
  rhsLocation[vals[0]]=vals[1]+";"+vals[2].split("\n")[0]
f.close()

for line in g:
  vals=line.split(",")
  lhsLocation[vals[0]]=vals[1]+";"+vals[2].split("\n")[0]
g.close()

rw=open("small_dataset/Wevalues.csv", "w+")

for keyr in rhsLocation:
  for keyl in lhsLocation:
    if keyr+keyl not in edgeNumbers:
      continue
    lat1 = float(rhsLocation[keyr].split(";")[0])
    long1 = float(rhsLocation[keyr].split(";")[1])
    lat2 = float(lhsLocation[keyl].split(";")[0])
    long2 = float(lhsLocation[keyl].split(";")[1])

    wr = edgeNumbers[keyr+keyl]
    dist = 600-math.sqrt(((lat1-lat2)*1000)**2 + ((long1-long2)*1000)**2)
    wr = wr + "," + str(dist)
    wr = wr + "\n"
    rw.write(wr)
rw.close()

