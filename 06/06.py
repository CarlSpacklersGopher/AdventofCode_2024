
import sys

def process_input(path: str) -> tuple[tuple[int, int], list[list[str]]]:
    ''' Reads the puzzle input. '''
    guard = (-1, -1)
    with open(path) as f:
        content = f.read()
        lines = content.split()

        cols = len(lines[0]) + 1 # +1 to account for \n
        g = content.find('^')
        guard = (g % cols, g // cols)

        grid = [list(l) for l in lines]

        return (guard, grid)

def part_1(puzzle_input:list[str]) -> int:
    ''' Solves for Part 1. '''
    return 0

def part_2(puzzle_input:list[str]) -> int:
    ''' Solves for Part 2. '''
    return 0

if __name__ == '__main__':
    puzzle_input = process_input(sys.argv[1])
    print("Part 1: " + str(part_1(puzzle_input)))

    print("Part 2: " + str(part_2(puzzle_input)))

