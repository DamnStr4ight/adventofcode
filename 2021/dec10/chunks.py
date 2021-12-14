import statistics
result1=0
result2=0
openers=['(','[','{','<']
closers=[')',']','}','>']
points=[3,57,1197,25137]
points2=[1,2,3,4]
expected_closers=[]
remaining_closers=[]
incomplete_scores=[]
chunk=''
incomplete=[]
#solution 1
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
                result1+=points[closers.index(char)]
                incomplete.pop(-1)
                break

#solution2
for line in incomplete:
    expected_closers=[]
    for char in line:
        if char in openers:
            expected_closers.append(closers[openers.index(char)])
        elif char==expected_closers[-1]:
            expected_closers.pop()
    score=0
    expected_closers=list(reversed(expected_closers))
    for char in expected_closers:
        score*=5
        score+=points2[closers.index(char)]
    incomplete_scores.append(score)
incomplete_scores.sort()
result2=statistics.median(incomplete_scores)

        
        
        
print('Result1: '+str(result1))
print('Result2: '+str(result2))
        