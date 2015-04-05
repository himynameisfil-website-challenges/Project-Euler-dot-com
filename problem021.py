##Status: Solved
##Problem: Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
##If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
##For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
##Evaluate the sum of all the amicable numbers under 10000.

def divisor_sum(x):
    list=1
    for i in range(2,int(x**.5)+1):
        if x%i==0:
            list+=i
            if i!=x/i:
                list+=x/i
    return list


am_sum=0
for i in range(1,10000):
    x=divisor_sum(i)
    y=divisor_sum(x)
    if y==i and x!=i and x<10000:
        am_sum+= i + x


print(am_sum/2)
