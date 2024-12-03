

def process_input(path: str) -> list[list[int]]:
    ''' Reads the puzzle input. '''
    with open(path) as f:
        levels = []
        for line in f:
            lst = [int(x) for x in line.split()]
            levels.append(lst)
    return levels

def part_1(puzzle_input:list[list[str]]) -> int:
    ''' Solves for Part 1. '''
    safe_count = 0
    for levels in puzzle_input:
        unsafe_flag = False
        if sorted(levels) == levels or sorted(levels, reverse=True) == levels:
            for idx in range(1, len(levels)):
                delta = abs(levels[idx - 1] - levels[idx])
                if delta < 1 or delta > 3:
                    unsafe_flag = True
            if not unsafe_flag:
                safe_count += 1
        # print(f'{levels}, Safe: {safe_count}')
        
    return safe_count

def part_2(puzzle_input:list[list[str]]) -> int:
    ''' Solves for Part 2. '''
    return 0

if __name__ == '__main__':
    # puzzle_input = process_input('02/test_input.txt')
    puzzle_input = process_input('02/input.txt')
    print("Part 1: " + str(part_1(puzzle_input)))

    print("Part 2: " + str(part_2(puzzle_input)))
    
