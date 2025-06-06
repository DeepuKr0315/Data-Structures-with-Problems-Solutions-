# problem link = https://leetcode.com/problems/gas-station/description/

def canCompleteCircuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    res = 0
    total = 0
    for i in range(len(gas)):
        total += gas[i] - cost[i]
        if total < 0:
            total = 0
            res = i + 1
    return res

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(canCompleteCircuit(gas, cost))