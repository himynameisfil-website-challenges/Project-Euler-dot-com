#Status: Solved

#Problem : By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

#This function will make an array of prime numbers equal to or below the number you input
def xthprime(x):         
    list = [2]
    i=3
    while len(list)<x:
        for j in range(0,len(list)):
            if i%list[j]==0:
                i+=1
                break
        else:
            list.append(i)
            i+=1
    return list

#this will just print the last item of the list which is the number you're looking for
n=10001
print(xthprime(n)[len(xthprime(n))-1])
