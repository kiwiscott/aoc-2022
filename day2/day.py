import sys
from itertools import * 

outcomes = {
    ('R','R'): 3, 
    ('P','P'): 3, 
    ('S','S'): 3, 
    ('R','P'): 6, 
    ('R','S'): 0, 
    ('P','S'): 6, 
    ('P','R'): 0, 
    
    ('S','R'): 6, 
    ('S','P'): 0, 
}
card_value = {
    'R': 1, 
    'P': 2,
    'S':3  
}
p1_rps = {
    'A' : 'R', 
    'B' : 'P', 
    'C' : 'S', 
}
p2_rps = {
    'X' : 'R', 
    'Y' : 'P', 
    'Z' : 'S', 
}
win_lose_draw = {
    'X' : 0,
    'Y' : 3,
    'Z' : 6
}

def first(iterable, condition = lambda x: True):
    return next(x for x in iterable if condition(x))


def parse(puzzle_input):
    hands = []
    for d in puzzle_input: 
        hands.append((d[0],d[2]))
    return hands

def part1(data):
    """Solve part 1""" 
    value = 0 
    for d in data: 
        card_as_rps = ( p1_rps[d[0]], p2_rps[d[1]]  )
        value += outcomes[card_as_rps]
        value += card_value[card_as_rps[0]]
    return value


def part2(data):
    ##Anyway, the second column says how the round needs to end: 
    # X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!
    value = 0 
    for d in data: 
        points_needed = win_lose_draw[d[1]]
        value += points_needed

        p1c = p1_rps[d[0]]
        for outcome in outcomes:
            if p1c == outcome[0] and outcomes[outcome] ==points_needed:
                value += card_value[outcome[1]]
    return value

    


if __name__ == "__main__":
    for path in sys.argv[1:]:
        puzzle_input = open(path + '.txt').readlines()

        data = parse(puzzle_input)

        solution1 = part1(data)
        print("%s puzzle 1 : %s" % (path, solution1))

        data = parse(puzzle_input)
        solution2 = part2(data)
        print("%s puzzle 2 : %s" % (path, solution2))

