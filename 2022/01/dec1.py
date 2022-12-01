elves = [[]]
idx=0
with open("data.txt") as data:
    for line in data:
        if line == "\n":
            idx+=1
            elves.append([])
        else:    
            elves[idx].append(int(line))
max_cal=[0,0,0]
for elf in elves:
    curr_elf_cal = 0
    for cal in elf:
        curr_elf_cal +=cal
    if curr_elf_cal>min(max_cal):
        max_cal[max_cal.index(min(max_cal))]=curr_elf_cal
tot_cal = 0
for i in max_cal:
    tot_cal +=i
print("Elf carrying the most: " + str(max(max_cal)))
print("Top three elfs carries: " + str(tot_cal))