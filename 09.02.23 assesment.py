from tabulate import tabulate

class circle:

    def __init__(self, radius):
        self.radius = radius

    def circle_cal(self):
        area = 3.14 * self.radius
        circumference = 2 * 3.14 * self.radius
        print("The area of the circle is {}".format(area))
        print("The Circumference  of the circle is {}".format(circumference))
        table = [["Area", "Circumference"],
                 [area, circumference]
                 ]
        print(tabulate(table, headers='firstrow', tablefmt="fancy_grid"))


class square:
    def __init__(self, ar):
        self.ar = ar

    def square_cal(self):
        area = 4 * self.ar
        print("The area of the square is {}".format(area))
        table = [["Area", "Circumference"],
                 [area, area]
                 ]
        print(tabulate(table, headers='firstrow', tablefmt="fancy_grid"))

class triangle:
    def __init__(self, length, height, a, b, c):
        self.length = length
        self.height = height
        self.a = a
        self.b = b
        self.c = c

    def triangle_cal(self):
        area = 0.5 * self.length * self.height
        circumference = self.a * self.b * self.c
        print("The area of the triangle is {}".format(area))
        print("The Circumference  of the triangle is {}".format(circumference))
        table = [["Area", "Circumference"],
                 [area, circumference]
                 ]
        print(tabulate(table, headers='firstrow', tablefmt="fancy_grid"))


class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def rectangle_cal(self):
        area = self.length * self.width
        circumference = 2 * self.length + 2 * self.width
        print("The area of the rectangle is {}".format(area))
        print("The Circumference  of the rectangle is {}".format(circumference))
        table = [["Area", "Circumference"],
                 [area, circumference]
                 ]
        print(tabulate(table, headers='firstrow', tablefmt="fancy_grid"))


print('''
        Calculation for area and circumference
        enter the shape you want 
           circle or 1
           square or 2
           triangle or 3
           rectangle or 4
''')

x = input("Enter here ---").lower()
if x == "circle" or x == "1":
    radius = int(input("Enter the radius--"))
    cal = circle(radius)
    cal.circle_cal()
elif x == "square" or x == "2":
    ar = int(input("Enter the one side length--"))
    sq = square(ar)
    sq.square_cal()
elif x == "triangle" or x == "3":
    length = int(input("Enter the length of the triangle--"))
    height = int(input("Enter the height of the triangle--"))
    a = int(input("Enter the 1st side length--"))
    b = int(input("Enter the 2nd side length--"))
    c = int(input("Enter the 3rd side length--"))
    tri = triangle(length, height, a, b, c)
    tri.triangle_cal()
elif x == "rectangle" or x == "4":
    length = int(input("Enter the length of the rectangle--"))
    width = int(input("Enter the width of the rectangle--"))
    rec = rectangle(length, width)
    rec.rectangle_cal()

else:
    print("enter the mentioned values")
#output
'''

        Calculation for area and circumference
        enter the shape you want 
           circle or 1
           square or 2
           triangle or 3
           rectangle or 4

Enter here ---1
Enter the radius--7
The area of the circle is 21.98
The Circumference  of the circle is 43.96
╒════════╤═════════════════╕
│   Area │   Circumference │
╞════════╪═════════════════╡
│  21.98 │           43.96 │
╘════════╧═════════════════╛
'''