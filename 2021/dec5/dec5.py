seafloor = [[0 for _ in range(1000)] for _ in range(1000)]
crosSections=0

with open("input.txt") as data:
    for line in data:
        temp=line.split()
        point1=temp[0].split(',')
        point2=temp[2].split(',')
        x1=int(point1[0])
        x2=int(point2[0])
        y1=int(point1[1])
        y2=int(point2[1])
        
        if(x1==x2):
            if(y1<y2):
                for dot in range(y1,y2+1):
                    seafloor[dot][x1]+=1
            else:
                for dot in range(y2,y1+1):
                    seafloor[dot][x1]+=1
        elif(y1==y2):
            if(x1<x2):
                for dot in range(x1,x2+1):
                    seafloor[y1][dot]+=1
            else:
                for dot in range(x2,x1+1):
                    seafloor[y1][dot]+=1
        else:
            #deal with diagonals
            y_current=y1
            if x1<x2:#left to right
                if y1<y2:#top to bottom
                    for x in range(x1,x2+1):
                        seafloor[y_current][x]+=1
                        y_current+=1
                else:#bottom to top
                    for x in range(x1,x2+1):
                        seafloor[y_current][x]+=1
                        y_current-=1
            else:#right to left
                if y1<y2:#top to bottom
                    x_left=x2
                    x_right=x1
                    y_current=y2
                    for x in range(x_left,x_right+1):
                        seafloor[y_current][x]+=1
                        y_current-=1
                else:
                    x_left=x2
                    x_right=x1
                    y_current=y2
                    for x in range(x_left,x_right+1):
                        seafloor[y_current][x]+=1
                        y_current+=1                                 
                    
                
                
    for row in seafloor:
        for column in row:
            if column>1:
                crosSections+=1
    print(crosSections)
   
        