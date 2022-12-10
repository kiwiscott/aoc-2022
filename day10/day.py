import sys
from itertools import * 

def parse(puzzle_input):
    return puzzle_input

def preprocess_instructions(data):
    instructions = [] 
    for ins in data: 
        ins = ins.strip()
        if ins == "noop":
            instructions.append(ins)
        elif ins.startswith("addx"):
            instructions.append(ins.split()[0])
            instructions.append(ins.split()[1])
    return instructions

def run_all(instructions,during = None):
    xval = 1 
    for i,ival in enumerate(instructions):
        if during:
            during(i, xval)
        
        try:
            xval += int(ival) ### The sign was being dropped with is numeric so this is just as good for python
        except ValueError:
            None

    return xval

def part1(data):
    """Solve part 1"""
    cycles = [20, 60, 100, 140, 180, 220]
    instructions = preprocess_instructions(data)
    signal_strength = 0 

    #changed to callback after part 2 as it was just as easy
    #and its more consistent 
    def calc_strength(cycle,xval):
        nonlocal signal_strength 
        adj_cycle  = cycle +1
        if adj_cycle in cycles:
            signal_strength += adj_cycle * xval

    run_all(instructions,calc_strength)

    return signal_strength

def part2(data):
    """Solve part 2"""
    instructions = preprocess_instructions(data)

    def print_crt(cycle,xval):
        col = cycle % 40
        if (xval -1)  <= col <= (xval + 1):
            print('#',end='')
        else:
            print(' ',end='')
        
        if (cycle+1) % 40 == 0:
            print('')

    run_all(instructions,print_crt)
    print('\n')



if __name__ == "__main__":
    for path in sys.argv[1:]:
        puzzle_input = open(path + '.txt').readlines()

        data = parse(puzzle_input)

        solution1 = part1(data)
        print("%s puzzle 1 : %s" % (path, solution1))

        data = parse(puzzle_input)
        solution2 = part2(data)
        print("%s puzzle 2 : %s" % (path, solution2))

