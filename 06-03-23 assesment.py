class Area_And_Circumference:

    def circle(self, radius_of_circle):
        area_of_circle = 3.14 * (radius_of_circle**2)
        circumference_of_circle = 2 * 3.14 * radius_of_circle
        print("The are of circle is {} and circumference is {}".format(area_of_circle, circumference_of_circle))

    def square(self, length):
        area_of_square = length ** 2
        return area_of_square

    def triangle(self):
        height = int(input("Enter the height of the triangle"))
        breath = int(input("Enter the breath of the triangle"))
        a = int(input("Enter the 1st length of the triangle"))
        b = int(input("Enter the 2nd length of the triangle"))
        c = int(input("Enter the 3rd length of the triangle"))
        area_of_triangle = 0.5 * height * breath
        circumference_of_triangle = a + b + c
        print("The area of triangle is {} and circumference is {}".format(area_of_triangle, circumference_of_triangle))

    def rectangle(self):
        length = int(input("Enter the length of the rectangle"))
        width = int(input("Enter the width of the rectangle"))
        area_of_rectangle = length * width
        circumference_of_rectangle = length + width
        return area_of_rectangle, circumference_of_rectangle


circle = Area_And_Circumference()
circle.circle(7)

square = Area_And_Circumference()
x = square.square(10)
print("The area of square is {}".format(x))

triangle = Area_And_Circumference()
triangle.triangle()

rectangle = Area_And_Circumference()
y = rectangle.rectangle()
print("The area of rectangle  and circumference is {}".format(y))
