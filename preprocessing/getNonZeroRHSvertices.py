f = open("../../small_dataset/RHSvertices.csv", "r")
g=open("../../small_dataset/RHSvertices_withTags.csv", "w+")

for line in f:
    vals=line.split(",")
    if len(vals)>3:
	g.write(line)
g.close()
  
