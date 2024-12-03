import re

def process_input(path: str) -> str: 
    ''' Reads the puzzle input. '''
    with open(path) as f:
        return f.read()

def part_1(puzzle_input:str) -> int:
    ''' Solves for Part 1. '''

    matches = re.findall(r'mul\((\d+),(\d+)\)', puzzle_input)
    products = []
    for match in matches:
        products.append(int(match[0]) * int(match[1]))

    return sum(products)
    

def part_2(puzzle_input:list[str]) -> int:
    ''' Solves for Part 2. '''
    return 0

if __name__ == '__main__':
    # puzzle_input = process_input('03/test_input.txt')
    puzzle_input = process_input('03/input.txt')
    print("Part 1: " + str(part_1(puzzle_input)))

    print("Part 2: " + str(part_2(puzzle_input)))
    
