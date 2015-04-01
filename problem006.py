# Project-Euler-dot-com
#Solutions to problems done on projecteuler.com
#Problem: The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

#This program will create a list of squares of all natural numbers from 1 to 100
#It will then find the difference of the sum of squares and the square of sums
sumsquare = [i**2 for i in range(1,101)]
squaresum = (101*100/2)**2
print(squaresum - sum(sumsquare))
