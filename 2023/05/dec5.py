import numpy as np
sum=sum2=0
map_idx=-1
seeds=[]
maps=[[] for x in range(7)]
locations = []
#parse
with open("data.txt") as data:
    for line in data:
        if "seeds:" in line:
            temp=line.strip().split(' ')
            temp.pop(0)
            seeds=[eval(i) for i in temp]
        if line[0]=='\n':
            map_idx+=1
        if line[0].isdigit():
            temp=line.strip().split(' ')
            submap=[eval(i) for i in temp]
            maps[map_idx].append(submap)
#map
for s in seeds:
    source=s
    for map in maps:
        for submap in map:
            if source in range(submap[1],submap[1]+submap[2]):
                source=submap[0]-submap[1]+source
                break
    locations.append(source)
locations.sort()
sum=locations[0]


seed_found=False
seed_ranges=[]
for s in range(0,len(seeds),2):
    seed_ranges.append([seeds[s],seeds[s]+seeds[s+1]])
maps.reverse()
destination=0
location=0
while not seed_found:
    if(location%10):
        print("Trying location" + str(location))
    for map in maps:
        for submap in map:
            if destination in range(submap[0],submap[0]+submap[2]):
                destination=submap[1]-submap[0]+destination
                break
    for s in seed_ranges:
        if destination in range(s[0],s[1]):
            seed_found=True
            sum2=location
    location+=1
    destination=location
    
print("Answer1: " + str(sum))
print("Answer2: " + str(sum2))