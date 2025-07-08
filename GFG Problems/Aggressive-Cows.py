# Problem link = https://www.geeksforgeeks.org/problems/aggressive-cows/1?

def aggresiveCows(stalls, k):
    stalls.sort()
    def can_place(mid_dist):
        count = 1
        last_pos = stalls[0]
        for i in range(1, len(stalls)):
            if stalls[i] - last_pos >= mid_dist:
                count += 1
                last_pos = stalls[i]
        return count >= k
    low = 0
    high = stalls[-1] - stalls[0]
    result = 0
    while low <= high:
        mid = (low + high) // 2
        if can_place(mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    return result

stalls = [10, 1, 2, 7, 5]
k = 3
print(aggresiveCows(stalls, k))  # Output: 4