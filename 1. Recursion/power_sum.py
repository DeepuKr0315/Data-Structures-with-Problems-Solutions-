def power_sum(array, power=1):
    sumi = 0
    for i in array:
        if type(i)==list:
            sumi += power_sum(i, power+1)
        else:
            sumi += i
    return sumi**power

print(power_sum([1,2,[3,4],[[2]]]))