# Problem link = https://www.geeksforgeeks.org/dsa/egg-dropping-puzzle-dp-11/
# You are given n identical eggs and you have access to a k-floored building from 1 to k.

from functools import lru_cache

@lru_cache(maxsize=None)
def egg_drop(n, k):
    if k == 0 or k == 1:
        return k
    if n == 1:
        return k
    res = float('inf')
    for i in range(1, k + 1):
        # Check the worst case of dropping an egg from floor i
        # If it breaks we check below, if it doesn't break we check above
        print(f"Checking floor {i} with {n} eggs and {k} floors")
        cur = 1 + max(egg_drop(n - 1, i - 1), egg_drop(n, k - i))
        res = min(res, cur)
    return res

# print(egg_drop(2, 36))
print(egg_drop(2, 100))