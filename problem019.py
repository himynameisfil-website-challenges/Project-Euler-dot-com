# Project-Euler-dot-com
Solutions to problems done on projecteuler.com
import timeit
start= timeit.timeit()

d=0             #days elapsed
x=0
for y in range(0,101):      #year's we're considering
    for m in range(1,13):   #month we're considering
        if d%7==6 and y!=0:
            x+=1
        if m in [4,6,9,11]:
            d+=2
        elif m==2:
            if y%4==0 and ((y+1900)%100!=0 or (y+1900)%400==0):
                d+=1
        else:
            d+=3

print(x)

end=timeit.timeit()
print(end-start)
