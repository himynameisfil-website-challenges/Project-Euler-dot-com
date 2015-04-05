#Status: Logic error somehwere: getting an incorrect answer

#Problem: A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

#Solution
###This function will find all factors between 1 and sqrtx... then find the rest of the factors since they're the compliments of the previous ones
import math
def abundant(x):
    lst = [i for i in range(1,math.ceil(x**.5)) if x%i==0]
    for i in lst[1:]:
        if x/i != i:
            lst.append(x/i)
    return sum(lst)>x
###the only range of abundant numbers we care about range from 12 to 28123 so this creates a list of those abundant numbers
lst = [i for i in range(12,28124) if abundant(i)]

###The idea for this next part is to have the set of integers from 1-28124(comparelst) and construct a list of numbers that
###are the sum of two abundant numbers. Then i'll take the set difference between the two to get the set of numbers that
###aren't the sum of two abundant numbers
addlist = set()
comparelist = {i for i in range(1,28124)}
for i in range(0, len(lst)):
    for j in range(i,len(lst)):
        addlist.add(lst[i]+lst[j])
print(sum(comparelist.difference(addlist)))
