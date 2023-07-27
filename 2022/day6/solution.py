with open('inputData.txt', 'r') as file:
    line = file.readline()
    line = line.split(',')
#can be implemented using a set and a two pointers approach(sliding window)
# print(len(line[0]))
def partOne(comm):
    visited = set()
    i, j = 0, 0
   
    while i < len(comm) and j < len(comm):
        # print(visited)
        if len(visited) == 4:
            return j
        elif comm[j] not in visited:
            visited.add(comm[j])
            j += 1
        elif comm[j] in visited:
            while i < len(comm) and comm[i] != comm[j]:
                visited.remove(comm[i])
                i += 1
            i += 1
            visited.add(comm[j])
            j += 1

# finding the message marker which happens after the 14 th distinct character
def partTwo(comm):
    visited = set()
    i, j = 0, 0
    while i < len(comm) and j < len(comm):
        if len(visited) == 14:
            return j
        elif comm[j] not in visited:
            visited.add(comm[j])
            j += 1
        elif comm[j] in visited:
            while i < len(comm) and comm[i] != comm[j]:
                visited.remove(comm[i])
                i += 1
            i += 1
            visited.add(comm[j])
            j += 1
    return j
        
test1 = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
test2 = 'nppdvjthqldpwncqszvftbrmjlhg'
test3 = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
test4 = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'

print(partOne(line[0]))

print(partTwo(line[0]))