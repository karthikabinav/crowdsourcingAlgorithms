f=open("../../small_dataset/user_location_HK.csv", "r")

users = dict()
for line in f:
    vals=line.split(",")
    users[vals[0]] = dict()
    users[vals[0]]["lat"]=vals[2].split("\n")[0]
    users[vals[0]]["long"] = vals[1]
    users[vals[0]]["tags"] = list()
    users[vals[0]]["group"] = list()

f.close()

f=open("/scratch0/kabinav/meetup_dataset/meetup_user_tag.csv", "r")
for line in f:
    vals = line.split(",")
    if vals[0] not in users:
	continue
    users[vals[0]]["tags"].append(vals[1].split("\n")[0])
f.close() 
     
f=open("../../small_dataset/user_group_HK.csv", "r") 
for line in f:
    vals=line.split(",")
    users[vals[0]]["group"].append(vals[1])
f.close()

f=open("../../small_dataset/RHSvertices.csv", "w+")
for key in users:
    wr = key + "," + users[key]["lat"] + "," + users[key]["long"]
    for vals in users[key]["tags"]:
        wr = wr + "," + vals
    wr = wr + "\n"
    f.write(wr)
f.close()





