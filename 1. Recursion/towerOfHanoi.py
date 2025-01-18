def toh(N, fromm, to, aux):
    count = 0
    def helper(N, fromm, to, aux):
        nonlocal count #beacause count is not a global var andwe will not be able to incriment it's value without using this function
        if N==1:
            #print("Move disk", N, "from rod", fromm,"to rod", to)
            count += 1
            return
        helper(N-1, fromm, aux, to)
        #print("Move disk", N, "from rod", fromm,"to rod", to)
        count += 1
        helper(N-1, aux, to, fromm)
    helper(N, fromm, to, aux)
    #print("Total num of movements ==> ", count)
    return count
a = int(input("Enter number of plates you wants to shift ==> "))
print("Number of movements we have to make ==> ",toh(a, 1, 3, 2))