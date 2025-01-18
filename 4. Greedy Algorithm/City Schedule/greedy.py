# problem link = https://leetcode.com/problems/two-city-scheduling/description/

def citySchedule(costs):
    costs.sort(key = lambda x : x[0] - x[1])
    cost = 0
    n = len(costs)
    for i in range(n//2):
        cost += costs[i][0]
    for i in range(n//2, n):
        cost += costs[i][1]
    return cost

costs = [[10,20],[30,200],[400,50],[30,20]]
print(citySchedule(costs))
costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
print(citySchedule(costs))