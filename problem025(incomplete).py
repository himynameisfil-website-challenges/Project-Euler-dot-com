##Status: inefficient. possible to solve using the lengths of a string instead of a number
##Problem:The Fibonacci sequence is defined by the recurrence relation:
##
##Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
##Hence the first 12 terms will be:
##
##F1 = 1
##F2 = 1
##F3 = 2
##F4 = 3
##F5 = 5
##F6 = 8
##F7 = 13
##F8 = 21
##F9 = 34
##F10 = 55
##F11 = 89
##F12 = 144
##The 12th term, F12, is the first term to contain three digits.
##
##What is the first term in the Fibonacci sequence to contain 1000 digits?



goldenratio = (1 + 5**.5)/2
negagolden = ( 1- 5 ** .5)/2
def fibonacci(x):
  n = ((goldenratio ** x) - (negagolden ** x)) / (5 ** .5)
  return int(round(n,0))


n = 1
while n>0:
    if fibonacci(n)>=10**2:
      print(fibonacci(n))
      break
    n+=1
            
