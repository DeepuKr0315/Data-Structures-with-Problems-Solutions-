
# problem link = https://leetcode.com/problems/merge-intervals/description/

def merge(intervals):
    intervals.sort(key=lambda x:x[0])
    res = [intervals[0]]
    for start, end in intervals[1:]:
        last_end = res[-1][1]
        if start <= last_end:
            res[1][-1] = max(end, last_end)
        else:
            res.append([start, end])
    return res

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))