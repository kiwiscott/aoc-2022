import sys
from itertools import * 
import string

def parse(puzzle_input):
    sacks = []
    for p in puzzle_input:
        p = p.strip("\n")
        compartment1 = [* p[:len(p)//2]]
        compartment2 = [* p[len(p)//2:]]
        sacks.append((compartment1,compartment2))
    return sacks


def part1(data):
    """Solve part 1""" 
    string_indices = (string.ascii_lowercase + string.ascii_uppercase)
    total =0 

    for compartment1, compartment2 in data:
        for c in set(compartment1).intersection(compartment2): 
            total += string_indices.find(c) + 1 
    return total 
        

def part2(data):
    """Solve part 2"""
    string_indices = (string.ascii_lowercase + string.ascii_uppercase)
    total = 0 

    for groups_of_three in batched(data,3): 
        in_all = set(string_indices)
        for c1, c2 in groups_of_three: 
            in_all = in_all.intersection(c1 + c2)
        
        for c in in_all:
            total += string_indices.find(c) + 1 
    return total


def batched(iterable, n):
    "Batch data into lists of length n. The last batch may be shorter."
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while (batch := list(islice(it, n))):
        yield batch

if __name__ == "__main__":
    for path in sys.argv[1:]:
        puzzle_input = open(path + '.txt').readlines()

        data = parse(puzzle_input)

        solution1 = part1(data)
        print("%s puzzle 1 : %s" % (path, solution1))

        solution2 = part2(data)
        print("%s puzzle 2 : %s" % (path, solution2))

