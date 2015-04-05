#Status: Solved
#Problem: Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

#How many such routes are there through a 20×20 grid?
#Solution:
#instead of a graph, you can think of each route as a direction.
#e.g. the first example is right right down down(RRDD), second is RDRD.
#The important thing to note is that the number of moves it'll take to get to the corner is fixed
#along with the number of rights and down's you need to get there
#So the example problem is equivalent to asking "How many ways can you rearrange a 4 letter sequence with 2 R's and the rest D's?
#That's just 4 choose 2. and if you change the stuff for the problem at hand, it's 4

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
def combination(n,k):
    return int(factorial(n)/(factorial(k)*factorial(n-k)))

print(combination(40,20))

