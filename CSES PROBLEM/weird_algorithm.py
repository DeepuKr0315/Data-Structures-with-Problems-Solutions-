n = int(input())
print(n, end=' ')
def weird_algorithm(n):
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        print(n, end=' ')
weird_algorithm(n)