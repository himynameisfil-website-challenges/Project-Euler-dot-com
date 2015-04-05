##Status: SOlved
##Problem:Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
##
##1634 = 14 + 64 + 34 + 44
##8208 = 84 + 24 + 04 + 84
##9474 = 94 + 44 + 74 + 44
##As 1 = 14 is not a sum it is not included.
##
##The sum of these numbers is 1634 + 8208 + 9474 = 19316.
##
##Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

#Solution

#This function will compare the sum of the 5th power of each digit to a number... to the original number and return true if it's equal
import math
def fifthdigit(x):
  lst = [math.pow(int(i),5) for i in str(x)]
  if sum(lst)==x:
    return True
  else:
    return False

#This key to this problem is to recognize that it gets to a point where adding the 5th power of the highest digit(9^5) is less significant than adding a digit to a number.
#That point occurs when you go from 6 to 7 digits hese why you only check with the upper limit as 6(9^5)
lst = [i for i in range(2,(6*9**5)+1) if fifthdigit(i)]
print(sum(lst))
