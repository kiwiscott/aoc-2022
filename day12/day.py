import sys
from itertools import * 
from collections import deque
import string

def parse(input): 
    data =  [i.strip() for i in input]

    start_char = 'S'
    end_char = 'E'

    start = (0,0)
    end = (0,0)
    for ridx in range(len(data)):
        for cidx in range(len(data[0])): 
            if data[ridx][cidx] == start_char:
                start = (ridx,cidx)                
            elif data[ridx][cidx] == end_char:
                end = (ridx,cidx)

    data[start[0]] = data[start[0]].replace('S','a')
    data[end[0]] = data[end[0]].replace('E','z')

    return (start,end,data)



class Grid:
    def __init__(self,grid) -> None:
        self.grid = grid 
        self.allowed_neighbours = [(+1,0), (-1,0), (0,+1),(0,-1)] 
        self.cost_so_far = dict()
    
    def data_at(self, row,col): 
        if row >= 0 and col >= 0: 
            try: 
                return self.grid[row][col]
            except IndexError:
                return None
        else:
            return None
        

    def neighbors(self, row,col):
        current = self.data_at(row,col)

        for row_change, col_change in self.allowed_neighbours:
            r = row + row_change
            c = col + col_change
            value_at = self.data_at(r,c)
            if value_at and ord(value_at) <= ord(current) +1: 
                yield (r,c)
    
    def search(self,start,goal, reset=False):
        if reset:
            self.cost_so_far = dict() 

        frontier = deque()
        frontier.append(start)
        ##came_from =  dict()
        ##cost_so_far =  dict()
        ##came_from[start] = None
        self.cost_so_far[start] = 0
        
        while True:
            try: 
                current = frontier.pop()
            except IndexError:
                break 

            if current == goal: 
                continue

            for next in self.neighbors(current[0], current[1]): 
                new_cost = self.cost_so_far[current] + 1
                if next not in self.cost_so_far or  new_cost < self.cost_so_far[next]: 
                    self.cost_so_far[next] = new_cost
                    frontier.append(next)
                    ##came_from[next] = current
        
        if goal in self.cost_so_far:
            return self.cost_so_far[goal]
        else:
            return None


def data_at(coord,data):
    return data[coord[0]][coord[1]]

def part1(processed):
    (start,end,data) = processed
    grid = Grid(data)
    cost_so_far = grid.search(start,end,reset=True)    
    return cost_so_far

def part2(processed):
    """Solve part 1"""
    (start,end,data) = processed
    grid = Grid(data)

    ##sort the a's by the manhattan distance. In thoery we should try the closer ones to the end first 
    all_as = []
    for ridx in range(len(data)):
        for cidx in range(len(data[0])): 
            if data[ridx][cidx] == 'a':
                all_as.append((ridx,cidx))

    ##we can use the already traversed map to see if there's a better way of getting there. 
    ##There may be times when this docuesn't work but the brute force method (clearing out the mins steps to get to x takes 1000 times longer)

    current_min = sys.maxsize
    for row,col in all_as:
        new_start = (row,col)
        cost_so_far = grid.search( new_start ,end)
        if cost_so_far and cost_so_far < current_min:
            current_min = cost_so_far
    return current_min


if __name__ == "__main__":
    for path in sys.argv[1:]:
        puzzle_input = open(path + '.txt').readlines()

        data = parse(puzzle_input)

        solution1 = part1(data)
        print("%s puzzle 1 : %s" % (path, solution1))

        data = parse(puzzle_input)
        solution2 = part2(data)
        print("%s puzzle 2 : %s" % (path, solution2))

