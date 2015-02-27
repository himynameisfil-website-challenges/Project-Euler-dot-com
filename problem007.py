# Project-Euler-dot-com
Solutions to problems done on projecteuler.com
def xthprime(x):         #This function will make an array of prime numbers equal to or below the number you input
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

n=int(input("you want the xth prime number, what is x?"))
print(xthprime(n)[len(xthprime(n))-1])
