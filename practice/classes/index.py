class Dog():
        def __init__(self, name, age):
            """Initialize name and age attributes."""
            self.name = name
            self.age = age

        def sit(self):
            """Simulate a dog sitting in response to a command."""
            print(self.name.title() + " is now sitting.")

        def roll_over(self):
            """Simulate rolling over in response to a command."""
            print(self.name.title() + " rolled over!")


d1 = Dog('red dog', '2')
d1.sit()
d1.roll_over()

d2 = Dog(age=12, name='black Dog')

d2.sit()
d2.roll_over()
print(d2.name)