
#----------------------------------------------------------------------------------------------------------------
#1 python programme for numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
def divisible(n, m):
    div_list = []
    for i in range(n, m+1):
        if i % 7 == 0 and i % 5 == 0:
            div_list.append(i)
    print("The numbers that are divisible by 7 and multiple by 5 is {}".format(div_list))



# 2.Write a Python program to convert temperatures to and from Celsius, Fahrenheit.
# [ Formula : For fahrenheit F = (9/5 × C) + 32, celsius C = 5/9 x (F-32)  ]
# Expected Output:
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius
def degree_conversion():
    num = input("enter the number, like 45F or 60C")
    if num[-1] == 'F':
        temp_f = int(num[:-1])
        c = 0.55 * (temp_f - 32)
        print("The temperature in Fahrenheit {}°is converted into CELSIUS(c°) is {}°".format(temp_f, int(c)))
    elif num[-1] == 'C':
        temp_c = int(num[:-1])
        F = (1.8 * temp_c + 32)
        print("The temperature in celsius {}°is converted into FAHRENHEIT(F°) is {}°".format(temp_c, int(F)))
    else:
        print("Enter the correct formate, for ex : 45F or 60C")


#Write a Python program to guess a number between 1 and 9.
import random


def guess_the_number():
    count = 0
    x = random.randint(1, 10)
    while True:
        num = int(input("Guess the number"))
        count += 1
        if num == x:
            print("Congrats you get it")
            print("You got it finally after {} times".format(count))
            break
        elif num != x:
            print("Common dood guess again")


# 4 .Write a Python program to construct the following pattern, using a nested for loop.
def pattern():
    for i in range(1, 6):
        print("* " * i)
        print('')
    for j in range(5, 0, -1):
        print("* " * j)
        print('')


# 5 .Write a Python program that accepts a word from the user and reverse it

def reverse_the_string():
    name = input("Enter the string do you want reverse for eg: 'Gokul' ")
    le = len(name)
    x = name[-1:-le-1:-1]
    print(x)
#6 . code for counting even and odd number


def count_odd_and_even():
    x = int(input("Enter the range you want, (for eg : 23) - "))
    even = []
    odd = [1]
    for i in range(2, x):
        if i % 2 == 0:
            even.append(i)
        elif i % 2 != 0:
            odd.append(i)
    print("The even numbers are {}".format(even))
    print("The odd numbers are {}".format(odd))


# calculate simple interst
def simple_interst():
    P = int(input("Enter the amount you borrowed in bank for eg : 1000 (1000 rupees) ="))
    R = int(input("what was interest in your bank for eg : 5 (5% interest) ="))
    T = int(input("enter the year for interest for eg: 1 (1 Year) ="))
    SI = (P * R * T)/100
    Total_amount = P + SI
    print("The Interest Rate was {} rupees".format(int(SI)))
    print("The Total amount you need pay {} rupees".format(int(Total_amount)))


# 8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.


def skip_3_and_6():
    skip_list = []
    for i in range(0, 7):
        if i == 3 or i == 6:
            continue
        else:
            skip_list.append(i)
    print("The numbers after skipping 3 and 6 are {}".format(skip_list))

# 9 fibonacci series
def fibonacci_serise():
    j = int(input(" enter the range of fibonacci series you want = "))
    fibo = []
    for i in range(0, j):
        if i == 0 or i == 1:
            fibo.append(i)
        elif i > 1:
            v = fibo[-1] + fibo[-2]
            fibo.append(v)
    print("The fibonaccci is {}".format(fibo))


# 10.Write a Python program which iterates the integers from 1 to 50.
def fizz_buzz():
    for i in range(1, 50):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizz Buzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# 1 question
divisible(1500, 2700)
print("-----------------------------------**************__________________________________________________")
# 2 question
degree_conversion()
print("-----------------------------------**************__________________________________________________")
# 3 question
guess_the_number()
print("-----------------------------------**************__________________________________________________")
# 4 question
pattern()
print("-----------------------------------**************__________________________________________________")
# 5 question
reverse_the_string()
print("-----------------------------------**************__________________________________________________")
# 6 question
count_odd_and_even()
print("-----------------------------------**************__________________________________________________")
# 7 question
simple_interst()
print("-----------------------------------**************__________________________________________________")
# 8 question
skip_3_and_6()
print("-----------------------------------**************__________________________________________________")
# 9 question
fibonacci_serise()
print("-----------------------------------**************__________________________________________________")
# 10 question
fizz_buzz()
