def maxEnvelopes(envelopes):
    n = len(envelopes)
    dp = [1]*n
    envelopes.sort(key = lambda x:(x[0], -x[1]))
    maximum = 1
    for i in range(1, n):
        for j in range(i):
            if dp[j] + 1 > dp[i] and envelopes[i][1] > envelopes[j][1]:
                dp[i] = dp[j]+1
        if maximum < dp[i]:
            maximum = dp[i]
    return maximum

envelopes = [[5,4],[6,4],[6,7],[2,3]]
print(maxEnvelopes(envelopes))