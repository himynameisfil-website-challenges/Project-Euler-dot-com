# Project-Euler-dot-com
Solutions to problems done on projecteuler.com
x=2**1000
x=str(x)
powersum=0
for i in range(0,len(x)):
    powersum+=int(x[i])
print(powersum)
