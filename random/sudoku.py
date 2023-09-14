# Check if the sudoku is valid or not
from typing import List
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


def getEmptyCount(row):
    count = 0
    for i in row:
        if i == 0:
            count += 1
    return count


def isRowValid(rowNumber):
    row = board[rowNumber]
    return len(set(row)) == 10 - getEmptyCount(row)


def isColumnValid(colNumber):
    column = []
    for x in board:
        column.append(x[colNumber])
    return len(set(column)) == 10 - getEmptyCount(column)


def isCellValid(cell):
    return len(set(cell)) == 10 - getEmptyCount(cell)


def get_3x3_block(row, col):
    block = []
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            block.append(board[i][j])
    return block


for i in range(0, len(board)):
    # print(f"isRowValid:{i} - ", isRowValid(i))
    if not isRowValid(i):
        print("row invalid", i)

for i in range(0, len(board)):
    if not isColumnValid(i):
        print("column invalid", i)


for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        # print(f"get_3x3_block({i},{j}) - ", get_3x3_block(i, j))
        if not isCellValid(get_3x3_block(i, j)):  # Check 3x3 blocks
            print("cell invalid", i, j)
