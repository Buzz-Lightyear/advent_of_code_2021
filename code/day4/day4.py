NUMBERS = [50,68,2,1,69,32,87,10,31,21,78,23,62,98,16,99,65,35,27,96,66,26,74,72,45,52,81,60,38,57,54,19,18,77,71,29,51,41,22,6,58,5,42,92,85,64,94,12,83,11,17,14,37,36,59,33,0,93,34,70,97,7,76,20,3,88,43,47,8,79,80,63,9,25,56,75,15,4,82,67,39,30,89,86,46,90,48,73,91,55,95,28,49,61,44,84,40,53,13,24]

def print_board(board):
    print("\n")
    for row in board:
        print(' '.join([str(x) for x in row]))
    print("\n")

def part1():
    board_list = []
    with open("boards.txt", "r") as f:
        boards = [x.rstrip() for x in f.readlines()]
        current_board = []
        for line in boards:
            if line != '':
                current_board.append([int(line[0:2]), int(line[3:5]), int(line[6:8]), int(line[9:11]), int(line[12:14])])
            else:
                board_list.append(current_board)
                current_board = []
        print_board(current_board)
        board_list.append(current_board)
    
    board_dicts = []
    for board in board_list:
        curr_dict = {}
        for i, row in enumerate(board):
            for j, value in enumerate(row):
                curr_dict[value] = (i, j)
        board_dicts.append(curr_dict)
    
    # print(board_dicts[-1])

if __name__ == '__main__':
    part1()