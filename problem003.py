# Project-Euler-dot-com
Solutions to problems done on projecteuler.com
#Largest prime factor
n=600851475143
i=2
while i*i<n:
    if n%i==0:
        n=n/i
        i=2
    else:
        i+=1
print(n)
