# Dictionaries chapter 5
# distionary format is also called json formate
#

student = {'name':'Taha', 'age':51}
print(student['age'])

# Adding new attribute in dictionary
student['id']= 21009
print(student)

# remove key from dictionary
del student['name']
print(student)

# item in dictionnary
print(student.items())

for key, value in student.items():
    print("Key: " + key )
    # print("My Value: " + value)




# for key in student.keys():
#     print("Key: " + key )




# for myvalue in student.values():
#     print("myvalue: " + myvalue )


