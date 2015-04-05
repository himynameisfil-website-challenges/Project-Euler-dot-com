# Status: Solved
#Problem: The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

#Solution:
#This will look at all odd numbers between 3 and two million and add them together under the variable primesum... then add 2(technically it starts as 2 and add the other ones)
primesum=2
x=2000000
for i in range(3,x+1,2):
    for j in range(3,int(round(i**.5+1)),2):
        if i%j==0:
            break
    else:
        primesum+=i
print(primesum)
