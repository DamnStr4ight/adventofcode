lines = open("example.txt", 'r').read().split('\n')
stacks  = [[stack][0] for stack in [[line[i] for line in lines if len(line) > i and line[i].isupper()] for i in range(50)] if stack]
stacks2 = [[stack][0] for stack in [[line[i] for line in lines if len(line) > i and line[i].isupper()] for i in range(50)] if stack]
instructions = [[int(word) for word in line.split(' ') if word.isnumeric()] for line in lines if len(line) > 1 and line[0].islower()]
for instruction in instructions:
    for i in range(instruction[0]):
        stacks[instruction[2]-1].insert(0, stacks[instruction[1]-1].pop(0))
print("".join([stack[0] for stack in stacks]))
for instruction in instructions:
    stacks2[instruction[2]-1][0:0] = stacks2[instruction[1]-1][:instruction[0]]
    del stacks2[instruction[1]-1][:instruction[0]]
print("".join([stack[0] for stack in stacks2]))