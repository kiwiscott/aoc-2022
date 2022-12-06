import sys
from itertools import * 

def parse(puzzle_input):
    return puzzle_input[0]

def signal(fixed_len, data):
    """Solve part 1"""     
    for i in range(fixed_len, len(data)):
        s = data[i - fixed_len: i ]
        if len(s) == len(set(s)): 
            return i
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

