class Parent():
    def __init__(self, name):
        self.name = name

    def Print_Name(self):
        print (("My name is ") + self.name)


class Child(Parent):
    pass


a = Child("Sachin")

a.Print_Name()
