f=open("../../small_dataset/RHSvertices_withTags.csv", "r")
g=open("../../small_dataset/LHSvertices.csv", "r")

tags=dict()
for line in f:
    vals = line.split(",")
    for i in xrange(3, len(vals)):
	  tags[vals[i]]=1

for line in g:
    vals = line.split(",")
    for i in xrange(6, len(vals)):
	  tags[vals[i]]=1

print len(tags.keys())

