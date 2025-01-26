
# Problem Name = 2379. Minimum Recolors to Get K Consecutive Black Blocks
# problem Link = https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description/

def minRecolor(blocks, k):
    currentRecolor = 0
    for i in range(k):
        if blocks[i] == "W":
            currentRecolor += 1
    minRecolor = currentRecolor
    for i in range(k, len(blocks)):
        # decrease the value of currentRecolor when a 'W' block is leaving the window
        if blocks[i - k] == 'W':
            currentRecolor -= 1
        # increment the value of currentRecolor when a 'W' block is entering the window
        if blocks[i] == 'W':
            currentRecolor += 1
        minRecolor = min(minRecolor, currentRecolor)
    return minRecolor

    # countOfWhite = len(blocks)
    # for i in range(len(blocks) - k + 1):
    #     countOfWhite = min(countOfWhite, blocks[i + k].count("W"))
    # return countOfWhite

print(minRecolor(blocks = "WBBWWBBWBW", k = 7))