input = open("data.txt", 'r').readline()
window = [input[char] for char in range(14)]
for i in range(4,len(input)):
    if (len(window)==len(set(window))):
        print(i)
        break
    else:
        window.pop(0)
        window.append(input[i])
    