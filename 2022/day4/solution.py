data = []
with open('inputData.txt', 'r') as f:
    for line in f:
        line = line.strip() 
        ranges = line.split(",")  
        
        range_list = []
        for range_str in ranges:
            start, end = map(int, range_str.split("-"))
            range_list.append((start, end))
        
        data.append(range_list)


def partOne():
    assignments  = 0
    for pairs in data:
        one, two = pairs
        a, b = one
        c, d = two
        if a >= c and b <= d or c >= a and d <= b:
            assignments += 1
    return assignments


def partTwo():
    assignments = 0
    for pairs in data:
        one, two = pairs
        a, b = one
        c, d = two
        if a >= c and a <=d or b >= c and b <= d or c >= a and c <= b or d >= a and d <= b:
            assignments += 1
    return assignments



print('the  assignment pairs does one range fully contain the other', partOne())
print('the number of assignment pairs do the ranges overlap?', partTwo())