import re
dots=[]
folds=[]
with open("input.txt") as data:
    for line in data:
        if ',' in line:
            line=line.split(',')
            dots.append([int(line[0]),int(line[1])])
        if '=' in line:
            line=line.strip()
            line=line.split('=')
            line[0]=line[0].split(' ')[-1]
            folds.append([line[0],int(line[-1])])

def findsheetSize():
    x_max=0
    y_max=0
    for dot in dots:
        if dot[0]>x_max:
            x_max=dot[0]
        if dot[1]>y_max:
            y_max=dot [1]
    return x_max+1,y_max+1

def printSheet():
    for y in sheet:
        tmp=''
        print(tmp.join(y))
def fillDots():
    for dot in dots:
        sheet[dot[1]][dot[0]]='#'

def fillFold(fold):
    foldAlongAxis=fold[0]
    foldAlongIndex=fold[1]
    if foldAlongAxis=='x':
        for y in sheet:
            y[foldAlongIndex]='|'
    if foldAlongAxis=='y':
        for x in range(len(sheet[foldAlongIndex])):
            sheet[foldAlongIndex][x]='-'

def foldSheet(fold):
    foldAlongAxis=fold[0]
    foldAlongIndex=fold[1]
    fillFold(fold)
    if foldAlongAxis == 'y':
        linesToFold=y_max-foldAlongIndex
        for row in range(linesToFold):
            for col in range(x_max):
                    if sheet[row+linesToFold-1][col]=='#':
                        sheet[linesToFold-row-1][col]='#'
                        sheet[row+linesToFold-1][col]='.'
    if foldAlongAxis == 'x':
        linesToFold=x_max-foldAlongIndex
        for row in range(y_max):
            for col in range(linesToFold):
                    if sheet[row][col+linesToFold-1]=='#':
                        sheet[row][linesToFold-col-1]='#'
                        sheet[row][col+linesToFold-1]='.'
def countDots():
    result=0
    for row in sheet:
        for col in range(x_max):
            if row[col]=='|' or row[col]=='-':
                break
            elif row[col]=='#':
                result+=1
    return result
def findSolution():
    for row in range(len(sheet)):
        solution.append([])
        if sheet[row][0]=='-':
            break
        for col in range(row):
            if sheet[row][col]=='|':
                break
            else:
                solution[row].append(sheet[row][col])
def printSolution():
    for row in solution:
        tmp=''
        tmp=tmp.join(row)
        print(tmp)

x_max,y_max=findsheetSize()
sheet=[[' ' for _ in range(x_max)] for _ in range(y_max)]
fillDots()
foldSheet(folds[0])
print('Result1: '+str(countDots()))
for fold in folds:
    foldSheet(fold)
    if fold[0]=='y':
        sheet=sheet[:fold[1]]
        y_max=len(sheet)
    if fold[0]=='x':
        for row in range(y_max):
            sheet[row]=sheet[row][:fold[1]]
        x_max=len(sheet[0])
printSheet()