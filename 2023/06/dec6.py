import numpy as np
sum=sum2=0
times=[]
dists=[]
wins=[]
with open("data.txt") as data:
    temp=data.read().splitlines()
#1
times = [int(t) for t in temp[0].split()[1:]]
dists = [int(d) for d in temp[1].split()[1:]]
for t in range(len(times)):
    t_n=0
    while t_n<times[t]:
        if t_n*(times[t]-t_n) >=dists[t]:
            wins.append(len(range(t_n,times[t]-t_n))+1)
            t_n=times[t]+1
        t_n+=1  
sum=np.prod(wins)
#2
time = int(temp[0].split(":")[1].replace(" ", ""))
dist = int(temp[1].split(":")[1].replace(" ", ""))
for t in range(1,time):
    if t*(time-t) >=dist:
        sum2=len(range(t,time-t))+1
        break
print("Answer1: " + str(sum))
print("Answer2: " + str(sum2))