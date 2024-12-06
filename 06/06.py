
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

def turn_right(direction: tuple) -> tuple:
    directions = [(0, -1), # North
                  (1, 0),  # East
                  (0, 1),  # South
                  (-1, 0)  # West
                  ]
    next_dir = (directions.index(direction) + 1) % len(directions)
    return directions[next_dir]


def part_1(grid: list, guard: tuple) -> int:
    ''' Solves for Part 1. '''
    dx, dy = (0, -1) # North

    visited = set()
    while True:
        visited.add(guard)

        next_x, next_y = (guard[0] + dx, guard[1] + dy)
        in_bounds = (0 <= next_x < len(grid[0])) and (0 <= next_y < len(grid))
        if not in_bounds:
            break
        if grid[next_y][next_x] == '#':
            dx, dy = turn_right((dx, dy))

        guard = (guard[0] + dx, guard[1] + dy)


    return len(visited)

def part_2(grid: list, guard: tuple) -> int:
    ''' Solves for Part 2. '''
    return 0

if __name__ == '__main__':
    guard, grid = process_input(sys.argv[1])
    print("Part 1: " + str(part_1(grid, guard)))

    print("Part 2: " + str(part_2(grid, guard)))

