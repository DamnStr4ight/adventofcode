score  = 0
score2 = 0
pairs  = []
import time
start_time = time.time()
with open("data.txt") as data:
    for line in data:
        line = line.strip('\n').split(',')
        tmp1 = line[0].split('-')
        tmp2 = line[1].split('-')
        pairs.append([tmp1,tmp2])

for pair in pairs:
    sublist1 = []
    for i in range(int(pair[0][0]),int(pair[0][1])+1,1):
        sublist1.append(i)
    sublist2 = []
    for i in range(int(pair[1][0]),int(pair[1][1])+1,1):
        sublist2.append(i)
    if(all(elem in sublist1  for elem in sublist2) or all(elem in sublist2  for elem in sublist1)):
        score+=1
    if(any(elem in sublist1  for elem in sublist2) or any(elem in sublist1  for elem in sublist2)):
        score2+=1
print(score)
print(score2)

print("--- %s seconds ---" % (time.time() - start_time))