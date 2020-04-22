def valid(board, pos, num):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != 1:
            return False

    for i in range(len(board[0])):
        if board[i][pos[1]] == num and i != pos[0]:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num:
                return False

    return True


def solve(bo):
    find = findEmpty(bo) #tuple of empty position

    if not find:
        return True

    else:
        row, col = find

    for i in range(1, 10):
        if valid(board, find, i):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0
    return False

def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    return None


def printBoard(bo):
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


board = [
    [6, 2, 0, 5, 3, 0, 0, 0, 0],
    [5, 4, 0, 0, 9, 1, 0, 8, 0],
    [0, 0, 7, 0, 0, 0, 0, 0, 2],
    [0, 0, 1, 0, 0, 0, 0, 4, 3],
    [0, 8, 0, 0, 0, 0, 5, 0, 0],
    [4, 0, 0, 7, 6, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 9, 0, 0, 4],
    [0, 0, 0, 0, 2, 8, 0, 6, 0],
    [0, 0, 9, 0, 0, 3, 0, 7, 1]
]

printBoard(board)
solve(board)

print("solved")
printBoard(board)