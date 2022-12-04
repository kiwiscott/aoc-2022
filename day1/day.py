import sys
from itertools import * 

def parse(puzzle_input):
    groups = []
    collector = []
    for n in puzzle_input: 
        if(n != '\n'):
            collector.append(int(n))
        else:
            groups.append(collector)
            collector = [] 
    return groups


def part1(data):
    """Solve part 1""" 
    return max(map(sum,data))


def part2(data):
    """Solve part 2"""
    last3 = sorted(map(sum,data))[-3:]
    return sum(last3)

if __name__ == "__main__":
    for path in sys.argv[1:]:
        puzzle_input = open(path + '.txt').readlines()

        data = parse(puzzle_input)

        solution1 = part1(data)
        print("%s puzzle 1 : %s" % (path, solution1))

        solution2 = part2(data)
        print("%s puzzle 2 : %s" % (path, solution2))

