
## Method 1
# Problem = https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/

def findTheWinner(n, k):

    arr = []
    for i in range(1, n+1):
        arr.append(i)

    def helper(arr, startIndex):
        
        if len(arr)==1:
            return arr[0]
        
        removeIndex = (startIndex + k - 1) % len(arr)
        del arr[removeIndex]
        return helper(arr, removeIndex)
    
    return helper(arr, 0)

print("",findTheWinner(5, 2))