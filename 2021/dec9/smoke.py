map=[]
low_points=[]

result1=0

def basin_search(x,y):
    point=map[y][x]
    if point==9:
        return 0
    if x==0:
        left=10
    else:
        left=map[y][x-1]
    if x==x_max:
        right=10
    else:
        right=map[y][x+1]
    if y==0:
        top=10
    else:
        top=map[y-1][x]
    if y==y_max:
        bottom=10
    else:
        bottom=map[y+1][x]            
    #print('top: '+str(top)+' bottom: '+str(bottom)+' left: '+str(left)+' right: '+str(right))
    if point<left or point<right or point<top or point<bottom:
        
    

with open("example.txt") as data:
    for line in data:
        map.append(list(line))
    for i in range(len(map)):
        map[i].pop()
        map[i] = [int(i) for i in map[i]]
    #print(map)
    #print('x elements '+str(len(map[0])))
    #print('y elements '+str(len(map)))
    y_max=len(map)-1
    x_max=len(map[0])-1
    for y in range(len(map)):
        for x in range(len(map[0])):
            point=map[y][x]
            if x==0:
                left=10
            else:
                left=map[y][x-1]
            if x==x_max:
                right=10
            else:
                right=map[y][x+1]
            if y==0:
                top=10
            else:
                top=map[y-1][x]
            if y==y_max:
                bottom=10
            else:
                bottom=map[y+1][x]            
            #print('top: '+str(top)+' bottom: '+str(bottom)+' left: '+str(left)+' right: '+str(right))
            if point<left and point<right and point<top and point<bottom:
                result1+=point+1
                low_points.append([x,y])
    print(low_points)
    basins=[[]for _ in range(len(low_points))]
    print(basins)
    print('Sum of risk level: '+str(result1))
    for point in range(len(low_points)):
        basins[point].append(low_points[point])
    for basin in range(len(basins)):
        searching=1
        while(searching):
            #search top
            success=basin_search(basins[basin][0]-1,basins[basin][1]-1)
            if(success):
                if [basins[basin][0]-1,basins[basin][1]-1] not in basins[basin]:
                    basins[basin].append([basins[basin][0]-1,basins[basin][1]-1])
            #check sides
            #if side is lower than its sides, add the point to basin
            
        
    
            