
outcomes ={'A X': [3], 'A Y': [4], 'A Z': [9], 'B X': [1], 'B Y': [5], 'B Z': [9], 'C X': [7], 'C Y': [2], 'C Z': [6]}
outcomes2 ={'A X': [3], 'A Y': [4], 'A Z': [8], 'B X': [1], 'B Y': [5], 'B Z': [9], 'C X': [2], 'C Y': [6], 'C Z': [7]}
my_points = 0
secondstrat=0
with open("data.txt",'r') as d:
    for line in d:
        my_points+=outcomes[line.strip("\n")][0]
        secondstrat+=outcomes2[line.strip("\n")][0]
print("My points first strat: "+ str(my_points))
print("My points second strat: "+ str(secondstrat))