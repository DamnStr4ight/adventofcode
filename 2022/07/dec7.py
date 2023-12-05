import sys
sys.setrecursionlimit(50000) 
lines=open("example.txt", 'r').read().split('\n')
#print(lines)
folders = {}
current_folder=''
depth = 0

for line in lines:
    if '$' in line:
        if "cd" in line:
            if ".." in line:
                depth -= 1
            else:
                current_folder=line.split(' ')[2]
                if current_folder not in folders:
                    folders[current_folder]=[]
    else:
        if line[0].isalpha():
            folders[current_folder].extend([line.split(' ')[1]])
        if line[0].isnumeric():
            folders[current_folder].extend([line.split(' ')[0]])

folder_sizes ={}

#while set(folder_sizes) !=set(folders):
#    for key in folders:
#        for item in folders[key]:
#            if str(item).isalpha() and item in folder_sizes:
#                print(item + " is counted")
#                print(folders[key])
#                idx=folders[key].index(item)
#                []=folder_sizes[item]
#                print(folders[key][folders[key].index(item)])#=folder_sizes[item]
#                print(folder_sizes[item])
#        if all(str(item).isnumeric() for item in folders[key]) and item not in folder_sizes:
#            folder_sizes[key]=sum([eval(i) for i in folders[key]])
#        print(folder_sizes)
#    print(folders)
            
#print(folder_sizes)

def add_path_to_directories(path, directories):
    if path not in directories.keys():
        directories[path] = 0
    return directories


def solution():
    f = open('data.txt', 'r')
    directories_size = {}
    current_stack = []
    current_path = ""
    for line in f:
        if line.startswith("$ cd"):
            if not line.startswith("$ cd ..") and not line.startswith("$ cd /"):
                current_path += f"/{line.split()[-1]}" if current_path != "/" else line.split()[-1]
                current_stack.append(current_path)
                directories_size = add_path_to_directories(current_path, directories_size)

            elif line.strip() == "$ cd /":
                current_path = "/"
                current_stack = ["/"]
                directories_size = add_path_to_directories(current_path, directories_size)

            elif line.strip() == "$ cd ..":
                current_path = "/".join(current_path.split("/")[:-1])
                current_stack.pop()

        if line[0].isdigit():
            file_size = int(line.split()[0])
            for directory in current_stack:
                directories_size[directory] += file_size

    final_list_task_1 = [el for el in directories_size.values() if el <= 100000]
    print("Task 1:")
    print(sum(final_list_task_1))

    MAX_USED_SIZE = 70000000 - 30000000
    current_root_size = directories_size["/"]
    space_to_free = current_root_size - MAX_USED_SIZE
    final_list_task_2 = sorted([el for el in directories_size.values() if el >= space_to_free])
    print("Task 2:")
    print(final_list_task_2[0])

    MAX_USED_SIZE = 70000000 - 30000000
    current_root_sixe = directories_size["/"]
    space_to_free = current_root_size - MAX_USED_SIZE
    final_list_task_2 = soret([el for el in directories_size.values() if el >= space_to_free])
    print("Task 2:")
    print(final_list_task_2)

solution()