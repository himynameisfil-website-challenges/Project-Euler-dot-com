##Status: SOlved
##Problem:The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
##
##Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
##
##(Please note that the palindromic number, in either base, may not include leading zeros.)

#This function will test whether or not something is palindromic
def palindrometest(x):
  x = str(x)
  for i in range(0, int(len(x)/2)):
    if x[i] != x[len(x) - 1 - i]:
      return False
  else:
    return True

#This will create a list of numbers under 1 million that are palindromic in binary and base 10
lst = [i for i in range(0,1000000) if palindrometest(i) and palindrometest(bin(i)[2:])]
print(sum(lst))
