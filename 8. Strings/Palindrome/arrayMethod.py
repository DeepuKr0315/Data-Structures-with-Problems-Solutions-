# T =O(n) beacuse we pushing to the array and traversing the string only one
# S = O(n) because we creating new array which will be converted into string later on
def isPalindrome(str):
    newArray = []
    for i in reversed(range(len(str))):
        newArray.append(str[i])
    if ''.join(newArray) == str:
        return True
    return False

print(isPalindrome("aba"))