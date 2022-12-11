import sys
from itertools import * 
import math

def parse(input): 
    monkeys = [] 
    monkey = None

    for line in input: 
        line = line.strip()
        if line.startswith("Monkey"): 
            monkey= Monkey() 
            monkeys.append(monkey)
        elif line.startswith("Starting"): 
            monkey.addItems(list(int(x) for x in line.split(':')[1].split(',')))
        elif line.startswith("Operation"): 
            monkey.operation = line.split('=')[1]
        elif line.split(":")[0] == "Test":
            monkey.test_divisor = int(line.split()[-1]) 
        elif line.split(":")[0] == "If true":
            monkey.when_true = int(line.split()[-1]) 
        elif line.split(":")[0] == "If false":
            monkey.when_false = int(line.split()[-1]) 

    return monkeys
    

class Monkey:
    def __init__(self) -> None:
        self.operation = None
        self.test_divisor = None
        self.when_true = None 
        self.when_false = None
        self.items = [] 
        self.inspections = 0 
    
    def addItems(self, items):
        for i in items: 
            self.items.insert(0, i)
    
    def processItem(self, relief_fn): 
        try: 
            item = self.items.pop()
            self.inspections += 1 
            return self.doit(item,relief_fn)
        except IndexError:
            return None
    
    def doit(self, item,relief_fn):
        old = item
        new = eval(self.operation)
        ##no damage process relief
        new = relief_fn(new)

        if new % self.test_divisor == 0: 
            return (self.when_true, new)
        return (self.when_false, new)
    
def flying_items(rounds,relief_fn): 
    for r in range(rounds):
        for m in data: 
            while True:
                res = m.processItem(relief_fn)
                if res == None: 
                    break

                data[res[0]].addItems([res[1]])
    inspections = [] 
    for m in data: 
        inspections.append(m.inspections)
    
    inspections.sort()
    return math.prod(inspections[-2:])

def part1(data):
    """Solve part 1"""
    return flying_items(20, lambda x : x // 3)

def part2(monkeys):
    """Solve part 1"""

    ### I looked at various answers
    ### the proble here is the numbers get to big so you have to figure 
    ### out how to keep the numbers small
    modulo = 1
    for m in monkeys:
        modulo *= m.test_divisor
    
    return flying_items(10000, lambda x: x % modulo)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        puzzle_input = open(path + '.txt').readlines()

        data = parse(puzzle_input)

        solution1 = part1(data)
        print("%s puzzle 1 : %s" % (path, solution1))

        data = parse(puzzle_input)
        solution2 = part2(data)
        print("%s puzzle 2 : %s" % (path, solution2))

