import numpy as np
sum=sum2=0
games=[]
win_cnts=[]
with open("data.txt") as data:
    for line in data:
        temp=line.strip().split(" ")
        temp2=[]
        for i in range(len(temp)):
            if temp[i] != '':
                temp2.append(temp[i])
        games.append(temp2)
    for g in games:
        w_cnt=0
        w_numbers = []
        p_numbers= []
        found_bar=False
        for i in range(2,len(g)):
            if g[i]=='|':
                found_bar=True
            elif found_bar:
                p_numbers.append(int(g[i]))
            else:
                w_numbers.append(int(g[i]))
        for w in w_numbers:
            if w in p_numbers:
                w_cnt+=1
        if w_cnt:
            sum+=2**(w_cnt-1)
        win_cnts.append([w_cnt,1])
        
    for w in range(len(win_cnts)):
        if win_cnts[w][0]:
            end_w_cnt=w+win_cnts[w][0]
            if end_w_cnt>len(win_cnts):
                end_w_cnt=len(win_cnts)
            for i in range(w+1,end_w_cnt+1):
                win_cnts[i][1]+=win_cnts[w][1]
    for w in win_cnts:
        sum2+=w[1]

print("Answer1: " + str(sum))
print("Answer2: " + str(sum2))