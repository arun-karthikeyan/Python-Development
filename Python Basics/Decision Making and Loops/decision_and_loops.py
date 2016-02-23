#!/usr/bin/env python

#a = 10, b = 12, c = 13 #Not possible in python

a, b, c = 10, 12, 13

#Finding the minimum of 3 numbers using if

if ((a<b) and (a<c)):
    print a, ' is the smallest'
elif b<c:
    print b, ' is the smallest'
else:
    print c, ' is the smallest'


#using for loop to print star pattern

for i in range(1,6):
    for j in range(i):
        print '*',
    print
else:
    print 'The star pattern has been successfully printed using a for loop'

print   #prints a blank line

#using while loop to print reverse star pattern
i = 1
while (i < 6):
    j = 6-i-1
    while (j >= 0):
        print '*',
        #--j # No increment or decrement operator in python
        j-=1
    print   #Prints a blank line
    #++i    # No increment or decrement operator in python
    i+=1
else: #Gets executed when after the outer for loop is exhausted
    print 'The reverse star pattern has been successfully printed using a while loop'

#Printing prime numbers from 10 - 19 using nested for loops and break statement

for num in range(10,20):
    for div in range(2,num):
        if ((num%div)==0):
            print num, " is not a prime number"
            break
    else:
        print num, " is a prime number"

#Pass statement - a new statement in python which is used in places where a syntax is required but no execution will take places
#The below function definition will throw an error if not for the pass statement, it helps us to come back to the code to finish the implementation.
def initLog(someargs):
    pass #Remember to implement this method
