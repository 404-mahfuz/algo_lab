#print('\n'+'enter the sudoku numbers ( that must be between 0-9 ) sequentially for all row and column '+'\n')

#board = []
#for i in range(9):
#    row = []
#    for j in range(9):
#        num = int(input(f"Enter value for row {i+1}, column {j+1}: "))
#        row.append(num)
#    board.append(row)

board = [
    [0,6,8,0,1,0,3,7,9],
    [2,0,0,0,0,0,1,5,0],
    [5,0,0,0,0,8,0,0,4],
    [0,4,6,5,2,9,7,8,3],
    [3,0,0,4,8,7,0,0,0],
    [7,0,0,0,6,3,5,0,0],
    [9,0,4,0,5,2,0,1,0],
    [8,0,2,9,7,6,0,3,5],
    [0,5,3,0,4,0,0,0,0]
]


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if if_possible(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def if_possible(bo, num, pos):
    # Checking row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Checking column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Checking box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

print("\n"+'here is the unsolved sudoku '+'\n')

print_board(board)
solve(board)
print('\n'+"starting to solve......"+'\n')
print("_____________ solved ________________"+'\n')
print_board(board)


