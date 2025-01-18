# Pointer method
# T = O(n/2) = O(n) because we traversing the str till i <= j, which equals to half the length of the array
# S = O(1) 
def isPalindrome(str):
    i, j = 0, len(str)-1
    while i <= j:
        if str[i] != str[j]:
            return False
        i += 1
        j -= 1
    return True
print(isPalindrome("aabaa"))