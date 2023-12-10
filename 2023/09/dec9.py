import time
sum=sum2=0
histories=[]    
with open("data.txt") as data:
    for line in data:
        histories.append([[eval(i) for i in line.strip().split(' ')]])
for h in histories:
    i=0
    while (len(set(h[i]))!=1 or h[i][0]!=0):
        h.append([])
        for n in range(len(h[i])-1):
            h[i+1].append(h[i][n+1]-h[i][n])
        i+=1
for h in histories:
    for l in range(len(h)-1,-1,-1):
        if(h[l][0]==h[l][1]==h[l][-1]==0):
            h[l].append(0)
        else:
            h[l].append(h[l][-1]+h[l+1][-1])
for h in histories:
    for l in range(len(h)-1,-1,-1):
        if(h[l][0]==h[l][1]==h[l][-1]==0):
            h[l].insert(0,0)
        else:
            h[l].insert(0,h[l][0]-h[l+1][0])

for h in histories:
    sum+=h[0][-1]
    sum2+=h[0][0]
print("Answer1: " + str(sum))
print("Answer2: " + str(sum2))