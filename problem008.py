#status: Solved

#Problem: The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
#The number in question can be found here: https://projecteuler.net/problem=8
#Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

x=13
n=str(input("Input the thousand digit code"))
largestproduct=0
currentproduct=1
#This will go through the sequence and multiply x amount of adjacent numbers, whenever the program finds a product larger than the current largest number,
#The larger number will replace it. Then it will print the largest number after it's gone through every combination
for i in range(0,len(n)-x-1):
    currentproduct=1
    for j in range(0,x):
        currentproduct*=int(n[i+j])
    if currentproduct>largestproduct:
        largestproduct=currentproduct

print(largestproduct)
