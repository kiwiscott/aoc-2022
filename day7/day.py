#! python3

import sys
from itertools import * 

class Directory:
    def __init__(self,parent, name):
        self.parent = parent
        self.name = name
        self.files = []
        self.childDirs = [] 
    
    def addFile(self, filename, size):
        self.files.append((filename,size))

    def addChildDir(self, name):
        self.childDirs.append(Directory(self, name))

    def printTree(self, offset):
        print("%s - %s (dir)" % (offset * " ", self.name))

        for cd in self.childDirs:
            cd.printTree(offset+1)

        for f in self.files:
            print("%s - %s (file, size=%s)" % ((offset  + 2)* ' ',f[0], f[1]))
    
    def recursive_size(self):
        size= 0 
        for f in self.files:
            size += f[1]

        for ch in self.childDirs: 
            size += ch.recursive_size()
        
        return size

    def recursive_dir_size(self):
        holda = [(self.name, self.recursive_size())]

        for ch in self.childDirs: 
            children = ch.recursive_dir_size()
            for c in children:
                holda.append(c)
        
        return holda


    def moveDir(self, path):
        if path == ".." and self.parent is not None:
            return self.parent
        
        for d in self.childDirs:
            if d.name == path:
                    return d
        
        return self
        
def parse(puzzle_input):
    pines = []
    for p in puzzle_input:
        pines.append(p.strip())
    return pines

           
def build_tree(data):
    ##Create Root 
    root = Directory(None, "/")
    cwd = root

    for d in data: 
        if d.startswith("$"):
            ##command 
            command = d.split(' ')[1]
            if command == "cd":
                path = d.split(' ')[2].strip()
                if path == "/":
                    cwd = root
                else:
                    cwd = cwd.moveDir(path)
        elif d.startswith("dir"):
            ##add directory
            cwd.addChildDir(d.split(' ')[1].strip())
        elif len(d.strip()) > 0:
            ##add file 
            file = d.split(' ')[1].strip()
            size = int(d.split(' ')[0].strip())
            cwd.addFile(file,size)
    return root 
            

def part1(data):
    root = build_tree(data)
    ##root.printTree(0)

    ##print(root.recursive_size())

    all_under_100000 = 0 
    for d in root.recursive_dir_size():
        if(d[1] < 100000):
            all_under_100000 += d[1]
    return all_under_100000

def part2(data):
    """Solve part 2"""
    total_space_available = 70000000
    required_space = 30000000

    #44376732
    root = build_tree(data)
    current_allocated_space = root.recursive_size()
    too_free_up = current_allocated_space - (total_space_available - required_space)

    possible_options = [] 

    for d in root.recursive_dir_size():
        if(d[1] >= too_free_up):
            possible_options.append(d[1])

    return sorted(possible_options)[0]
    

if __name__ == "__main__":
    for path in sys.argv[1:]:
        puzzle_input = open(path + '.txt').readlines()

        data = parse(puzzle_input)

        solution1 = part1(data)
        print("%s puzzle 1 : %s" % (path, solution1))

        data = parse(puzzle_input)
        solution2 = part2(data)
        print("%s puzzle 2 : %s" % (path, solution2))

