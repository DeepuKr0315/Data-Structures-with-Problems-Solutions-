# Problem link - https://leetcode.com/problems/flood-fill/description/
# FLOOD-FILL

def dfs(image, sr, sc, color, rows, cols, source):
    if(sr < 0 or sr >= rows or sc < 0 or sc >= cols):
        return
    if(image[sr][sc] != source):
        return
    image[sr][sc] = color
    dfs(image, sr - 1, sc, color, rows, cols, source)
    dfs(image, sr + 1, sc, color, rows, cols, source)
    dfs(image, sr, sc - 1, color, rows, cols, source)
    dfs(image, sr, sc + 1, color, rows, cols, source)


def floodfill(image, sr, sc, color):
    if(image[sr][sc] == color):
        return image
    rows = len(image)
    cols = len(image[0])
    source = image[sr][sc]
    dfs(image, sr, sc, color, rows, cols, source)
    return image

print(floodfill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2))