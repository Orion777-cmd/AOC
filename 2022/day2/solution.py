strategy_guide = []
with open('inputData.txt', 'r') as f:
    for line in f:
        line = line.strip()
        
        strategy_guide.append(line)

"""
A: Rock ==> X for Rock
B: Paper ==> Y for Paper
C: Scissors ==> Z for Scissors

    Score Count
1 for rock  selected    
2 for paper selected
3 for scissors selected


0 for loss
3 for draw
6 for win

"""
score_count = {
    'X': 1, 
    'Y': 2,
    'Z': 3,
    'loss': 0,
    'draw': 3,
    'win': 6
}

# implementation
def partOne():
    tot_score = 0
    for round in strategy_guide:
        opponent, self = round[0], round[-1]
        if opponent == 'A':
            if self == 'X':
                tot_score += score_count[self] + score_count['draw']
            elif self == 'Y':
                tot_score += score_count[self] + score_count['loss']
            else:
                tot_score += score_count[self] + score_count['win']
        elif opponent == 'B':
            if self == 'Y':
                tot_score += score_count[self] + score_count['draw']
            elif self == 'Z':
                tot_score += score_count[self] + score_count['loss']
            else:
                tot_score += score_count[self] + score_count['win']
        else:
            if self == 'Z':
                tot_score += score_count[self] + score_count['draw']
            elif self == 'X':
                tot_score += score_count[self] + score_count['loss']
            else:
                tot_score += score_count[self] + score_count['win']
    return tot_score



# part two ( change of plans)

def partTwo():
    """
    x: loose
    y: draw
    z: win
    """
    new_score = 0
    for round in strategy_guide:
        opponent, self = round[0], round[-1]
        if opponent == 'A':
            if self == 'Z':
                new_score += score_count['win'] + score_count['Y']
            elif self == 'X':
                new_score += score_count['loss'] + score_count['Z']
            else:
                new_score += score_count['draw'] + score_count['X']
        elif opponent == 'B':
            if self == 'X':
                new_score += score_count['loss'] + score_count['X']
            elif self == 'Y':
                new_score += score_count['draw'] + score_count['Y']
            else:
                new_score += score_count['win'] + score_count['Z']
        else:
            if self == 'Y':
                new_score += score_count['draw'] + score_count['Z']
            elif self == 'Z':
                new_score += score_count['win'] + score_count['X']
            else:
                new_score += score_count['loss'] + score_count['Y']
    return new_score

print('the total score is: ', partOne())
print('the total score for the second strategy is: ', partTwo())