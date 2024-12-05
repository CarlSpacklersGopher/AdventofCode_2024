
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
        
        # Verticals
        for col_num in range(len(raw[0])):
            tmp = ''
            for row_num in range(len(raw)):
                tmp += raw[row_num][col_num]
            vert_tb.append(tmp)
        vert_bt = [x[::-1] for x in vert_tb]


        # Diagonals
        for diag_slice_num in range(len(raw[0])): # Assume square
            # Top Right to Bottom Left
            l_trbl_slice = ''
            r_trbl_slice = ''
            l_trbl_slice_start = (0, len(raw[0]) - 1 - diag_slice_num)
            r_trbl_slice_start = (0 + diag_slice_num, len(raw[0]) - 1)

            # Top Left to Bottom Right 
            l_tlbr_slice = ''
            r_tlbr_slice = ''
            l_tlbr_slice_start = (0 + diag_slice_num, 0)
            r_tlbr_slice_start = (0, 0 + diag_slice_num)

            count = 0
            slice_complete = False
            while not slice_complete:
                if count > len(raw[0]): # max traversal distance is diagonal length
                    slice_complete = True

                # Top Right to Bottom Left
                if l_trbl_slice_start[1] - count >= 0:
                    l_trbl_slice += raw[l_trbl_slice_start[0] + count][l_trbl_slice_start[1] - count]
                if r_trbl_slice_start[0] + count < len(raw):
                    r_trbl_slice += raw[r_trbl_slice_start[0] + count][r_trbl_slice_start[1] - count]

                # Top Left to Bottom Right
                if l_tlbr_slice_start[0] + count < len(raw):
                    l_tlbr_slice += raw[l_tlbr_slice_start[0] + count][l_tlbr_slice_start[1] + count]
                if r_tlbr_slice_start[1] + count < len(raw[0]):
                    r_tlbr_slice += raw[r_tlbr_slice_start[0] + count][r_tlbr_slice_start[1] + count]
                count += 1

            diag_trbl.append(l_trbl_slice)
            diag_trbl.append(r_trbl_slice)

            diag_tlbr.append(l_tlbr_slice)
            diag_tlbr.append(r_tlbr_slice)

        diag_bltr = [x[::-1] for x in diag_trbl]
        diag_brtl = [x[::-1] for x in diag_tlbr]        

    return [forwards,
            backwards,
            vert_tb,
            vert_bt,
            diag_trbl,
            diag_bltr,
            diag_tlbr]

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
    
