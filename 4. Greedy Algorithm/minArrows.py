# problem link == https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/

def minArrows(points):
    n = len(points)
    points.sort(key = lambda x : x[1])
    end = float('-inf')
    res = 0
    for start, finish in points:
        if start > end:
            end = finish
            res += 1
    return res

points = [[10,16],[2,8],[1,6],[7,12]]
print(minArrows(points))