with open("inputData.txt") as file:
    commands = file.readlines()

dirs = {"/home":0}
path = "/home"

def buildDictionary():

    for command in commands:

    
        if command[0] == "$":
            
    
            if command[2:4] == "ls":
                pass
        
            elif command[2:4] == "cd":
        
                if command[5:6] == "/":
                    path = "/home"

                elif command[5:7] == "..":
                    path = path[0:path.rfind("/")]

            
                else:
                    dir_name = command[5:]             
                    path = path + "/" + dir_name       
                    dirs.update({path:0})               

        elif command[0:3] == "dir":
            pass

        else:
            size = int(command[:command.find(" ")])   
        
            dir = path
            for i in range(path.count("/")):
                dirs[dir] += size
                dir = dir[:dir.rfind("/")]

def partOne():
    totSize = 0
    for key, val in dirs.items():
        if val <= 100000:
            totSize += val
    return totSize


def partTwo():
    total_disk_space = 70000000
    needed_space = 30000000
    unused_space = abs(total_disk_space - dirs["/home"])
    min_directory_deleted = needed_space - unused_space
    # print(min_directory_deleted)
    sorted_dirs = {key: value for key, value in sorted(dirs.items(), key=lambda item: item[1])}
    for val in sorted_dirs.values():
        if val >= min_directory_deleted:
            return val
    
buildDictionary()
print(partOne())
print(partTwo())