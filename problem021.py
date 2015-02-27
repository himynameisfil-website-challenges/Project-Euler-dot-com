# Project-Euler-dot-com
Solutions to problems done on projecteuler.com
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
