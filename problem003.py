# Project-Euler-dot-com
#Solutions to problems done on projecteuler.com
#Largest prime factor
#Problem: The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

#Solution: This program will look for factors of our number and 
#reduce our number every time a factor is found and start the process again.
#This will continue until there are no more factors. aka the number left is prime. 
#Since it keeps reducing the number by dividing by factors from smallest to largest, the number remaining must be the largest
n=600851475143
i=2
while i*i<n:
    if n%i==0:
        n=n/i
        i=2
    else:
        i+=1
print(n)
