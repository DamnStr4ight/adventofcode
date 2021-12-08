
result1=0
result2=0
decoded=[0 for _ in range(7)]
digits=['a' for _ in range(10)]
topSegment='a'
with open("example.txt") as data:
    for line in data:
        segments=line.split();
        for i in range(5):
            lampsOn=len(segments[-(i+1)])
            if lampsOn==2 or lampsOn==3 or lampsOn==4 or lampsOn==7:
                result1+=1

    print('Result1: '+str(result1))

with open("input.txt") as data:
    for line in data:
        segments=line.split()
        #find the easy once
        for i in range(10):
            #print(segments[i])
            if len(segments[i])==2:
                digits[1]=segments[i]
            elif len(segments[i])==3:
                digits[7]=segments[i]
            elif len(segments[i])==4:
                digits[4]=segments[i]
            elif len(segments[i])==7:
                digits[8]=segments[i]
        one=digits[1]
        seven=digits[7]
        four=digits[4]
        topSegment='a'
        rightSide1=one[0]
        rightSide2=one[1]
        for char in one:
            seven=seven.replace(char,'')
        topSegment=seven
        decoded[0]=topSegment
        for char in one:
            four=four.replace(char,'')
        middleOrRightTop1=four[0]
        middleOrRightTop2=four[1]
        #print(digits)
        #print('Top Segment: '+topSegment)
        for i in range(10):
            if len(segments[i])==5 and rightSide1 in segments[i] and rightSide2 in segments[i]:
                digits[3]=segments[i]
        if middleOrRightTop1 in digits[3]:
            decoded[1]=middleOrRightTop2
            decoded[3]=middleOrRightTop1
        else:
            decoded[1]=middleOrRightTop1
            decoded[3]=middleOrRightTop2
        for i in range(10):
            if len(segments[i])==5 and decoded[1] in segments[i]:
                digits[5]=segments[i]
                if rightSide1 in digits[5]:
                    decoded[5]=rightSide1
                    decoded[2]=rightSide2
                elif rightSide2 in digits[5]:
                    decoded[5]=rightSide2
                    decoded[2]=rightSide1
        for i in range(10):
            if len(segments[i])==5 and decoded[2] in segments[i] and decoded[5] not in segments[i]:
                digits[2]=segments[i]
            elif len(segments[i])==6 and decoded[3] not in segments[i]:
                digits[0]=segments[i]
            elif len(segments[i])==6 and decoded[2] not in segments[i]:
                digits[6]=segments[i]
            elif len(segments[i])==6:
                digits[9]=segments[i]
        for i in range(len(segments)):
            segments[i]=''.join(sorted(segments[i]))
        for i in range(len(digits)):
            digits[i]=''.join(sorted(digits[i]))
        outputNumber=0
        pos=1
        for i in range (5):
            digit=segments[-(i+1)]
            for i in range(len(digits)):
                if digit==digits[i]:
                    outputNumber+=i*pos
            pos=pos*10
        print(outputNumber)
        result2+=outputNumber
                    
        print(digits)
        print(decoded)
        print(result2)
        