from tabulate import tabulate


class calculation:
    def A_and_C_of_all(self):
        ca = 3.14 * (self.radius**2)
        cc = 3.14 * (self.radius * 2 * 3.14)
        ra = self.breath * self.width
        rc = (2*self.breath) * (2*self.width)
        ta = 0.5 * self.base * self.height
        tc = self.st_length*self.nd_length*self.rd_length
        table = [["Type", 'area', 'circumference'],
                 ["Circle",ca, cc],
                 ["Rectangle",ra, rc],
                 ["Triangle",ta, tc]
                 ]
        print(tabulate(table, tablefmt="fancy_grid"))

    def __init__(self, breath, width, height, base, st_length, nd_length, rd_length ,radius):
        self.breath = breath
        self.width = width
        self.height = height
        self.base = base
        self.st_length = st_length
        self.nd_length = nd_length
        self.rd_length = rd_length
        self.radius = radius


cal = calculation(6,8,3,4,9,4,6,5)
cal.A_and_C_of_all()