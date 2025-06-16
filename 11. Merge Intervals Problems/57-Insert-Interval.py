
# problem link = https://leetcode.com/problems/insert-interval/description/

def insert(intervals, newInterval):
    res = []
    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]:
            res.appen(newInterval)
            return res + intervals[i:]
        elif newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
        else:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = min(newInterval[1], intervals[i][1])
    res.append(newInterval)
    return res

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(insert(intervals, newInterval))