def nonRepeatChar(str):
    check = {}
    for c in str:
        if c in check:
            check[c] += 1
        else:
            check[c] = 1
    for i in range(len(str)):
        if check[str[i]] == 1:
            return i
    return None

print(nonRepeatChar("abaRb150cd"))