# Project-Euler-dot-com
#Solutions to problems done on projecteuler.com
#largest palindrome product
#Problem: A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

#Solution: the function palindrometest will comparethe last number with the first, 2nd to last with the second, etc until all elements are checked
#If at any point in time the numbers don't match with its partner number, it'll return false. if they all match, the function will return true.
def palindrometest(x):
  x = str(x)
  for i in range(0, int(len(x)/2)):
    if x[i] != x[len(x) - 1 - i]:
      return False
  else:
    return True

#This section will look at all numbers that are a multiple of three digit numbers. If the number is palindromic and larger than any previous palindromic number checked, 
#the largestpalindrome variable will update accordingly
largestpalindrome = 0
for i in range(100,1000):
  for j in range(i,1000):
    if i * j < largestpalindrome and palindrometest(i*j):
      largestpalindrome = i*j
print(largestpalindrome)
