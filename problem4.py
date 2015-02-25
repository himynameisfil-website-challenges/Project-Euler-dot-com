# Project-Euler-dot-com
Solutions to problems done on projecteuler.com
#largest palindrome product

def palindrometest(x):
  x = str(x)
  for i in range(0, int(len(x)/2)):
    if x[i] != x[len(x) - 1 - i]:
      return False
  else:
    return True
largestpalindrome = 0
for i in range(100,1000):
  for j in range(i,1000):
    if i * j < largestpalindrome and palindrometest(i*j):
      largestpalindrome = i*j
print(largestpalindrome)
