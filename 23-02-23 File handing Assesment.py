# 1. WAP to read the content of file and count how many times letter 'a' comes in file

x = open("C:\\Users\\Gokul\\Documents\\practice.txt.txt", "rt")
y = x.read()
c = y.count("a") + y.count("A")
print("The number of 'a' present in the file is {}".format(c))
x.close()
print("--------------------------------------------------------------------------------------------------")
#2. WAP to read the content of file and display 'I' in place of 'E' while displaying the content of file all
#other characters should appear as it is.

with open("C:\\Users\\Gokul\\Documents\\practice.txt.txt", "r") as file:
    content = file.read()
    print(content.replace("E", "I"))
print("--------------------------------------------------------------------------------------------------")
# 3.  WAP to read the content of file and display how many upper case characters and digits are present.
up_count, dig_count = 0, 0
with open("C:\\Users\\Gokul\\Documents\\practice.txt.txt", "r") as file1:
    content1 = file1.read()
for i in content1:
    if i.isupper():
        up_count += 1
    elif i.isdigit():
        dig_count += 1
print("The count of uppercase is {} and digits is {}".format(up_count, dig_count))
print("--------------------------------------------------------------------------------------------------")

# 4. WAP to read the content of file and count how many vowels in it.
with open("C:\\Users\\Gokul\\Documents\\practice.txt.txt", "r") as file2:
    content2 = file2.read()
    Vowels = content2.count("a") + content2.count("A") + content2.count("e") + content2.count("E") + content2.count("i") + content2.count("I") + content2.count("o") + content2.count("O") + content2.count("u") + content2.count("U")
    print("The count of vowels are {}".format(Vowels))
print("--------------------------------------------------------------------------------------------------")

#5(a). Write a statement in Python to open text file NEWS. TXT so that new content can be written

with open("C:\\Users\\Gokul\\Documents\\NEWS.txt", "w") as file3:
    content3 = file3.write("Hello this is News channel")
    file3.close()

#5(b). Write a statement in Python to open text file NEWS. TXT so that existing content can be read
with open("C:\\Users\\Gokul\\Documents\\NEWS.txt", "r") as file4:
    print(file4.read())
    file4.close()

#5(c). Write a statement in Python to open text file NEWS. TXT so that new content can be written after
with open("C:\\Users\\Gokul\\Documents\\NEWS.txt", "a") as file5:
    content5 = file5.write(" \n Today the weather going to severe rain")
    file5.close()
print("--------------------------------------------------------------------------------------------------")

#6. Write a function ISTOUPCOUNT() in python to read the content of file WRITER.TXT, to count and
#display the occurance of IS, TO, UP.
with open("C:\\Users\\Gokul\\Documents\\writer.txt", "r") as file6:
    x = file6.read()
def ISTOUPCOUNT(x):
    counts = x.count("IS") + x.count("is") + x.count("TO") + x.count("to") + x.count("UP") + x.count("up")
    print("The count of IS TO UP is {}".format(counts))
file6.close()
ISTOUPCOUNT(x)

print("--------------------------------------------------------------------------------------------------")

''''7. Write a function COUNTAE() in python to read lines from text file WRITER. TX T, and display those
lines, which are starting either with A or starting with E. For example if the content of file is •
A CLEAN ENVIRONMENT IS NECESSARY FOR OUR GOOD HEALTH.
WE SHOULD CLEAN OUR ENVIRONMENT.
EDUCATIONAL INSTITUTE SHOULD TAKE THE LEAD
The function should display:
A CLEAN ENVIRONMENT IS NECESSARY FOR OUR GOOD HEALTH.
EDUCATIONAL INSTITUTE SHOULD TAKE THE LEAD'''
with open("C:\\Users\\Gokul\\Documents\\writer.txt", "r") as file7:
    y = file7.read()
def COUNTAE(y):
    count4 = 0
    if y.startswith(("A", "E", "e", "a")):
        count4 += 1
        print(count4)

COUNTAE(y)

