from operator import itemgetter
sum=sum2=0
hands1=[]
hands2=[]
cards='23456789TJQKA'
cards2='J23456789TQKA'

HIGH_CARD=1
PAIR=2
TWO_PAIR=3
THREE_OF_KIND=4
FULL_HOUSE=5
FOUR_OF_KIND=6
FIVE_OF_KIND=7

with open("data.txt") as data:
    for line in data:
        temp=line.strip().split(' ')
        hands1.append([temp[0],int(temp[1])])
        hands2.append([temp[0],int(temp[1])])

def CheckHands(taskNr,hand_list):
    for h in hand_list:
        if taskNr==2:
            jacks=h[0].count('J')
        else:
            jacks=0
        if len(set(h[0]))==1:
            h.append(FIVE_OF_KIND)
        elif len(set(h[0]))==2:
            occurances=h[0].count(h[0][0])
            #four of a kind
            if occurances==4 or occurances==1:
                if jacks > 0:
                    h.append(FIVE_OF_KIND)
                else:
                    h.append(FOUR_OF_KIND)
            #full house
            else:
                if jacks>0:
                    h.append(FIVE_OF_KIND)
                else:
                    h.append(FULL_HOUSE)
        elif len(set(h[0]))==3:
            #three of a kind
            if h[0].count(h[0][0])==3 or h[0].count(h[0][1])==3 or h[0].count(h[0][2])==3:
                if jacks==3 or jacks==1:
                    h.append(FOUR_OF_KIND)
                else:
                    h.append(THREE_OF_KIND)
            #two pair
            else:
                if jacks==2:
                    h.append(FOUR_OF_KIND)
                if jacks==1:
                    h.append(FULL_HOUSE)
                else:
                    h.append(TWO_PAIR)
        #pair
        elif len(set(h[0]))==4:
            if jacks==1 or jacks==2:
                h.append(THREE_OF_KIND)
            else:
                h.append(PAIR)
        #high card
        elif len(set(h[0]))==5:
            if jacks==1:
                h.append(PAIR)
            else:
                h.append(HIGH_CARD)

CheckHands(1,hands1)
hands1=sorted(hands1, key=lambda word: [cards.index(c) for c in word[0]])
hands1=sorted(hands1, key=itemgetter(2))
CheckHands(2,hands2)
hands2=sorted(hands2, key=lambda word: [cards2.index(c) for c in word[0]])
hands2=sorted(hands2, key=itemgetter(2))
for h in range(len(hands1)):
    sum+=hands1[h][1]*(h+1)
for h in range(len(hands2)):
    sum2+=hands2[h][1]*(h+1)
print("Answer1: " + str(sum))
print("Answer2: " + str(sum2))