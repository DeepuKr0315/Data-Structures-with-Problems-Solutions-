def discriminant(a, b, c):
    D = (b * b) - (4* (a * c))
    if D >= 0:
        return f"Dicriminant D = {D} which is positive and roots will be real"
    else:
        return f"Dicriminant D = {D} which is negative and roots will be imaginary"

a = int(input())
b = int(input())
c = int(input())
print(discriminant(a, b, c))
