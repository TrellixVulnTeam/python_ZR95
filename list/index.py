colors = ['red', 'blue', 'green']
print (colors[0])  ## red print
print (colors[2] ) ## green print
print(len(colors))  ## 3

# Assignment with an = on lists does not make a copy. Instead, assignment makes the two variables point to the one list in memory.
b = colors
b[0]= "new red by b"

print(colors)
print(b)

# Accessing an index which does not exist generates an exception (an error).
# https://www.learnpython.org/en/Lists
# mylist = [1,2,3]
# print(mylist[10])

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

second_name = names[1]


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

# Using Operators with Lists
# Lists can be joined with the addition operators:
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)