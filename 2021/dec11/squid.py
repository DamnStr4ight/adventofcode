squids=[]
flashed=[[0 for _ in range(10)] for _ in range(10)]
result1=0
def printSquid():
    print('')
    for x in squids:
        print(x)
def printflashed():
    print('')
    for x in flashed:
        print(x)
def squidCharge():
    for row in range(len(squids)):
        for col in range(len(squids[row])):
            squids[row][col]+=1

def flashEffect(row,col):
    #print('Flasing on squid '+str(row)+' '+str(col))
    row_max=len(squids)-1
    col_max=len(squids)-1
    if row!=0:
        #print('Updating :'+str(row-1)+' '+str(col))
        squids[row-1][col]=squids[row-1][col]+1
    if row!=0 and col!=0:
        #print('Updating :'+str(row-1)+' '+str(col-1))
        squids[row-1][col-1]=squids[row-1][col-1]+1
    if row!=0 and col!=col_max:
        #print('Updating :'+str(row-1)+' '+str(col+1))
        squids[row-1][col+1]=squids[row-1][col+1]+1
    if col!=0:
        #print('Updating :'+str(row)+' '+str(col-1))
        squids[row][col-1]=squids[row][col-1]+1
    if col!=col_max:
        #print('Updating :'+str(row)+' '+str(col+1))
        squids[row][col+1]=squids[row][col+1]+1
    if row!=row_max and col!=0:
        #print('Updating :'+str(row+1)+' '+str(col-1))
        squids[row+1][col-1]=squids[row+1][col-1]+1
    if row!=row_max:
        #print('Updating :'+str(row+1)+' '+str(col))
        squids[row+1][col]=squids[row+1][col]+1
    if row!=row_max and col != col_max:
        #print('Updating :'+str(row+1)+' '+str(col+1))
        squids[row+1][col+1]=squids[row+1][col+1]+1
    #printSquid()
    

def squidFlash():
    flashDetected=0
    for row in range(len(squids)):
        for col in range(len(squids[row])):
            if squids[row][col]>9 and flashed[row][col]==0:
                flashDetected+=1
                flashEffect(row,col)
                flashed[row][col]=1
    return flashDetected
firstAllFlashingFound=0
with open("input.txt") as data:
    for line in  data:
        line=list(line.strip())
        line=[int(i) for i in line]
        squids.append(line)
    #print('Before any steps:')
    #printSquid()
    for step in range(1000):
        squidCharge()
        flashed=[[0 for _ in range(10)] for _ in range(10)]
        flashing=1
        while(flashing):
            tmp=0
            tmp=squidFlash()
            result1+=tmp
            if tmp==0:
                flashing=0
        for row in range(len(squids)):
            for col in range(len(squids[row])):
                if squids[row][col]>9:
                    squids[row][col]=0 
        #print('After step '+str(1+step)+':')
        #printSquid()
        #printflashed()
        #print(result1)
        howManyFlashed=0
        for row in range(len(flashed)):
            for col in range(len(flashed[row])):
                if flashed[row][col]==1:
                    howManyFlashed+=1
        #print(howManyFlashed)
        if howManyFlashed==100 and firstAllFlashingFound==0:
            print('Fisrt Step all flashed: '+str(step))
            firstAllFlashingFound=1
            break
    print('Result 1: '+str(result1))