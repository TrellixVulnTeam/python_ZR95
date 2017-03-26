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