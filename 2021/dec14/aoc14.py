polymer=""
translations={}
with open("input.txt") as data:
    polymer=data.readline()
    polymer=polymer.strip()
    for line in data:
        line=line.strip()
        line=line.split(' -> ')
        translations[line[0]]=line[-1]

def insertChars():
    stringLength=len(polymer)
    tmp=list(polymer)
    charToInsert=[]
    newpolymer=[]
    newPolymerStr=''
    for char in range(stringLength-1):
        charToInsert.append(translations.get(polymer[char:char+2]))
    for char in range(len(tmp)):
        newpolymer.append(tmp[char])
        if char<len(charToInsert):
            newpolymer.append(charToInsert[char])
    newPolymerStr=newPolymerStr.join(newpolymer)
    return newPolymerStr
def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num
def least_frequent(List):
    counter = -1
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency< counter or counter==-1):
            counter = curr_frequency
            num = i
 
    return num
#print(polymer)
#print(translations)
#print(translations.get('NN'))
for step in range(40):
    print('Step: '+str(step))
    polymer=insertChars()
polymerList=list(polymer)
#print(most_frequent(polymerList))
#print(least_frequent(polymerList))
print(polymerList.count(most_frequent(polymerList))-polymerList.count(least_frequent(polymerList)))
#print(polymer)