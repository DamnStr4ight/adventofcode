input = open("data.txt", 'r').readline()
def charsUntilSOF(window):
    for i in range(4,len(input)):
        if (len(window)==len(set(window))):
            return i
        else:
            window.pop(0)
            window.append(input[i])
print(charsUntilSOF([input[char] for char in range(4)]))
print(charsUntilSOF([input[char] for char in range(14)]))