# Project-Euler-dot-com
Solutions to problems done on projecteuler.com
n = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

##n="""3
##7 4
##2 4 6
##8 5 9 3"""

#What i want the code to do:
#First i'll it start w/ our first number [3]        (in our code, this will be labeled as our current list)
#It'll take a look at the next row 7 4 and i'll just have a new row which will be the max sum( [7,4] will be labeled as our comparison list)
#in this case it'll look like [10,7]        (This will be the start of our next itteration of code called next list)

#Then it'll look at the next row and look at it's optimal options [12, (14 or 11), 13] (the code will loop w/ [10,7] as our current list, [2,4,6] as our comparision, and [12,14,13] will be our next current list)
#it will pick the larger one so [12,14,13]
#it will move onto the next row [20, (17 or 19), (23 or 21), 16] etc.
current_list=[int(n.split("\n")[0])]

for i in range(0,len(n.split("\n"))-1):     #This for loop w/ i will look for the maximum sum for the current row it's on(repeated till the last row
    comparison_list=[]
    next_list=[]
    for k in range(0,len(n.split("\n")[i+1].split(" "))):           #This loop will construct our comparison list. 
        comparison_list.append(int(n.split("\n")[i+1].split(" ")[k]))   
    for j in range(0,len(comparison_list)):                 #This entire for loop will create our next list which will be the "current list" of our next index 
        if j==0:
            next_list.append(current_list[j]+comparison_list[j])
        elif j==len(comparison_list)-1:
            next_list.append(current_list[j-1]+comparison_list[j])
        else:
            if (comparison_list[j]+current_list[j-1])>(comparison_list[j]+current_list[j]):
                next_list.append(comparison_list[j]+current_list[j-1])
            else:
                next_list.append(comparison_list[j]+current_list[j])
    current_list=next_list
x=0
for l in range(0,len(next_list)):
    if next_list[l]>x:
        x=next_list[l]

print(x)
