def maxEnvelopes(envelopes):
    
    envelopes.sort(key = lambda x:(x[0], -x[1]))
    n = len(envelopes)
    sub = [envelopes[0][1]]

    def binSearch(sub, num):
        left, right = 0, len(envelopes)-1
        while left < right:
            mid = (left + right) // 2
            if sub[mid] < num:
                left = mid+1
            else:
                right = mid
        return left
    for i in range(1, n):
        num = envelopes[i][1]
        if num > sub[-1]:
            sub.append(num)
        else:
            x = binSearch(sub, num)
            sub[x] = num
    return len(sub)

e = [[4,5],[4,6],[6,7],[2,3],[1,1]]
print(maxEnvelopes(e))