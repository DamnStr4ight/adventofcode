
result1=0
result2=0
openers=['(','[','{','<']
closers=[')',']','}','>']
points=[3,57,1197,25137]
points2=[1,2,3,4]
expected_closers=[]
remaining_closers=[]
chunk=''
incomplete=[]
with open("input.txt") as data:
    for line in data:
        incomplete.append(line.strip())
        for char in line:
            if char in openers:
                chunk+=char
                expected_closers.append(closers[openers.index(char)])
            elif char==expected_closers[-1]:
                chunk+=char
                expected_closers.pop()
            elif char!='\n':
                #print(line)
                print('Expected '+str(expected_closers[-1])+', but found ' +str(char)+ ' instead.')
                result1+=points[closers.index(char)]
                incomplete.pop(-1)
                break
print(incomplete)
for line in incomplete:
    for char in openers:
        num_openers=line.count(char)
        num_closers=line.count(closers[openers.index(char)])
        missing_closers=num_openers-num_closers
        result2+=points2[openers.index(char)]*missing_closers
        
        
        
print('Result1: '+str(result1))
print('Result2: '+str(result2))
        