expenses=[]

with open("input.txt") as data:
    for line in data:
        line.strip()
        expenses.append(int(line))
print(expenses)
for expense in expenses:
    for i in range(len(expenses)):
        for j in range(len(expenses)):
            if expense + expenses[i]+expenses[j]==2020:
            #print(str(expense)+' and '+str(expenses[i])+' makes 2020 and multiplied is: '+str(expense * expenses[i]))
                print(expense * expenses[i]*expenses[j])
