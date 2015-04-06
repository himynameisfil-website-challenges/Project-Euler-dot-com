##Status: Solved
##Problem:https://projecteuler.net/problem=28
##Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
##
##21 22 23 24 25
##20  7  8  9 10
##19  6  1  2 11
##18  5  4  3 12
##17 16 15 14 13
##
##It can be verified that the sum of the numbers on the diagonals is 101.
##
##What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?


#First thing to note is that the an individual side increases by 2 every time you add a layer
#that is represented in the j variable to get our next number.
#We start with the last number we had, and add whatever our j is to it and add it to the list
#We repeat that 4 times(1 for each corner of the square) and then we move onto our next
#layer via adding 2 to our j variable
lst = [1]
j = 2
while j <1001:
    for i in range(0,4):
        lst.append(lst[-1]+j)
    j+=2
    
print(sum(lst))
