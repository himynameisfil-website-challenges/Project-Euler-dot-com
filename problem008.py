# Project-Euler-dot-com
Solutions to problems done on projecteuler.com
x=int(input("Product of x adjacent numbers... what is x?"))
n=str(input("Input the thousand digit code"))
largestproduct=0
currentproduct=1
for i in range(0,len(n)-x-1):
    currentproduct=1
    for j in range(0,x):
        currentproduct*=int(n[i+j])
    if currentproduct>largestproduct:
        largestproduct=currentproduct

print(largestproduct)
