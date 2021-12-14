connections=[]
caves=[]
paths=[]
smallCaves=[]
largeCaves=[]

def printList(liste):
    for line in liste:
        print(line)

def findNeighbours(cave):
    neighbours=[]
    for connection in connections:
        cavesInConnection=connection.split('-')
        if cave in cavesInConnection:
            if cave != cavesInConnection[0] and cavesInConnection[0] not in neighbours:
                neighbours.append(cavesInConnection[0])
            elif cave != cavesInConnection[1] and cavesInConnection[1] not in neighbours:
                neighbours.append(cavesInConnection[1])
    #print('Cave: '+cave+' has these neighbours '+str(neighbours)) 
    return neighbours

def removeDeadend(cave):
    tmp=[]
    for connection in connections:
        tmp.append(connection)
        cavesInConnection=connection.split('-')
        if cave in cavesInConnection:
            #print('removed :'+connection)
            tmp.pop()
    return tmp
def explorePath(path,visitedTwice):
    newPaths=[]
    lastVisitedCave=path[-1]
    if lastVisitedCave !='end':
        for connection in connections:
            newPath=[]
            cavesInConnection=connection.split('-')
            if cavesInConnection[0]==lastVisitedCave:
                if cavesInConnection[1].islower() and cavesInConnection[1] not in path or cavesInConnection[1].isupper() or path.count(visitedTwice)<2 and cavesInConnection[1]==visitedTwice:
                    for i in range(len(path)):
                        newPath.append(path[i])
                    newPath.append(cavesInConnection[1])
                    newPaths.append(newPath)    
    return newPaths

def removeIllegalPaths():
    for path in paths:
        if path[-1]!='end':
            allPaths.pop(allPaths.index(path))
            
            
            

#Start of program
with open("example.txt") as data:
    for line in data:
        line=line.strip()
        connections.append(line)
        cavesInLine=line.split('-')
        for cave in cavesInLine:
            if cave not in caves and cave !='-':
                caves.append(cave)
        if cavesInLine[0] !='start' and cavesInLine[-1] !='end':    
            connections.append(str(cavesInLine[-1])+'-'+str(cavesInLine[0]))

for cave in caves:
    if cave.islower() and cave != 'start' and cave !='end':
        smallCaves.append(cave)
    elif cave.isupper():
        largeCaves.append(cave)
startPaths=[]
#add all start paths
for connection in connections:
    cavesInConnection=connection.split('-')
    if cavesInConnection[0]=='start':
        startPaths.append([cavesInConnection[0]])
        startPaths[-1].append(cavesInConnection[1])

allPaths=[]
newPaths=[]
pathsToPop=[]
pathsToAdd=[]
printList(smallCaves)
for cave in smallCaves:
    print('Checking cave: '+str(cave))
    for start in startPaths:
        paths.append(start)
    visitedTwice=cave
    newPathAdded=1
    while(newPathAdded):
        print('paths present: ' + str(len(paths)))
        newPathAdded=0
        for path in paths:
            if(path[-1] !='end'):
                newPaths.append(explorePath(path,visitedTwice))
                #print('New paths found: '+str(newPaths[0]))
                if len(newPaths)>0:
                    newPathAdded=1
                    #print('Current paths: '+str(paths))
                    pathsToPop.append(path)
                    for i in newPaths[0]:
                        #print(i)
                        pathsToAdd.append(i)
                newPaths.clear()
            else:
                allPaths.append(path)
                pathsToPop.append(path)
        print('Removing: '+str(len(pathsToPop))+' paths')
        print('length path: '+str(len(paths)))
        for pop in pathsToPop:
            paths.pop(paths.index(pop))
        print('length path: '+str(len(paths)))
        for add in pathsToAdd:
            if add not in allPaths:
                paths.append(add)
        pathsToAdd.clear()
        pathsToPop.clear()
    paths.clear()
removeIllegalPaths()
#printList(paths)
print('There are: '+str(len(allPaths))+' paths in the cave system.') 