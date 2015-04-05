##Status: SOlved
##Problem:145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
##
##Find the sum of all numbers which are equal to the sum of the factorial of their digits.
##
##Note: as 1! = 1 and 2! = 2 are not sums they are not included.


import math

#This function will return true under the condition that the sum of the factorial digits is equal to the original number
def digitfactorial(x):
  y = [math.factorial(int(i)) for i in str(x)]
  return sum(y) == x
#This list will contain all digit factorials. They key to finding the upper limit is that there is a breakpoint where adding the worst case scenario(9!) is less significant than actually adding a digit to the whole sequence.
#That breakpoint occurs between a 7 and 8 digit number
lst = [i for i in range(3,math.factorial(9)*7+1) if digitfactorial(i)]
print(sum(lst))
