import sys
from itertools import * 
        
def parse(puzzle_input):
    pines = []
    for p in puzzle_input:
        pines.append(p.strip())
    return pines

def checkNorth(v, x,y,data):
    steps = 0
    ci = x-1 

    while ci >= 0:
        steps +=1
        try:
            if v <= int(data[ci][y]):
                return (False, steps) 
        except:
            steps-+1 
            break
        ci = ci-1
    return (True, steps)

def checkSouth(v, x,y,data):
    steps = 0
    ci = x+1 
    while ci >= 0:
        steps +=1
        try: 
            if v <= int(data[ci][y]):
                return (False, steps) 
        except IndexError:
            steps-=1; 
            break            
        ci = ci+1
        
    return (True, steps)

def checkEast(v, x,y,data):
    steps = 0
    ci = y-1 
    while ci >= 0:
        steps +=1
        try: 
            if v <= int(data[x][ci]):
                return (False, steps) 
        except IndexError:
            steps-=1; 
            break            
        ci = ci-1
        
    return (True, steps)

def checkWest(v, x,y,data):
    steps = 0
    ci = y+1 
    while ci >= 0:
        steps +=1
        try: 
            if v <= int(data[x][ci]):
                return (False, steps)
        except IndexError:
            steps-=1; 
            break        
        ci = ci+1
    return (True, steps)


def part1(data):
    count =0 
    result = [] 
    for x in range(0,len(data)):

        for y in range(0,len(data[x])):
            v = int(data[x][y]) 
            if checkNorth(v,x,y,data)[0] or checkSouth(v,x,y,data)[0] or checkEast(v,x,y,data)[0] or checkWest(v,x,y,data)[0]:
                count+=1

    return count

def part2(data):
    count =0 
    result = [] 
    for x in range(0,len(data)):
        for y in range(0,len(data[x])):
            v = int(data[x][y]) 
            n = checkNorth(v,x,y,data)[1] 
            s = checkSouth(v,x,y,data)[1] 
            e = checkEast(v,x,y,data)[1] 
            w = checkWest(v,x,y,data)[1] 
            dis = n*s*e*w
            result.append(dis)
    
    return max(result)
    

if __name__ == "__main__":
    for path in sys.argv[1:]:
        puzzle_input = open(path + '.txt').readlines()

        data = parse(puzzle_input)

        solution1 = part1(data)
        print("%s puzzle 1 : %s" % (path, solution1))

        data = parse(puzzle_input)
        solution2 = part2(data)
        print("%s puzzle 2 : %s" % (path, solution2))

