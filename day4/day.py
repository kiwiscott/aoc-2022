import sys
from itertools import * 
import re 

##
## More memory used this way. most efficient way is to use simple math 
##

def parse(puzzle_input):
    regex = '^(\d*)-(\d*),(\d*)-(\d*)'
    pairs = [] 
    for l in puzzle_input:
        matches = re.match(regex, l)
        pairs.append(
                (
                    ( 
                        int(matches.group(1)) ,
                        int(matches.group(2)) 
                    ),
                    (
                        int(matches.group(3)) ,
                        int(matches.group(4)) 
                    )
                )
            )
    return pairs


def part1(data):
    """Solve part 1""" 
    wholly_contained_pairs = 0 
    for pair in data: 
        r1 = set(range(pair[0][0],pair[0][1]+1 ))
        r2 = set(range(pair[1][0],pair[1][1]+1 ))

        if len(r1 - r2) == 0 or len(r2-r1) == 0:
                wholly_contained_pairs += 1
    return wholly_contained_pairs 

def part2(data):
    """Solve part 2"""
    over_lapping_pairs = 0 
    for pair in data: 
        r1 = set(range(pair[0][0],pair[0][1]+1 ))
        r2 = set(range(pair[1][0],pair[1][1]+1 ))

        if len(r1 - r2) < len(r1)  or len(r2-r1) < len(r2):
            over_lapping_pairs += 1
    return over_lapping_pairs 


if __name__ == "__main__":
    for path in sys.argv[1:]:
        puzzle_input = open(path + '.txt').readlines()

        data = parse(puzzle_input)

        solution1 = part1(data)
        print("%s puzzle 1 : %s" % (path, solution1))

        solution2 = part2(data)
        print("%s puzzle 2 : %s" % (path, solution2))

