f=open("../../small_dataset/LHSvertices.csv", "r")
g=open("../../small_dataset/RHSvertices_withTags.csv", "r")
g1=open("../../small_dataset/user_group_HK.csv", "r")
h=open("../../small_dataset/edgeNumbers.csv", "w+")

lhs=list()
lhsGroup=dict()
for line in f:
  vals = line.split(",")
  lhs.append(vals[0])
  lhsGroup[vals[0]]=vals[3]
f.close()

rhs=list()
rhsGroup=dict()

for line in g1:
  vals=line.split(",")
  rhsGroup[vals[0]]=vals[1]

count = 0
for line in g:
  vals=line.split(",")
  rhs.append(vals[0])
g.close()

num=1
for r in rhs:
  for l in lhs:
    if lhsGroup[l]==rhsGroup[r]:
      h.write(str(num) + "," + r + "," + l + "\n")
      num+=1
h.close()


