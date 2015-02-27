# Project-Euler-dot-com
Solutions to problems done on projecteuler.com
a=0
b=0
c=0

for c in range(1,1000):
    for b in range(1,c):
        a=1000-c-b
        if 0<a<b<c and a**2+b**2==c**2:
            print(a*b*c)
            break
