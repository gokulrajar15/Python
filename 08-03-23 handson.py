class Marks:
    def __init__(self):
        self.Tamil = 0
        self.English = 0
        self.Maths = 0
        self.Science = 0
        self.Social = 0

    def enter_marks(self, Tamil, English, Maths, Science, Social):
        self.Tamil = Tamil
        self.English = English
        self.Maths = Maths
        self.Science = Science
        self.Social = Social

    def display_marks(self):
        print("Tamil = {}".format(self.Tamil))
        print("English = {}".format(self.English))
        print("Maths = {}".format(self.Maths))
        print("Science = {}".format(self.Science))
        print("Social = {}".format(self.Social))


class average(Marks):
    def display_total_average(self):
        Total = (self.Tamil + self.English + self.Maths + self.Science + self.Social)
        average = Total/5
        print("The total mark is {}".format(Total))
        print("The Average mark is {}".format(average))



class Student(average):
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


gokul = Student("Gokul", "10th", "Male", "999230202", "mettur,salem")
gokul.display_details()
gokul.enter_marks(37, 45, 89, 23, 45)
gokul.display_marks()
gokul.display_total_average()
