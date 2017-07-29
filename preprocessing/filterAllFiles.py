"""
f= open("/scratch0/kabinav/meetup_dataset/event_group_time.csv", "r")
g = open("../../small_dataset/event_group_time_HK.csv", "w+")
h = open("../../small_dataset/event_location_HK.csv", "r")

events = dict()
for line in h:
    vals = line.split(",")
    events[vals[0]] = 1

first = True
for line in f:
    if first:
        first = False
	continue 
    vals = line.split(",")
    if vals[0] in events:
	g.write(line)
g.close()	
"""

"""
f= open("/scratch0/kabinav/meetup_dataset/group_tag.csv", "r")
g = open("../../small_dataset/event_group_time_HK.csv", "r")
h = open("../../small_dataset/group_tag_HK.csv", "w+")

groups = dict()

for line in g:
    vals= line.split(",")
    groups[vals[1]] = 1

first = True
for line in f:
     if first:
	first=False
	continue
     vals= line.split(",")
     if vals[0] in groups:	
	h.write(line)
h.close()
"""
"""
f=open("/scratch0/kabinav/meetup_dataset/meetup_user_tag.csv", "r")
g=open("../../small_dataset/user_location_HK.csv", "r")
h=open("../../small_dataset/meetup_user_tag_HK.csv", "w+")

users=dict()

for line in g:
    vals=line.split(",")
    users[vals[0]]=1
first = True
for line in f:
    if first:
	first=False
	continue
    vals=line.split(",")
    if vals[0] in users:
        h.write(line)
h.close()
"""
"""
f=open("/scratch0/kabinav/meetup_dataset/user_event_ym.csv", "r")
g1=open("../../small_dataset/user_location_HK.csv", "r")
g2=open("../../small_dataset/event_location_HK.csv", "r")
h=open("../../small_dataset/user_event_ym_HK.csv", "w+")


users=dict()
events=dict()
for line in g1:
    vals=line.split(",")
    users[vals[0]]=1
for line in g2:
    vals=line.split(",")
    events[vals[0]]=1    

first = True
for line in f:
    if first:
	first=False
	continue
    vals=line.split(",")
    if vals[0] in users and vals[1] in events:
        h.write(line)
h.close()
"""
f=open("/scratch0/kabinav/meetup_dataset/user_group.csv", "r")
g1=open("../../small_dataset/user_location_HK.csv", "r")
g2=open("../../small_dataset/group_tag_HK.csv", "r")
h=open("../../small_dataset/user_group_HK.csv", "w+")

users=dict()
events=dict()
for line in g1:
    vals=line.split(",")
    users[vals[0]]=1

for line in g2:
    vals=line.split(",")
    events[vals[0]]=1    

first = True
for line in f:
    if first:
	first=False
	continue
    vals=line.split(",")
    if vals[0] in users and vals[1] in events:
        h.write(line)
h.close()



