rucksacks = []
with open('inputData.txt', 'r') as f:
    for line in f:
        line = line.strip()
        
        rucksacks.append(line)

# implementation
# calculating the priority of the common characters that are found on both sides of the rucksack 

def partOne():
    priority = 0
    for rucksack in rucksacks:
        mid = len(rucksack) // 2
        left = rucksack[:mid]
        right = rucksack[mid:]
        common = set()
        for i in left:
            if i in right and i not in common:
                if i.islower():
                    priority += ord(i) - 96
                else:
                    priority += ord(i) - 38
                common.add(i)
    return priority

def partTwo():
    priority = 0
    new_rucksacks = []
    j = 0
    for i in range(0, len(rucksacks), 3):
        group = []
        j = i
        while j < i + 3:
            group.append(rucksacks[j])
            j += 1
        new_rucksacks.append(group)
    
    for group in new_rucksacks:
        common = set()
        for i in group[0]:
            if i in group[1] and i in group[2] and i not in common:
                if i.islower():
                    priority += ord(i) - 96
                else:
                    priority += ord(i) - 38
                common.add(i)
    return priority


            
print('the priority of the common characters: ', partOne())
print('the priority for the three groups is: ',     partTwo())

