# Project-Euler-dot-com
#Solutions to problems done on projecteuler.com
#smallest multiple
#Problem: 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

n=0
i=0
j=1
a=1
#This function will make an array of prime numbers equal to or below the number you input
def primesunder(x):         
    list = [2]
    for i in range(3,x+1):
        for j in range(0,len(list)):
            if i%list[j]==0:
                break
        else:
            list.append(i)
    return list

n=20
#This for+while loop will effectively construct our number we're looking for
#So for the example, it's [2,3,5,7]. and the first for loop goes through each element in that set
#It then looks for a prime^j such that it's larger than our number we entered, so it would've found 2^4>10, 3^3>10, 5^2>10, and 7^2>10
#from here, it just constructs our number by a= 1 * (prime_1^(j_1-1)) * (prime_2^(j_2 - 1)) * etc.


for i in range(0,len(primesunder(n))):      
        j=1                                 
        while j>0:                          
            if primesunder(n)[i] ** j > n:  
                a*=primesunder(n)[i] ** (j-1)
                break
            j+=1
        
print(a)
