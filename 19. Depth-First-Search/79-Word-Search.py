# Problem Link = https://leetcode.com/problems/word-search/description/

def wordSearch(board, word):
    def dfs(row, col, idx):
        if idx == len(word):
            return True
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or board[row][col] != word[idx]:
            return False
        
        temp = board[row][col]
        board[row][col] = '#'
        found = (dfs(row + 1, col, idx + 1) or dfs(row - 1, col, idx + 1) or dfs(row, col + 1, idx + 1) or dfs(row, col - 1, idx + 1))
        board[row][col] = temp
        return found
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(i, j, 0):
                return True
    return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(wordSearch(board, word))