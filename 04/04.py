
import sys

def process_input(path: str) -> list[str]:
    ''' Reads the puzzle input. '''
    forwards = []
    backwards = []
    vert_tb = []
    vert_bt = []
    diag_trbl = []
    diag_bltr = []
    diag_tlbr = []
    diag_brtl = []

    with open(path) as f:
        raw = [line.strip() for line in f.readlines()]
        forwards = [x for x in raw]
        backwards = [x[::-1] for x in raw]
        vert_tb = []
        for col_num in range(len(raw[0])):
            tmp = ''
            for row_num in range(len(raw)):
                tmp += raw[row_num][col_num]
            vert_tb.append(tmp)
        vert_bt = [x[::-1] for x in vert_tb]

        print(f'forward: {forwards}')
        print(f'backward: {backwards}')
        print(f'vert_tb: {vert_tb}')
        print(f'vert_bt: {vert_bt}')

    return None

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
    
