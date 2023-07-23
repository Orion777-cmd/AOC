arrays = []
with open('inputData.txt', 'r') as f:
    current_array = []
    for line in f:
        line = line.strip()
        if line == "":
            arrays.append(current_array)
            current_array = []
        else:
            current_array.append(int(line))
    
    if current_array:
        arrays.append(current_array)

max_ = float('-inf')
for i in range(len(arrays)):
    if sum(arrays[i]) > max_:
        max_ = sum(arrays[i])
        index = i

# for part two to find the three elves with the most calories
new_arrays = []
for i in range(len(arrays)):
    new_arrays.append(sum(arrays[i]))

new_arrays.sort(reverse=True)

maxThree = new_arrays[0] + new_arrays[1] + new_arrays[2]
print(max_, 'calories carried by ', index+1,'th elf ')
print('the calorie carried by the three elves with the most calories is ', maxThree, 'calories')
