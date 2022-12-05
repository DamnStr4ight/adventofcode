import copy
lines = open("data.txt", 'r').read().split('\n')
stacks  = [[stack][0] for stack in [[line[i] for line in lines if len(line) > i and line[i].isalpha()] for i in range(50)] if stack]
instructions = [[int(word) for word in line.split(' ') if word.isnumeric()] for line in lines if len(line) > 1 and line[0].isalpha()]
def craneOperation(model, box_layout, moves):
    for task in moves:
        for i in range(task[0]):
            tmp=box_layout[task[1]-1].pop(0)
            box_layout[task[2]-1].insert(0,tmp) if model==9000 else box_layout[task[2]-1].insert(i,tmp)
    return "".join([stack[0] for stack in box_layout])
print(craneOperation(9000, copy.deepcopy(stacks), instructions))
print(craneOperation(9001, copy.deepcopy(stacks), instructions))