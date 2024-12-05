
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
    good_seq = [] 
    isgood = True
    for seq in page_sequences:
        for idx, page in enumerate(seq):
            requirements = set(order_rules.get(page, []))
            if requirements:
                following_pages = set(seq[idx:])
                if following_pages.intersection(requirements):
                    isgood = False
                    break
        if isgood:
            good_seq.append(seq)
        isgood = True

    
    middle_pages = []
    for seq in good_seq:
        middle_pages.append(seq[(len(seq) // 2)])


    return sum(middle_pages)

def part_2(order_rules: dict, page_sequences:list[list[int]]) -> int:
    ''' Solves for Part 2. '''
    return 0

if __name__ == '__main__':
    order_rules, page_sequences = process_input(sys.argv[1])
    print("Part 1: " + str(part_1(order_rules, page_sequences)))

    print("Part 2: " + str(part_2(order_rules, page_sequences)))
    
