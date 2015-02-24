# Project-Euler-dot-com
Solutions to problems done on projecteuler.com
goldenratio = (1 + 5**.5)/2
negagolden = ( 1- 5 ** .5)/2
def fibonacci(x):
  n = ((goldenratio ** x) - (negagolden ** x)) / (5 ** .5)
  return int(round(n,0))
count = 0
i = 0
while fibonacci(i)<4000000:
  if fibonacci(i)%2==0:
    count+=fibonacci(i)
  i+=1
print(count)
