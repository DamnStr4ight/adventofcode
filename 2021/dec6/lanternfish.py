population_squished=[0 for _ in range(9)]
with open("input.txt") as data:
    temp=data.readline()
    population=temp.split(',')
    population=[int(i) for i in population]
    for fish in population:
        population_squished[fish]+=1
    for days in range(256):
        next_pop=[0 for _ in range(9)]
        for fish in range(len(population_squished)):
            if fish==0:
                next_pop[6]=population_squished[0]
                next_pop[8]=population_squished[0]
            else:
                next_pop[fish-1]+=population_squished[fish]
        population_squished=next_pop
        if days == 79 or days==255:
            total_fish=0
            for fish in population_squished:
                total_fish+=fish
            print('Total fish after' +str(days+1)+ ' days: '+str(total_fish))