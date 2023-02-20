
def area_of_shapes():
    print("Area of different shapes using function")
    while True:
        name = input('''Enter the type of shape you want 
                     type 1 or SQUARE
                     type 2 or RECTANGLE
                     type 3 or TRIANGLE
                     type 4 or  CIRCLE''')
        name = name.lower()
        if name == '1'or name == "square":
            le = int(input("enter the length of square"))
            print("The area of square is {}".format(le**2))
        elif name == '2' or name == "rectangle":
            l = int(input("enter the length of rectangle"))
            w = int(input("enter the width of rectangle"))
            print("The area of rectangle is {}".format(l*w))
        elif name == '3' or name == "triangle":
            b = int(input("enter the base of triangle"))
            h = int(input("enter the height of triangle"))
            print("The area of triangle is {}".format(0.5 * (b*h)))
        elif name == '4' or name == "circle":
            r = int(input("enter the radius of circle"))
            print("The area of circle is {}".format(3.141 * r))

        print("do you want continue y/n")
        c = input("Enter y/n")
        if c == "n" or c == "N":
            break


def unit():
    Unit = int(input("Enter the unit you consumed"))
    if Unit < 100:
        print(" you dont have current bill")
    elif Unit < 501:
        a = (Unit - 100) * 8
        print(" you current bill is Rs:{}".format(a))
    elif Unit < 1001:
        b = ((Unit - 500) * 10) + (400 * 8)
        print(" you current bill is Rs:{}".format(b))
    elif Unit < 2001:
        c = (((Unit - 1000) * 15) + 8200)
        print(" you current bill is Rs:{}".format(c))
    elif Unit < 5001:
        d = (((Unit - 2000) * 20) + 23200)
        print(" you current bill is Rs:{}".format(d))
    elif Unit < 10001:
        e = (((Unit - 5000) * 25) + 83200)
        print(" you current bill is Rs:{}".format(e))
    elif Unit < 20001:
        f = (((Unit - 10000) * 50) + 208200)
        print(" you current bill is Rs:{}".format(f))
    elif Unit > 20000:
        g = (((Unit - 20000) * 75) + 708200)
        print(" you current bill is Rs:{}".format(g))



area_of_shapes()
print("----------------------------------------Electricity bill----------------------------------------------------")
unit()
