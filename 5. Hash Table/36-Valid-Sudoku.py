# Problem Link = https://leetcode.com/problems/valid-sudoku/description
from collections import defaultdict
def sudokuSolver(board):
    rows = defaultdict(set)
    cols = defaultdict(set)
    squares = defaultdict(set)
    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3) * 3 + (c // 3)]):
                return False
            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            squares[(r // 3) * 3 + (c // 3)].add(board[r][c])
    return True

board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

print(sudokuSolver(board))
