
# Problem = https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/

def findTheWinner(n, k):
    def josephusProblem(n):
        if n==1:
            return 0
        return (josephusProblem(n-1)+k)%n 
    return josephusProblem(n)+1
print(findTheWinner(5,2))