board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]

# board = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
# ]


def solve(bo):  # function to solve a board that has been given too it
    find = find_empty(bo)
    if not find:
        return True  # base case of our recursive algorithm
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0
    print_board(bo)
    return False


def valid(
    bo, num, pos
):  # function to check if we can insert a given number into a given spot

    # check if the row is valid
    for i in range(len(bo[0])):
        if num == bo[pos[0]][i] and pos[1] != i:
            return False

    # now we check the column

    for i in range(len(bo)):
        if num == bo[i][pos[1]] and pos[0] != i:
            return False

    # now we want to check the box
    # first thing we do is find out the coordinates of the box we are in
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    # making it through all these checks means that the entry is valid
    return True


def print_board(bo):  # function to print a given board
    print("- - - - - - - - -")
    for i in range(len(board)):
        if (i) % 3 == 0 and i != 0 and i != 8:
            print("- - - - - - - - -")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print("|", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")
    print("- - - - - - - - -")
    print()


def find_empty(bo):  # function to find the first empty space on a given board
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col
    return None


print("Initial Board:")
print_board(board)
solve(board)
print("Final Board;")
print_board(board)
