import sys
from itertools import * 

def parse(puzzle_input):
    return puzzle_input


def part1(data):
    """Solve part 1""" 


def part2(data):
    """Solve part 2"""

if __name__ == "__main__":
    for path in sys.argv[1:]:
        puzzle_input = open(path + '.txt').readlines()

        data = parse(puzzle_input)

        solution1 = part1(data)
        print("%s puzzle 1 : %s" % (path, solution1))

        solution2 = part2(data)
        print("%s puzzle 2 : %s" % (path, solution2))

