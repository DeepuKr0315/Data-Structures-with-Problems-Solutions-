# problem link = https://leetcode.com/problems/two-city-scheduling/description/

def twoCitySchedule(costs):
    memo = {}
    def minCost(i, a_count):
        if len(costs) == i:
            # Base case: if we've considered all people, we wil have sent exactly n to A. 
            #so we can just return 0. There is no need to again check whether n people are sent to city A
            return 0
        if (i, a_count) in memo:
            return memo[(i, a_count)]
        if a_count < len(costs)//2:
            # Cost of sending the i-th person to A
            costA = costs[i][0] + minCost(i + 1, a_count+1)
        else:
            costA = float('inf')
        b_count = i - a_count
        if b_count < len(costs)//2:
            # Cost of sending the i-th person to B
            costB = costs[i][1] + minCost(i + 1, a_count)
        else:
            costB = float("inf")
        # Store the result in memo dictionary and return the minimum cost
        memo[(i, a_count)] = min(costA, costB)
        return memo[(i, a_count)]
    return minCost(0, 0)

costs = [[10,20],[30,200],[400,50],[30,20]]
print(twoCitySchedule(costs))