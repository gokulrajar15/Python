class Marks:
    #constructor
    def __init__(self):
        self.Tamil, self.English, self.Maths, self.Science, self.Social = 0, 0, 0, 0, 0

    # for receiving marks
    def enter_marks(self, Tamil, English, Maths, Science, Social):
        self.Tamil = Tamil
        self.English = English
        self.Maths = Maths
        self.Science = Science
        self.Social = Social

    # for displaying marks
    def display_marks(self):
        print("Tamil = {}".format(self.Tamil))
        print("English = {}".format(self.English))
        print("Maths = {}".format(self.Maths))
        print("Science = {}".format(self.Science))
        print("Social = {}".format(self.Social))


class average:
    def display_total_and_Avg(self):
        Total = self.Tamil + self.English + self.Maths + self.Science + self.Social
        print("The Total mark of {} is {}".format(self.name, Total))
        average = Total / 5
        print("The Average mark is {}".format(average))



class Student(average, Marks):
    def __init__(self, name, s_class, sex, ph_number, address):
        self.name = name
        self.s_class = s_class
        self.sex = sex
        self.ph_number = ph_number
        self.address = address

    def display_details(self):
        print("Name: {}".format(self.name))
        print("Class: {}".format(self.s_class))
        print("Sex: {}".format(self.sex))
        print("Phone Number: {}".format(self.ph_number))
        print("Address: {}".format(self.address))


print("------------Students Details------------------------")
gokul = Student("Gokul", "10th", "Male", "999230202", "mettur, salem")
gokul.display_details()
print("------------------Marks------------------------")
gokul.enter_marks(37, 45, 89, 23, 45)
gokul.display_marks()
gokul.display_total_and_Avg()
