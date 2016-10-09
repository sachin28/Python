class Info(object):
    def __init__(self, name, age, address):

        self.name = name
        self.age = age
        self.address = address

    def name_print(self):
        print self.name

    def age_print(self):
        print self.age

    def address_print(self):
        print self.address

class ChildInfo(Info):

    def __init__(self, name, age, address, school):

        self.school = school
        super(ChildInfo, self).__init__(name, age, address)

   # def doubleAge(self):
       # print 2*int(self.age)


    def school_print(self):

        print self.school


a = Info("Sachin", "25", "SanJose")
b = ChildInfo("Sandeep", "22", "Pune", "PCCOE")

a.age_print()
b.name_print()
b.school_print()
#b.school()

