score,score2  = 0
pairs  = []
with open("data.txt") as data:
    for line in data:
        line = line.strip('\n').split(',')
        tmp1 = line[0].split('-')
        tmp2 = line[1].split('-')
        pairs.append([tmp1,tmp2])
for pair in pairs:
    sublist1 = [i for i in range(int(pair[0][0]),int(pair[0][1])+1,1)]
    sublist2 = [i for i in range(int(pair[1][0]),int(pair[1][1])+1,1)]
    if(all(elem in sublist1  for elem in sublist2) or all(elem in sublist2  for elem in sublist1)):
        score+=1
    if(any(elem in sublist1  for elem in sublist2) or any(elem in sublist1  for elem in sublist2)):
        score2+=1
print("solution1: " + str(score) + "    solution2: "+ str(score2))