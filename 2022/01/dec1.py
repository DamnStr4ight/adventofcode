
idx=0
with open("example.txt") as data:
    elves = [eval(x.split('\n')) for x in data.read().split("\n\n")]
print(elves)
max_cal=[0,0,0]
for elf in elves:
    if sum(eval(x) for x in elf)>min(max_cal):
        max_cal[max_cal.index(min(max_cal))]=sum(eval(x) for x in elf)
print("Elf carrying the most: " + str(max(max_cal)))
print("Top three elfs carries: " + str(sum(max_cal)))