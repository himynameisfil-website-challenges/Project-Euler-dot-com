##Status: Solved
##Problem:You are given the following information, but you may prefer to do some research for yourself.
##
##1 Jan 1900 was a Monday.
##Thirty days has September,
##April, June and November.
##All the rest have thirty-one,
##Saving February alone,
##Which has twenty-eight, rain or shine.
##And on leap years, twenty-nine.
##A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
##How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

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
