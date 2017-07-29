"""
f = open("../../small_dataset/event_location.csv", "r")
g= open("../../small_dataset/event_location_HK.csv", "w+")

first = True
for line in f:
    if first:
        first = False
	continue
    vals = line.split(",")
    longitude = float(vals[1])
    latitude = float(vals[2].split("\n")[0])

    if longitude>= 113.843 and longitude <= 114.283:
	if latitude>=22.209 and latitude<=22.609:
	    g.write(line)	

g.close()
"""

f = open("../../small_dataset/user_location.csv", "r")
g = open("../../small_dataset/user_location_HK.csv", "w+")

first = True
for line in f:
    if first:
        first = False
	continue
    vals = line.split(",")
    longitude = float(vals[1])
    latitude = float(vals[2].split("\n")[0])

    if longitude>= 113.843 and longitude <= 114.283:
	if latitude>=22.209 and latitude<=22.609:
	    g.write(line)	

g.close()



