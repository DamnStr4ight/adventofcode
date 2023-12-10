from itertools import cycle
import math
sum=sum2=0
instructions=[]
nodes={}

with open("data.txt") as data:
    for line in data:
        #first line has only L's and R's
        if len(set(line.strip()))==2:
            instructions=list(line.strip())
        elif not line[0] =='\n':
            nodes.update({line[:3]:[line[7:10],line[12:15]]})

end_found=False
node='AAA'
end_node='ZZZ'
while not end_found:
    for inst in instructions:
        if node==end_node:
            end_found=True
            break
        sum+=1
        if inst=='L':
            node=nodes[node][0]
        else:
            node=nodes[node][1]
nodes2 = [n for n in nodes.keys() if n.endswith('A')]
steps = [0] * len(nodes2)
for i, n in enumerate(nodes2):
    print(i)
    print(n)
    pos = n
    for d in cycle(instructions):
        if d == 'L':
            pos=nodes[pos][0]
        else:
            pos=nodes[pos][1]
        steps[i] += 1
        if pos.endswith('Z'):
            break
sum2=math.lcm(*steps)
print("Answer1: " + str(sum))
print("Answer2: " + str(sum2))