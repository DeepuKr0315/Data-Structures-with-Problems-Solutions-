# Problem Link = https://leetcode.com/problems/surrounded-regions/description

def surroundedRegions(board):
    if not board:
        return
    rows = len(board)
    cols = len(board[0])
    def helper(row, col):
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or board[row][col] != "O":
            return
        board[row][col] = "S"
        helper(row + 1, col)
        helper(row - 1, col)
        helper(row, col + 1)
        helper(row, col - 1)
    for i in range(rows):
        helper(i, 0)
        helper(i, cols - 1)
    for j in range(cols):
        helper(0, j)
        helper(rows - 1, j)

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == "O":
                board[i][j] = "X"
            elif board[i][j] == "S":
                board[i][j] = "O"
    return board

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print(surroundedRegions(board))

board = [["X"]]
print(surroundedRegions(board))