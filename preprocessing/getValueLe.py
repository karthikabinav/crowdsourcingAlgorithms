f=open("../../small_dataset/RHSvertices_withTags.csv", "r")
g=open("../../small_dataset/LHSvertices.csv", "r")

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

maxi=0
for keyr in rhsTags:
  for keyl in lhsTags:
    total = rhsTags[keyr].union(lhsTags[keyl])
    covered = rhsTags[keyr].intersection(lhsTags[keyl])
    maxi = max(maxi, len(total)-len(covered))

print maxi

