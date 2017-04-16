class Student():
    def  __init__(self, name, age):
           self.name = name
           self.age = age
    def ageMsg(self):
        print(self.age)

s1 = Student('taha', 28)

s2 = Student('Wamic', 27)

print(s1.name)
s2.ageMsg()