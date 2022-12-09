import sys
import math
from itertools import * 
        
def parse(puzzle_input):
    pines = []
    for p in puzzle_input:
        (d,s) = p.split()
        pines.append((d, int(s)) )
    return pines


def move_head(direction,head):
    head[0] += 1 if direction == 'U' else -1 if  direction == 'D' else 0 
    head[1] += 1 if direction == 'R' else -1 if  direction == 'L' else 0 

def move_tail(k1,k2): 
    ##if the row and the colum is different but the gap for both is one do nothing 
    row_delta = k1[0] - k2[0]
    col_delta = k1[1] - k2[1]
    if abs(row_delta) > 1 or abs(col_delta) > 1:
        #we only move 1 step
        k2[0] += -1 if row_delta < 0 else 1 if row_delta > 0 else 0 
        k2[1] += -1 if col_delta < 0 else 1 if col_delta > 0 else 0 
        

def rope_mover(rope_len,movements):
    rope = [[0, 0] for n in range(rope_len)] 
    tail_locations = set() 

    for (direction,step) in movements:
        while step != 0: 
            for e,r in enumerate(rope):
                if e == 0: 
                    move_head(direction,rope[0])
                else:
                    move_tail(rope[e-1], rope[e])
                
            tail_locations.add(tuple(rope[-1]))
            step = step -1
    return len(tail_locations)        

def part1(movements):
    return rope_mover(2,movements) 
    
def part2(movements):
    return rope_mover(10,movements) 
    

if __name__ == "__main__":
    for path in sys.argv[1:]:
        puzzle_input = open(path + '.txt').readlines()

        data = parse(puzzle_input)

        solution1 = part1(data)
        print("%s puzzle 1 : %s" % (path, solution1))

        data = parse(puzzle_input)
        solution2 = part2(data)
        print("%s puzzle 2 : %s" % (path, solution2))

