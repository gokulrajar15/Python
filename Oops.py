class main:
    def collect(self):
        global l, w, r, h, ba, a, b, c
        l = int(input('Enter length of rectangle value:'))
        w = int(input('Enter width of rectangle value:'))
        r = int(input('Enter radius of circle value:'))
        h = int(input('Enter height of triangle value:'))
        ba = int(input('Enter Base of triangle value:'))
        a = int(input('Enter side1 of triangle value:'))
        b = int(input('Enter side2 of triangle value:'))
        c = int(input('Enter side3 of triangle value:'))
        print('\n')


class child1(main):

    def area_circle(self):
        area = 3.14 * r * r
        print('Area of the circle:', area)

    def peri_circle(self):
        pm = 2 * (22 / 7) * r
        print('Perimeter of circle:', pm, '\n')


class child2(main):
    def area_rect(self):
        area = l * w
        print('Area of the rectangle is:', area)

    def peri_rect(self):
        pm = 2 * (l + w)
        print('Perimeter of the rectangle is:', pm, '\n')


class child3(main):
    def area_triangle(self):
        area = (h * ba) / 2
        print('Area  of the triangel:', area)

    def peri_triangle(self):
        pm = a + b + c
        print('perimeter  of the triangel:', pm, '\n')


class child4(child1, child2, child3):
    def all_methods(self):
        main.collect(self)
        child1.area_circle(self)
        child1.peri_circle(self)
        child2.area_rect(self)
        child2.peri_rect(self)
        child3.area_triangle(self)
        child3.peri_triangle(self)


obj = child4()
obj.all_methods()