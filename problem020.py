# Project-Euler-dot-com
Solutions to problems done on projecteuler.com
def factorial(x):
    if x==0:
        return 1
    else:
        return x*factorial(x-1)

n=factorial(100)
sumfunction=0
for i in range(0,len(n)):
    sumfunction+=int(str(n)[i])
print(sumfunction)
