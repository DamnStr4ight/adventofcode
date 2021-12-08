increased = 0

with open("input.txt") as msmnt:
    prev_msmnt=int(msmnt.readline())
    for current_msmnt in msmnt:
        current_msmnt = int(current_msmnt.replace('\n',''))
        if (current_msmnt > prev_msmnt):
            increased+=1
            print(str(current_msmnt)+' increase')
        else:
            print(str(current_msmnt)+' decrease')
        prev_msmnt=current_msmnt
print(increased)
