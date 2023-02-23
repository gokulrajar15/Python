# 1. WAP to read the content of file and count how many times letter 'a' comes in file

x = open("C:\\Users\\Gokul\\Documents\\practice.txt.txt", "rt")
y = x.read()
count = 0
for i in y:
    if i == "a" or "A":
        count += 1
print("The number of 'a' present in the file is {}".format(count))
x.close()

#2. WAP to read the content of file and display 'I' in place of 'E' while displaying the content of file all
#other characters should appear as it is.

with open("C:\\Users\\Gokul\\Documents\\practice.txt.txt", "r") as file:
    content = file.read()
    print(content.replace("E", "I"))
