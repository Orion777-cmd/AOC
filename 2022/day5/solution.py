with open('inputData.txt') as file:
    stack_strings, instructions = (i.splitlines() for i in file.read().strip('\n').split('\n\n'))

stacks = {int(digit):[] for digit in stack_strings[-1].replace(" ","")}
indexes = [index for index, char in enumerate(stack_strings[-1]) if char != " "]
moves = []


def displayStacks():
    print("\n\nStacks:\n")
    for stack in stacks:
        print(stack, stacks[stack])
    print("\n")


def loadStacks():
    for string in stack_strings[:-1]:
        stack_num = 1
        for index in indexes:
            if string[index] == " ":
                pass
            else:
                stacks[stack_num].insert(0, string[index])
            stack_num += 1

def emptyStacks():
    for stack_num in stacks:
        stacks[stack_num].clear()

def getStackEnds():
    answer = ""
    for stack in stacks:
        answer += stacks[stack][-1] if stacks[stack] else ""
    return answer

def buildMoves():
    
    for instruction in instructions:
        inst = instruction.split()
        move = []
        for i in inst:
            if i.isdigit():
                move.append(int(i))
        moves.append(move)
    
#part One

def partOne():
    loadStacks()
    buildMoves()
    for move in moves:
        num, from_stack, to_stack = move
        for i in range(num):
            stacks[to_stack].append(stacks[from_stack].pop())
    print(getStackEnds())

def partTwo():
    emptyStacks()
    loadStacks()
    
    for move in moves:
        num , from_stack, to_stack = move
        length = len(stacks[to_stack])
      
        for i in range(num):
            if stacks[from_stack]:
                stacks[to_stack].insert(length, stacks[from_stack].pop())
    print(getStackEnds())
partOne()
partTwo()