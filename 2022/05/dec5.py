import copy
answer = ''
num_stacks = 0

with open("data.txt","r") as d:
    num_stacks=int(len(d.readline())/4)
stacks=[[] for _ in range(num_stacks)]

with open("data.txt","r") as d:
    for line in d:
        if any(char.isdigit() for char in line):
            break
        for char in range(1,len(line),4):
            if line[char] != ' ':
                stacks[int(char/4)].append(line[char])
    d.readline() #pop the blank
    instructions = []
    for line in d:
        line=line.split(' ')
        instructions.append([int(line[1]),int(line[3]),int(line[5])])

def craneOperation(model, box_layout, moves):
    answer = ''
    for task in moves:
        for i in range(task[0]):
            tmp=box_layout[task[1]-1].pop(0)
            if model == 9000:
                box_layout[task[2]-1].insert(0,tmp)
            elif model == 9001:
                box_layout[task[2]-1].insert(i,tmp)
    for stack in box_layout:
        answer +=stack[0]
    return answer


print(craneOperation(9000, copy.deepcopy(stacks), instructions))
print(craneOperation(9001, copy.deepcopy(stacks), instructions))