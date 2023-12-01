import re
sum=0
sum2=0
numbers = ["zero","one","two","three","four","five","six","seven","eight","nine"]
with open("data.txt") as data:
    for line in data:
        #1
        temp=re.sub("[^0-9]", "", line)
        sum+=int(temp[0]+temp[-1])
        #2
        temp2=line
        for n in numbers:
            temp2=temp2.replace(n,n[0]+str(numbers.index(n))+n[-1])
        temp2=re.sub("[^0-9]", "", temp2)
        sum2+=int(temp2[0]+temp2[-1])
print("Answer1: " + str(sum))
print("Answer2: " + str(sum2))