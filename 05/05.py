
import sys

order_rules = {}

def process_input(path: str) -> tuple:
    ''' Reads the puzzle input. '''
    with open(path) as f:
        order_rules = {}
        page_sequences = []

        mass_text = f.read()
        order_text, sequence_text = mass_text.split('\n\n')
        for order in order_text.split():
            first, second = order.strip().split('|')
            first = int(first)
            second = int(second)

            requirements = order_rules.get(second, [])
            requirements.append(first)
            order_rules[second] = requirements


        for sequence in sequence_text.split():
            page_sequences.append([int(x) for x in sequence.split(',')])

        return (order_rules, page_sequences) 

def part_1(order_rules: dict, page_sequences:list[list[int]]) -> int:
    ''' Solves for Part 1. '''
    return 0

def part_2(order_rules: dict, page_sequences:list[list[int]]) -> int:
    ''' Solves for Part 2. '''
    return 0

if __name__ == '__main__':
    order_rules, page_sequences = process_input(sys.argv[1])
    print("Part 1: " + str(part_1(order_rules, page_sequences)))

    print("Part 2: " + str(part_2(order_rules, page_sequences)))
    
