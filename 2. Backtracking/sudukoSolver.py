def solveSudoku(board):
    # No need to create new list or array because we will change the values inplace    
    def isValid(num, row, col):
        for x in range(9):
            for x in range(9):
                if board[x][col] == num:
                    return False
                if board[row][x] == num:
                    return False
                #box check
                r = 3 * (row//3) + x//3
                c = 3 * (col//3) + x%3
                if board[r][c] == num:
                    return False
        return True

    def fillTheBoard(board):
        # identify empty cell
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    for num in "123456789":
                        if isValid(num, row, col):
                            board[row][col] = num
                            if (fillTheBoard(board)): return True
                            board[row][col] = "." #backtracking
                    return False # when we come out of an approach, then we will go to 25th statement
        return True # when the board is already filled this return statement will be in use
    fillTheBoard(board)