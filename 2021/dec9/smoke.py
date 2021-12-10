map=[]
low_points=[]
unasigned_points=[]

result1=0

with open("input.txt") as data:
    for line in data:
        map.append(list(line))
    for i in range(len(map)):
        map[i].pop()
        map[i] = [int(i) for i in map[i]]
    y_max=len(map)-1
    x_max=len(map[0])-1
    for y in range(len(map)):
        for x in range(len(map[0])):
            unasigned_points.append([x,y])
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
            if point<left and point<right and point<top and point<bottom:
                result1+=point+1
                low_points.append([x,y])
                unasigned_points.pop(-1)
            if point==9:
            #we dont want to assign 9s to any basin later
                unasigned_points.pop(-1)
    print('Sum of risk level: '+str(result1))
    
    basins=[[]for _ in range(len(low_points))]
    #solution 2
    for point in range(len(low_points)):
        basins[point].append(low_points[point])
    while len(unasigned_points)>0:
        for point in range(len(unasigned_points)):
            for i in range(len(low_points)):
                for basin_point in basins[i]:                              
                    try:
                        x_distance=abs(basin_point[0]-unasigned_points[point][0])
                        y_distance=abs(basin_point[1]-unasigned_points[point][1])
                        if x_distance==1 and y_distance==0 or x_distance==0 and y_distance==1:
                            basins[i].append(unasigned_points[point])
                            unasigned_points.pop(point)
                    except:
                        pass               
    basin_sizes=[]
    for basin in basins:
        basin_sizes.append(len(basin))
    basin_sizes.sort()
    result2=basin_sizes[-1]*basin_sizes[-2]*basin_sizes[-3]
    print('Sum of largest basins is: '+str(result2))