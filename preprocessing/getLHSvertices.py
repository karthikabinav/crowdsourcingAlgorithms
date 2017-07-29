import csv

f = open("../../small_dataset/event_location_HK.csv", "r")

events=dict()
for line in f:
    vals = line.split(",")
    events[vals[0]] = dict()
    events[vals[0]]["lat"] = float(vals[2].split("\n")[0])
    events[vals[0]]["long"] = float(vals[1])
    events[vals[0]]["group"] = -1
    events[vals[0]]["start_time"]=-1
    events[vals[0]]["end_time"] = -1
f.close()

f=open("../../small_dataset/event_group_time_HK.csv", "r")

for line in f:
    vals = line.split(",") 
    events[vals[0]]["group"] = vals[1]
    events[vals[0]]["start_time"] = int(vals[2])
    events[vals[0]]["end_time"] = int(vals[3].split("\n")[0])
f.close()

#f=open("../../small_dataset/group_tag_HK.csv", "w+")
f=open("/scratch0/kabinav/meetup_dataset/group_tag.csv", "r")

group_tags = dict()
for line in f:
    vals = line.split(",")
    group = vals[0]
    if group not in group_tags:
        group_tags[group] = list()
    group_tags[group].append(vals[1].split("\n")[0])
f.close() 

for key in events:
    events[key]["tags"] = list()
    if events[key]["group"] not in group_tags:
        continue   
   
    for vals in group_tags[events[key]["group"]]:
	events[key]["tags"].append(vals)


f = open('../../small_dataset/LHSvertices.csv', 'w+') 
for key in events:
    wr = ""
    wr = key + "," + str(events[key]["lat"]) + "," + str(events[key]["long"]) + "," + str(events[key]["group"]) + ","+ str(events[key]["start_time"]) + "," + str(events[key]["end_time"])
    for vals in events[key]["tags"]:
	wr = wr + "," + vals
    wr = wr + "\n" 
    f.write(wr)
f.close()
