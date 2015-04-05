##Status: Solved
##Problem: If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
##
##If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
##
##
##NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

numbermap = [0,3,3,5,4,4,3,5,5,4]  #This is a map from our base numbers to the ammount of letters used
hundred = 7
thousand = 8
und = 3
teens = [3,3,3,3,4,3,4,4,3,4]   #additional letters relative to its single digit place
tens = [0,"blank",6,6,5,5,5,7,6,6]        #tens 20, 30,....

count = 0

for i in range(1,1001): #This for loop will go thorugh each number
    strnum = str(i)
    count+=numbermap[int(strnum[len(strnum)-1])]     #for said number, it'll count the letters used for the singles digit place
    if i >9:                                            #for any number beyond 9, it'll take into conideration the tens digit place using the teens as a special case ruling relative to the others
        if int(strnum[len(strnum)-2]) == 1:
            count+=teens[int(strnum[len(strnum)-1])]
        else:
            count+=tens[int(strnum[len(strnum)-2])]
    if i > 99:                                          #this will consider the hundreds digit place making rules about when to add hundred and and
        count+=numbermap[int(strnum[len(strnum)-3])]
        if i%1000 !=0:
            count+= hundred
        if i%100 != 0:
            count+=und
    if i > 999:
        count+=numbermap[int(strnum[len(strnum)-4])]
        count+= thousand
print(count)
