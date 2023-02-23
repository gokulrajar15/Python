# Read method
x = open("C:\\Users\\Gokul\\Desktop\\Material\\oops.txt", "r")
print(x.read())
x.close()
print("-----------------------------------------------------------")
# append method
y = open("C:\\Users\\Gokul\\Desktop\\Material\\oops.txt", "a")
app = y.write(" \nI love python")
y.close()
print("-----------------------------------------------------------")
z = open("C:\\Users\\Gokul\\Desktop\\Material\\oops.txt", "r")
print(z.read())
z.close()
print("-----------------------------end------------------------------")


#Using for loop string n number of name

n = open("C:\\Users\\Gokul\\Desktop\\Material\\Names.txt", "a")
while True:
    name = input("Enter the names")
    n.write(name)
    n.write("\n")
    if name == "Stop" or name == "stop":
        break
n.close()
g = open("C:\\Users\\Gokul\\Desktop\\Material\\Names.txt", "r")
print(g.read())
g.close()
