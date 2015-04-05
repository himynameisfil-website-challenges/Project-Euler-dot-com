#Status: Solved

#Problem : If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

#creates a list of all numbers divisible by 3 or 5 between 0 and 999. Then prints the sum of the list
lst = [i for i in range(0,1000) if i%3==0 or i%5==0]
print(sum(lst))
