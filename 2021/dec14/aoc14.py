#import numpy as np
#from scipy.optimize import curve_fit
#import matplotlib.pyplot as plt

polymer=""
translations={}
pairCount=[]
firstLetter=''
lastLetter=''
#letters=[['B',0],['N',0],['C',0],['H',0]]
letters=[['P',0],['V',0],['O',0],['H',0],['F',0],['C',0],['K',0],['N',0],['S',0],['B',0]]
with open("input.txt") as data:
    polymer=data.readline()
    polymer=polymer.strip()
    firstLetter=polymer[:1]
    lastLetter=polymer[-1:]
    for line in data:
        line=line.strip()
        line=line.split(' -> ')
        translations[line[0]]=line[-1]
        tmp=line[0]
        pairSpawnA=tmp[:1]+line[1]
        pairSpawnB=line[1]+tmp[1:]
        pairCount.append([line[0],pairSpawnA,pairSpawnB,0])

def printPairs():
    print('Current pairs: ')
    for pair in pairCount:
        print(pair)
def countLetters():
    for letter in letters:
        for pair in pairCount:
            if pair[0][:1]==letter[0]:
                letter[1]=letter[1]+pair[3]
def expandPair(strPair,steps):
    flushPairCount()
    for pair in pairCount:
        if pair[0]==strPair:
            pair[3]=pair[3]+1
    for step in range(steps):
        PairsToUpdate=[]
        for pair in pairCount:
            if pair[3]>0:
                PairsToUpdate.append([pair[1],pair[3]])
                PairsToUpdate.append([pair[2],pair[3]])
                pair[3]=0       
        for update in PairsToUpdate:
            for i in range(len(pairCount)):
                if pairCount[i][0]==update[0]:
                    pairCount[i][3]=pairCount[i][3]+update[1]
    for letter in letters:
        for pair in pairCount:
            if pair[0][:1]==letter[0]:
                letter[1]=letter[1]+pair[3]
def flushPairCount():
    for pair in pairCount:
        pair[3]=0        

for char in range(len(polymer)-1):
    strPair=polymer[char:char+2]
    expandPair(strPair,10)

printPairs()
print(letters)
min_letter=-1
max_letter=0

for letter in letters:
    if letter[0]==lastLetter:
        letter[1]=letter[1]+1
    if letter[1]>max_letter:
        max_letter=letter[1]
    if letter[1]<min_letter or min_letter==-1:
        min_letter=letter[1]

print('Result2: '+str(max_letter-min_letter))


