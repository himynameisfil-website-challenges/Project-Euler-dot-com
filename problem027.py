##Status: Solved
##Problem:https://projecteuler.net/problem=27
##Euler discovered the remarkable quadratic formula:
##
##n² + n + 41
##
##It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.
##
##The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.
##
##Considering quadratics of the form:
##
##n² + an + b, where |a| < 1000 and |b| < 1000
##
##where |n| is the modulus/absolute value of n
##e.g. |11| = 11 and |−4| = 4
##Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

largest,x,y,a,b = 0,0,0,0,0
#Function to determine primality
def isprime(x):
    if x<=1:
        return False
    if x ==2:
        return True
    if x %2 ==0:
        return False
    i =3
    while i*i<=x:
        if x%i == 0:
            return False
        i+=2
    else:
        return True
#Function that will determine how many primes will be produced for consecutive n values 0 to n
    #for the formula n^2 +a*n +b
def primecount(a,b):
    n = 0
    x = b
    while isprime(x):
        n+=1
        x = (n**2)+(n*a)+b
    return n

#orginally, i just set the a and b range from -999 to 999 but
#The formula implies that b needs to be prime in order for the consecutive values to be greater than 0
#therefore, i shortened one of the ranged to just the primes(in the list called lst)
lst = [i for i in range(0,1000) if isprime(i)]
for i in range(-999,1000):
    for j in lst:
        if primecount(i,j)>largest:
            largest = primecount(i,j)
            x = i
            y = j
print(x*y)

