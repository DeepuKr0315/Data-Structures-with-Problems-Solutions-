
# problem link = https://leetcode.com/problems/two-city-scheduling/description/

def twoCitySchedule(costs):
    def minCost(i, a_count):
        if len(costs) == i:
            return 0
        if a_count < len(costs)//2:
            costA = costs[i][0] + minCost(i + 1, a_count+1)
        else:
            costA = float('inf')
        b_count = i - a_count
        if b_count < len(costs)//2:
            costB = costs[i][1] + minCost(i + 1, a_count)
        else:
            costB = float("inf")
        return min(costA, costB)
    return minCost(0, 0)

costs = [[10,20],[30,200],[400,50],[30,20]]
print(twoCitySchedule(costs))