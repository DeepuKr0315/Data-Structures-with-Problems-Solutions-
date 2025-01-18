def numRescueBoats(people, limit):
    #write code here
    people.sort()
    x=0
    l, r=0, len(people)-1
    while l<=r:
        x+=1
        if people[l]+people[r]<=limit:
            l+=1
        r-=1
    return x

people = [3, 5, 3, 4]
limit = 5
print(numRescueBoats(people, limit))