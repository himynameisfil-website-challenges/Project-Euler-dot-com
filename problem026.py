#Status: Solved
##Problem: A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
##
##1/2	= 	0.5
##1/3	= 	0.(3)
##1/4	= 	0.25
##1/5	= 	0.2
##1/6	= 	0.1(6)
##1/7	= 	0.(142857)
##1/8	= 	0.125
##1/9	= 	0.(1)
##1/10	= 	0.1
##Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
##
##Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

import math
#This function will find where the long division loop starts/ends using remainders
#and return how many entries are in the loop
def longdivision(x):
    R = 1
    lst = []
    while lst.count(R)==0:
        if R==0:
            return 0
        lst.append(R)
        Q = math.floor(R/x)
        R = (R - (Q*x))*10
    return len(lst[lst.index(R):])

#This section will go through the denominators 2-999 and will replace the champion number whenever it finds a case that returns a larger loop
championnumber = 0
championvalue = 0
for i in range(2,1000):
    if longdivision(i)>championvalue:
        championnumber = i
        championvalue = longdivision(i)
print(championnumber)
