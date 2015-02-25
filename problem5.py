# Project-Euler-dot-com
Solutions to problems done on projecteuler.com
#smallest multiple
n=0
i=0
j=1
a=1
def primesunder(x):         #This function will make an array of prime numbers equal to or below the number you input
    list = [2]
    for i in range(3,x+1):
        for j in range(0,len(list)):
            if i%list[j]==0:
                break
        else:
            list.append(i)
    return list

n=20
for i in range(0,len(primesunder(n))):      #This for+while loop will effectively construct our number we're looking for
        j=1                                 
        while j>0:                          #So for the example, it's [2,3,5,7]. and the first for loop goes through each element in that set
            if primesunder(n)[i] ** j > n:  #It then looks for a prime^j such that it's larger than our number we entered, so it would've found 2^4>10, 3^3>10, 5^2>10, and 7^2>10
                a*=primesunder(n)[i] ** (j-1)   #from here, it just constructs our number by a= 1 * (prime_1^(j_1-1)) * (prime_2^(j_2 - 1)) * etc.
                break
            j+=1
        
print(a)
