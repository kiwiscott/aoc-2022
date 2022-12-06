import sys
from itertools import * 

def parse(puzzle_input):
    return puzzle_input[0]

def signal(fixed_len, data):
    """Solve part 1""" 
    a = [None] * fixed_len

    for index, c in enumerate(data):
        a.insert(0,c)
        a.pop()

        if None not in a and fixed_len == len(a) == len(set(a)): 
            return index + 1
    
    return None
            
def part1(data):
    """Solve part 2"""
    return signal(4,data)

def part2(data):
    """Solve part 2"""
    return signal(14,data)
    

if __name__ == "__main__":
    for path in sys.argv[1:]:
        puzzle_input = open(path + '.txt').readlines()

        data = parse(puzzle_input)

        solution1 = part1(data)
        print("%s puzzle 1 : %s" % (path, solution1))

        data = parse(puzzle_input)
        solution2 = part2(data)
        print("%s puzzle 2 : %s" % (path, solution2))

