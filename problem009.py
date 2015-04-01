# Project-Euler-dot-com
#Solutions to problems done on projecteuler.com
#Problem: A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
a=0
b=0
c=0
#This will go through every combination of 3 numbers that can add up to 1000, then it will find the product of that combination
for c in range(1,1000):
    for b in range(1,c):
        a=1000-c-b
        if 0<a<b<c and a**2+b**2==c**2:
            print(a*b*c)
            break
