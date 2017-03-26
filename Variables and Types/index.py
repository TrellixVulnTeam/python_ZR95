# Assignments can be done on more than one variable "simultaneously" on the same line like this
# https://www.learnpython.org/en/Variables_and_Types
a, b = 3, 4
print(a,b)

# Mixing operators between numbers and strings is not supported:
# one = 1
# two = 2
# hello = "hello"
# print(one + two + hello)

mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)