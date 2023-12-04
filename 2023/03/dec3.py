import numpy as np
sum=sum2=max_y=max_x=0
lines=[]
sym_coordinates=[]
numbers=[]
gear_coordinates=[]

def lookAhead(x,y):
    for x_n in range(x,max_x+1):
        if x_n==max_x:
            return max_x
        elif not lines[y][x_n].isdigit():
            return x_n

with open("data.txt") as data:
    for line in data:
        lines.append(line.strip())
    max_x=len(lines[0])
    #print(max_x)
    max_y=len(lines)
    #parse out all numbers and sybols, and their coordinates
    for y in range(max_y):
        x=0
        while x < max_x:
            if lines[y][x].isdigit():
                if x==max_x-1:
                    x=max_x+1
                else:
                    x_n=lookAhead(x+1,y)
                    numbers.append([lines[y][x:x_n],y,x,x_n-1])
                    x=x_n
            elif lines[y][x]=='*':
                sym_coordinates.append([y,x])
                gear_coordinates.append([y,x])
                x+=1
            elif not lines[y][x]=='.':
                sym_coordinates.append([y,x])
                x+=1
            else:
                x+=1
    #find out which once are part numbers
    for n in numbers:
        for s in sym_coordinates:
            if n[1]-1==s[0] or n[1]==s[0] or n[1]+1==s[0]:
                if n[2]-1 <= s[1] <= n[3]+1:
                    sum+=int(n[0])
                    break
    #find gear coordinates with 2 numbers adjacent:
    for g in gear_coordinates:
        adj_cnt=0
        adj=[]
        for n in numbers:
            if n[1]-1==g[0] or n[1]==g[0] or n[1]+1==g[0]:
                if n[2]-1 <= g[1] <= n[3]+1:
                    adj_cnt+=1
                    adj.append(int(n[0]))
        if adj_cnt==2:
            sum2+=np.prod(adj)
            
print("Answer1: " + str(sum))
print("Answer2: " + str(sum2))