#!/usr/bin/env python

number_int = 10
print 'Integer Number : ',number_int

number_floating = 10.0
print 'Floating Point Number : ',number_floating

number_long = 20L
print 'Long Number : ',number_long

del number_long

# print 'Trying to print deleted Long Number : ', number_long

number_complex = 3 + 4j
print 'Complex Number : ',number_complex

str = 'Hello World'

#This is possible
# del str

print 'Full String : ',str

print 'First character : ',str[0]

print 'First 3 characters : ',str[:3]

print 'Second character to fourth character : ',str[1:5]

print 'Print 3rd character from the last : ', str[-3]

print 'Print last 5 characters : ', str[-5:]

print 'Length of the string : ',len(str)

comp_num = complex(4, 5)

print 'New Complex number : ', comp_num

r_line = repr("dandanakka _//\\_")
sadha_line = "dandanakka _//\\_"

print "Dandanakka : ", r_line

print "Sadha Line : ", sadha_line

eval = eval("1 + 2 * 3")

print "Evaluated expression : ", eval

list_obj = ['This', 'is', 'a', 'list']

tuple_obj = ['is', 'is', 'sa', 'tu']

print "This is a tuple typecasted into list : ", list(tuple_obj)

print "This is a list typecasted into tuple : ", tuple(list_obj)

print "This is a list typecasted into a dictionary : ", dict(tuple_obj)

print "A when converted to an integer", ord('A')

print "A converted to hex", hex(255)

print "A converted to octal", oct(7)

print "Integer division", (int(8)/int(5))

print "Exponentiation - 2**3 is : ", 2**3

print "Floor Division - 5//2 is :", 5//2

print "Floor Division - 4.4//2.3 : ", 4.4//2.3

print "Not Equal Operator : 2<>3 ", 2<>3

print "Not Equal Operator : 2!=2 ", 2!=2


# Identity Operators
a = 20
b = 20

print "a : ", a, "and b : ", b

if a is b:
    print "a and b are equal"
else:
    print "a and b are not equal"

b = 30

print "a : ", a, "and b : ", b

if a is b:
    print "a and b are equal"
else:
    print "a and b are not equal"

print "Difference between 'is' and '=='"

tuple_a = (1, 2)
tuple_b = (1, 2)

print "tuple_a : ", tuple_a," and tuple_b : ", tuple_b


if tuple_a is tuple_b:
    print "tuple_a is tuple_b"
else:
    print "tuple_a is not tuple_b"

if tuple_a == tuple_b:
    print "tuple_a == tuple_b"
else:
    print "tuple_a == not tuple_b"

print "Member Ship Operators"

if 1 in tuple_a:
    print "1 is in tuple_a"
else:
    print "1 is not in tuple_a"

if 3 in tuple_a:
    print "3 is in tuple_a"
else:
    print "3 is not in tuple_a"

if "3" in tuple_a:
    print "str(3) is in tuple_a"
else:
    print "str(3) is not in tuple_a"
