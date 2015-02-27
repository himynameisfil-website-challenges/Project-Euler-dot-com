# Project-Euler-dot-com
Solutions to problems done on projecteuler.com
#this is done via bruteforce. extremely inefficient

def collatzlength(x):
    j=1
    while j>0 and x!=1:
        if x%2==0:
            x/=2
        else:
            x=3*x+1
        j+=1
    return j

champion=1
i=0
for i in range(1,1000000):
    print("i=",i)
    print("champ=",champion)
    if collatzlength(i)>collatzlength(champion):
        champion=i
        
print(champion)


lista = [ [1], [1] ]      #i want this array to be set up like a database where the first subset contails the starting number
                        #and the equivalent position number in the second subset is it's collatz number

def collatzlength(x):
    j=1
    while j>0 and x!=1:
        if x%2==0:
            x/=2
        else:
            x=3*x+1
        j+=1
    return j

for i in range(2,100):
    lista[0].append(i)
    lista[1].append(collatzlength(i))
for k in range(0,99):
    print(lista[0][k],lista[1][k])
