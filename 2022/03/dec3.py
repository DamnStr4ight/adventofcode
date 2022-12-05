score = 0
score2 =0

bags = []

groups= []

with open("data.txt") as data:
    idx=0
    for line in data:
        line=line.strip('\n')
        mid=int(len(line.strip('\n'))/2)+1
        first = line[:mid-1]
        second = line[mid-1:]
        bags.append([first,second])

        groups.append(line)
        print(groups)
    idx=0
    for bag in bags:
        idx+=1
        for char in bag[0]:
            if char in bag[1]:
                value = ord(char)
                if (value > 95):
                    score += value-96
                    break
                else:
                    score += value-38
                    break
    
    for i in range(0,len(groups),3):
        print(groups[i])
        for char in groups[i]:
            if ((char in groups[i+1]) and (char in groups[i+2])):
                value = ord(char)
                if (value > 95):
                    score2 += value-96
                    break
                else:
                    score2 += value-38
                    break


print(score)
print(score2)