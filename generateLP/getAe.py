import random
f=open("../../small_dataset/RHSvertices_withTags.csv", "r")
g=open("../../small_dataset/LHSvertices.csv", "r")

h=open("../../small_dataset/edgeNumbers.csv", "r")

edgeNumbers = dict()
for line in h:
  vals=line.split(",")
  edgeNumbers[vals[1]+vals[2].split("\n")[0]]=vals[0]
h.close()

lhsTags=dict()
rhsTags=dict()

for line in f:
  vals=line.split(",")
  rhsTags[vals[0]]=set()
  for i in xrange(3,len(vals)):
    rhsTags[vals[0]].add(int(vals[i].split("\n")[0]))
f.close()

for line in g:
  vals=line.split(",")
  lhsTags[vals[0]]=set()
  for i in xrange(6,len(vals)):
    lhsTags[vals[0]].add(int(vals[i].split("\n")[0]))
g.close()

rw=open("../../small_dataset/Aevalues.csv", "w+")

maxi=0
AeMap=dict()
cnt=0
for keyr in rhsTags:
  for keyl in lhsTags:
    if keyr+keyl not in edgeNumbers:
      continue
    total = rhsTags[keyr].union(lhsTags[keyl])
    covered = rhsTags[keyr].intersection(lhsTags[keyl])
    wr = edgeNumbers[keyr+keyl]
    nonZero=total-covered
    for k in nonZero:
      if k not in AeMap:
        AeMap[k]=cnt
        cnt+=1
      wr = wr + "," + str(AeMap[k])
    wr = wr + "\n"
    rw.write(wr)
rw.close()

