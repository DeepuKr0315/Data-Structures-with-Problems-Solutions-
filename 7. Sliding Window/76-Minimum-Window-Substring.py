
# problem link = https://leetcode.com/problems/minimum-window-substring/description/

def minWindow(s, t):
    if t == "":
        return ""
    count_t = {}
    window = {}
    for c in t:
        count_t[c] = 1 + count_t.get(c, 0)
    need, have = len(count_t)   , 0
    res = [-1, -1]
    res_length = float('inf')
    left = 0
    for right in range(len(s)):
        c = s[right]
        window[c] = 1 + window.get(c, 0)
        # check whether currently a criteria has been met
        if c in count_t and window[c] == count_t[c]:
            have += 1
        # let's check whether all chars are present or not
        while have == need:
            #moving left pointer
            #the current window is a valid window
            if (right - left + 1) < res_length:
                res = [left, right]
                res_length = right - left + 1
            # move left pointer
            # 1. window[s[left]] decrement
            window[s[left]] -= 1
            # 2. have has to be decremented or not
            if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                have -= 1
            left += 1
    left, right = res
    return s[left:right+1] if res_length != float('inf') else ''

s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))