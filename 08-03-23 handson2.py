
class circle:
    def A_and_C_of_circle(self):
        a = 3.14 * (self.radius**2)
        c = 3.14 * (self.radius * 2 * 3.14)
        print("The area of circle is {}".format(a))
        print("The circumference of circle is {}".format(c))


class rectangle(circle):
    def A_and_C_of_rectangle(self):
        a = self.breath * self.width
        c = (2*self.breath) * (2*self.width)
        print("The area of rectangle is {}".format(a))
        print("The circumference of rectangle is {}".format(c))


class triangle(rectangle):
    def A_and_C_of_triangle(self):
        a = 0.5 * self.base * self.height
        print("The area of triangle is {}".format(a))


class main(triangle):
    def __init__(self, breath, width, height, base, radius):
        self.breath = breath
        self.width = width
        self.height = height
        self.base = base
        self.radius = radius

    def displayall(self):
        circle.A_and_C_of_circle(self)
        rectangle.A_and_C_of_rectangle(self)
        triangle.A_and_C_of_triangle(self)


cal = main(4, 5, 3, 7, 8)
cal.displayall()
