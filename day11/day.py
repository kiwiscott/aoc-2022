import sys
from itertools import * 
import math

def example_data():
    monkey0 = Monkey(0,'old * 19', 23,2,3)
    monkey0.addItems([79,98])

    monkey1 =  Monkey(1,'old + 6', 19,2,0)
    monkey1.addItems([54,65,75,74])

    monkey2 =  Monkey(2,'old * old', 13,1,3)
    monkey2.addItems([79,60,97])

    monkey3 =  Monkey(3,'old + 3', 17,0,1)
    monkey3.addItems([74])

    monkeys = [ monkey0,
         monkey1,
         monkey2,
         monkey3,
    ]
    return monkeys
def real_data(): 
    monkey0 = Monkey(0,'old * 17', 2,2,6)
    monkey0.addItems([85,79,63,72])

    monkey1 = Monkey(1,'old * old', 7,0,2)
    monkey1.addItems([53,94,65,81,93,73,57,92])

    monkey2 = Monkey(2,'old + 7', 13,7,6)
    monkey2.addItems([62,63])

    monkey3 = Monkey(3,'old + 4', 5,4,5)
    monkey3.addItems([57,92,56])

    monkey4 = Monkey(4,'old + 5', 3,1,5)
    monkey4.addItems([67])

    monkey5 = Monkey(5,'old + 6', 19,1,0)
    monkey5.addItems([85, 56, 66, 72, 57, 99])

    monkey6 = Monkey(6,'old * 13', 11,3,7)
    monkey6.addItems([86, 65, 98, 97, 69])

    monkey7 = Monkey(7,'old + 2', 17,4,3)
    monkey7.addItems([87, 68, 92, 66, 91, 50, 68])

    monkeys = [ monkey0,
         monkey1,
         monkey2,
         monkey3,
         monkey4,
         monkey5,
         monkey6,
         monkey7,
    ]
    return monkeys




    
    return puzzle_input

class Monkey:
    def __init__(self, id, operation,test_divisor,when_true,when_false) -> None:
        self.id = id
        self.operation = operation
        self.test_divisor = test_divisor
        self.when_true = when_true 
        self.when_false = when_false
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
        if path == 'example':
            data = example_data()
        else:
            data = real_data()

        solution1 = part1(data)
        print("%s puzzle 1 : %s" % (path, solution1))

        if path == 'example':
            data = example_data()
        else:
            data = real_data()
    
        solution2 = part2(data)
        print("%s puzzle 2 : %s" % (path, solution2))

