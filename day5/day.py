import sys
from itertools import * 
import re 

def parse(puzzle_input):
    bin_reg = '[(A-Z)]'
    move_reg ='move\s(\d*)\sfrom\s(\d*)\sto\s(\d*)' 

    cargohold = [] 
    moves = [] 

    ##Process Bins
    bin_fixed_width = 4 
    number_of_bins = int(len(puzzle_input[0]) / bin_fixed_width)
    for i in range(0, number_of_bins):
        cargohold.append([])
    
    for line in puzzle_input: 
        move_match = re.match(move_reg,line)
        if move_match:
            ##move 3 from 1 to 3
            qty = int(move_match[1])
            fromb = int(move_match[2]) - 1 ##zerobased
            tob = int(move_match[3]) - 1 ##zerobased
            moves.append((qty,fromb,tob))
        elif re.search(bin_reg,line):
            bin_matches = re.finditer( bin_reg, line)
            for m in bin_matches: 
                bin = int(m.start() / bin_fixed_width )
                ##print(m.start(), m.end(), m.group(0), bin )
                cargohold[bin].insert(0, m.group())
    return (cargohold,moves)


def part1(data):
    """Solve part 1"""
    cargohold,moves = data

    #move 1 deom 1 to 0
    for (qty,fromb, tob) in moves: 
        ##print(qty)
        for i in range(qty):
            p = cargohold[fromb].pop()
            cargohold[tob].append(p)
    #answer
    tops = ''
    for b in cargohold:
        tops += b[-1]

    return tops


def part2(data):
    cargohold,moves = data    
    holder = [] 

    #move 1 deom 1 to 0
    for (qty,fromb, tob) in moves: 
        holder.clear() 
        for i in range(qty):
            p = cargohold[fromb].pop()
            holder.append(p)
        while len(holder) > 0: 
            cargohold[tob].append(holder.pop())

    #answer
    tops = ''
    for b in cargohold:
        try: 
            tops += b[-1]
        except:
            pass

    return tops

if __name__ == "__main__":
    for path in sys.argv[1:]:
        puzzle_input = open(path + '.txt').readlines()

        data = parse(puzzle_input)

        solution1 = part1(data)
        print("%s puzzle 1 : %s" % (path, solution1))

        data = parse(puzzle_input)
        solution2 = part2(data)
        print("%s puzzle 2 : %s" % (path, solution2))

