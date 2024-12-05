
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
            l_trbl_slice = ''
            r_trbl_slice = ''
            l_trbl_slice_start = (0, len(raw[0]) - 1 - diag_slice_num)
            r_trbl_slice_start = (0 + diag_slice_num, len(raw[0]) - 1)

            count = 0
            slice_complete = False
            while not slice_complete:
                if count > len(raw[0]): # max traversal distance is diagonal length
                    print('TR -> BL (L): ' + l_trbl_slice)
                    print('TR -> BL (R): ' + r_trbl_slice)
                    slice_complete = True
                if l_trbl_slice_start[1] - count >= 0:
                    l_trbl_slice += raw[l_trbl_slice_start[0] + count][l_trbl_slice_start[1] - count]
                if r_trbl_slice_start[0] + count < len(raw):
                    r_trbl_slice += raw[r_trbl_slice_start[0] + count][r_trbl_slice_start[1] - count]
                count += 1

        '''
        for col_num in range(len(raw[0])):
            tmp_trbl = '' 
            tmp_tlbr = ''

            count = 0
            while True:
                if count > len(raw[0]):
                    break
                if col_num - count >= 0:
                    tmp_trbl += raw[count][col_num - count]
                if col_num + count < len(raw[0]):
                    tmp_tlbr += raw[count][col_num + count]
                count += 1
            
            print(f'TR -> BL: {tmp_trbl}')
            print(f'TL -> BR: {tmp_tlbr}')
            diag_trbl.append(tmp_trbl)
            diag_tlbr.append(tmp_tlbr)
        '''




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
    
