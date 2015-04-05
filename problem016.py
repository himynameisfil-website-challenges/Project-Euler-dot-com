##Status: Solved
##Problem:2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
##What is the sum of the digits of the number 2^1000?

x=2**1000
x=str(x)
powersum=0
for i in range(0,len(x)):
    powersum+=int(x[i])
print(powersum)
