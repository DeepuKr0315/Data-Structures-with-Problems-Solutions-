# Time complexity = O(n^2) traversing string = O(n) and appending string = O(n)
# Space Complexity = O(n) because we creating a new string of same length as of given string
def isPalindrome(str):
    new_str = ""
    for i in reversed(range(len(str))):
        new_str += str[i]
    if str == new_str:
        return True
    return False
print(isPalindrome("aaabaaa"))