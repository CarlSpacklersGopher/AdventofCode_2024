
def process_input(path: str) -> list[list[int]]:
    ''' Reads the puzzle input. '''
    with open(path) as f:
        lefts = []
        rights = []
        for line in f:
            left, right = line.split()
            lefts.append(int(left))
            rights.append(int(right))
        lefts.sort()
        rights.sort()
    return [lefts, rights]


def part_1(puzzle_input:list[list[int]]) -> int:
    ''' Solves for Part 1. '''
    lefts = puzzle_input[0]
    rights = puzzle_input[1]

    dist = 0
    for left, right in zip(lefts, rights):
        dist += abs(left - right)
    return dist

def part_2(puzzle_input:list[list[int]]) -> int:
    ''' Solves for Part 2. '''
    return 0

if __name__ == '__main__':
    # puzzle_input =  process_input('01/test_input.txt')
    puzzle_input = process_input('01/input.txt')
    print("Part 1: " + str(part_1(puzzle_input)))

    print("Part 2: " + str(part_2(puzzle_input)))
    
