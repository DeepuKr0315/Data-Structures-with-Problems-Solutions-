# problem link = https://leetcode.com/problems/two-city-scheduling/description/

def twoCitySchedule(costs):
    costs.sort(key = lambda x : x[0] - x[1])
    n = len(costs)//2
    dp = [[float('inf')] * (n + 1) for _ in range(2 * n + 1)]
    dp[0][0] = 0
    for i in range(1, 2*n + 1):
        for j in range(max(0, i - n), min(n, i) + 1):
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j-1] + costs[i-1][0])
            if j < i:
                dp[i][j] = min(dp[i][j], dp[i-1][j] + costs[i-1][1])
    return dp[2*n][n]

costs = [[10,20],[30,200],[400,50],[30,20]]
print(twoCitySchedule(costs))

"""
 We initialize a DP table where dp[i][j] represents the minimum cost of sending the first i people
 with j going to city A. ( In the recursive and memoization approach - each funch call returned this.
 i and j are like the input parameters for the recursive / memoization approach) 

Time Complexity: 

Filling the DP Table:

Outer Loop: The outer loop iterates from 1 to 2n, considering each person one by one, resulting in 2n iterations.

Inner Loop: The inner loop ranges from max(0, i - n) to min(n, i). This range ensures that only feasible scenarios
 are considered (where you don't send more people to a city than there are available positions).
 The maximum range of this inner loop is bound by n (it does not exceed the number of slots in either city),
 leading to a maximum of n + 1 iterations for each value of i.

Given that each cell computation involves a constant amount of work (a couple of additions and minimum comparisons),
the time complexity for filling the table is also O(n^2).

Space Complexity:

DP Table: The dynamic programming table dp is a two-dimensional array where the dimensions are determined by:

The total number of people (2n), which sets the number of rows in the table.

The number of people that can possibly be sent to city A (ranging from 0 to n), which sets the number of 
columns in the table to n + 1.

The size of the dp table is therefore (2n + 1) x (n + 1), accounting for all combinations from 0 to 2n people 
considered and 0 to n people sent to city A.

Thus, the space complexity of the tabulation approach is O(n^2). This is because the table stores results for 
each combination of people considered and the number of people sent to city A.
"""
