# Project-Euler-dot-com
Solutions to problems done on projecteuler.com
def factors(x):
    list =[]
    for i in range(1,int(round(x**.5+1))):
        if x%i==0:
            list.append(i)
            list.append(x/i)
    return len(set(list))
i=1
n=int(input("You want the first triangle number to have over x divisors, what is x?"))

while i>0:
    trinum=int((i*(i+1))/2)
    if factors(trinum)>n:
        print(trinum)
        break
    i+=1
