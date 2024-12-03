

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

    # Ways something could be wrong, but still safe:
    # 1. single duplicate added - set?
    # 2. single item out of order - asc sort
    # 3. single item out of order - desc sort
    # 4. single item causes delta greater than threshold when compared to max or min of levels
    # 5. single item causes delta less than threshold when compared to max or min of levels - DUPLICATE WITH ITEM 1
    
    maybe_safes = []
    for levels in puzzle_input:
        uniq = set(levels)
        if len(levels) - len(uniq) == 1:
            # if there's a single duplicate, no more removals are allowed
            maybe_safes.append(list(uniq))
        elif len(levels) == len(uniq):
            diffs_frontsort = []
            diffs_backsort = []
            for orig, f, b in zip(levels, sorted(levels), sorted(levels, reverse=True)):
                if orig != f:
                    diffs_frontsort.append(orig)
                if orig != b:
                    diffs_backsort.append(orig)
            if len(diffs_frontsort) >= 2:
                # at least one item changed places
                maybe_safes.append(levels.remove(diffs_frontsort[0])) # just remove first item that changed places and check
            elif len(diffs_backsort >= 2):
                maybe_safes.append(levels.remove(diffs_backsort[0])) # just remove first item that changed places and check

            # TODO:gotta find a way to do the difference greater than 3 difference math and remove stuff without brute forcing?

    safe_count = 0
    for maybe_safe in maybe_safes:
        safe_count += part_1([maybe_safe]) 

    return safe_count

if __name__ == '__main__':
    puzzle_input = process_input('02/test_input.txt')
    # puzzle_input = process_input('02/input.txt')
    print("Part 1: " + str(part_1(puzzle_input)))

    print("Part 2: " + str(part_2(puzzle_input)))
    
