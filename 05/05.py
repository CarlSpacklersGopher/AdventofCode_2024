
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


def is_ordered(order_rules: dict, sequence: list[int]) -> bool:
    isordered = True
    for idx, page in enumerate(sequence):
        requirements = set(order_rules.get(page, []))
        if requirements:
            following_pages = set(sequence[idx:])
            if following_pages.intersection(requirements):
                isordered = False
                break
    return isordered

def part_1(order_rules: dict, page_sequences:list[list[int]]) -> int:
    ''' Solves for Part 1. '''
    good_seq = [] 
    for seq in page_sequences:
        if is_ordered(order_rules, seq):
            good_seq.append(seq)

    middle_pages = []
    for seq in good_seq:
        middle_pages.append(seq[(len(seq) // 2)])

    return sum(middle_pages)


def part_2(order_rules: dict, page_sequences:list[list[int]]) -> int:
    ''' Solves for Part 2. '''
    not_ordered = []
    for seq in page_sequences:
        if not is_ordered(order_rules, seq):
            not_ordered.append(seq)

    for seq in not_ordered:
        for idx, page in enumerate(seq):            
            swap_made = True
            while True:
                if swap_made:
                    page = seq[idx] # something new moved into this idx, so stay here and repeat sort.
                else:
                    break
                requirements = order_rules.get(page, [])
                if requirements:
                    following_pages = seq[idx:]
                    for req in requirements:
                        if req not in following_pages:
                            swap_made = False
                        else:
                            req_idx = seq.index(req, idx)
                            seq.insert(req_idx, seq.pop(idx)) # insert current idx 1 place after found requirement
                            swap_made = True
                            break
                else:
                    swap_made = False

    middle_pages = []
    for seq in not_ordered:
        middle_pages.append(seq[(len(seq) // 2)])
    
    return sum(middle_pages)



if __name__ == '__main__':
    order_rules, page_sequences = process_input(sys.argv[1])
    print("Part 1: " + str(part_1(order_rules, page_sequences)))

    print("Part 2: " + str(part_2(order_rules, page_sequences)))
    
