import numpy as np
sum=sum2=game=0
max =  [12,13,14]#red,green,blue
colors = ["red","green","blue"]
topPulls = []

with open("data.txt") as data:
    for line in data:
        #1
        topPulls.append([0,0,0])
        pulls=line.split(" ")
        for p in range(len(pulls)):
            for c in range(len(colors)):
                if colors[c] in pulls[p]:
                    if int(pulls[p-1])>topPulls[game][c]:
                        topPulls[game][c]=int(pulls[p-1])
        game+=1
    for tp in topPulls:
        sum+=topPulls.index(tp)+1
        sum2+=np.prod(tp)
        for m in range(len(max)):
            if tp[m]>max[m]:
                sum-=topPulls.index(tp)+1
                break
        #2

print("Answer1: " + str(sum))
print("Answer2: " + str(sum2))