# Project-Euler-dot-com
Solutions to problems done on projecteuler.com
primesum=2
x=int(input("You want the sum of all primes below.."))
for i in range(3,x+1,2):
    for j in range(3,int(round(i**.5+1)),2):
        if i%j==0:
            break
    else:
        primesum+=i
print(primesum)
