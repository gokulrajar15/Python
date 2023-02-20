#************************************************************************************while loop**************************************************************************************
#Natural numbers upto N reverse order
def rev_num(n):
# n is number of times to run
    i, rev_lst = 0, []
    while n != i:
        rev_lst.append(n)
        n -=  1
    print("The reverse number is {}".format(rev_lst))

# Fibonacci series
def fibo(z):
# z is number times to run
    fibo_list = [0]
    n = 1
    while n != z:
        if n == 1:
            fibo_list.append(n)
        elif n > 1:
            fibo_temp = fibo_list[-2] + fibo_list[-1]
            fibo_list.append(fibo_temp)
        n += 1
    print("The Fibonacci series is {}".format(fibo_list))


# factorial
def factorial(n):
    # here t is to store the n, because atlast n became 0 using decrement
    t = n
    factorial = 1
    while n != 0:
        factorial *= n
        n -= 1
    print("The factorial of {} is {}".format(t, factorial))
#palindrom
def palindrome(n):
    t = n
    x = len(str(n))
    temp = ""
    while True:
        if x == 0:
            break
        else:
            z = n % 10
            n = n//10
            temp = temp + str(z)
        x = x - 1
    Reversed_number = int(temp)
    if t == Reversed_number:
        print("enter number {} is palindrom ".format(t))
    elif t != Reversed_number:
        print("enter number {} is not a palindrom ".format(t))


# reverse the given number
def Reverse_the_Number(n):
    t = n
    x = len(str(n))
    temp = ""
    while True:
        if x == 0:
            break
        else:
            z = n % 10
            n = n//10
            temp = temp + str(z)
        x = x - 1
    Reversed_number = int(temp)
    print("The reversed number is {}".format(Reversed_number))
    
# Sum of given number

def sum_of_N_numbers():
    print("-----------------------------------------------------sum of n numbers-----------------------------------------------------------")
    sum = 0
    while True:
        n = int(input("Enter the number, Enter 0 to stop"))
        if n == 0:
            break
        else:
            sum += n
    print("The sum entered value is {}".format(sum))


rev_num(20)
fibo(10)
factorial(5)
palindrome(121)
Reverse_the_Number(12345)
sum_of_N_numbers()

#**************************************************************************************for loop***************************************************************************************
def reverse_n_natural_number(n):
    rev_list = []
    for i in range(n, 0, -1):
        rev_list.append(i)
    print("The natural numbers in reverse order is {} ".format(rev_list))

#----------------------------------------------------------------------------------------------------------------


def fibonacci(n):
    fibonacci_lst = []
    for i in range(0, n):
        if i == 0 or i == 1:
            fibonacci_lst.append(i)
        elif i > 1:
            x = fibonacci_lst[-1] + fibonacci_lst[-2]
            fibonacci_lst.append(x)
    print("The fibonacci series is {}".format(fibonacci_lst))

#----------------------------------------------------------------------------------------------------------------


def factorial(n):
    m = 1
    for i in range(1, n+1):
        m *= i
    print("The factorial of {} is {}".format(n, m))

#----------------------------------------------------------------------------------------------------------------


def sum_of_digits(n):
    t = n
    length = len(str(n))
    sum = 0
    for i in range(length):
        y = n % 10
        sum = sum + y
        n = n//10
    print("The sum of given value {} is {}".format(t, sum))

#----------------------------------------------------------------------------------------------------------------


def prime_number(num):
    pass

#----------------------------------------------------------------------------------------------------------------

def palindrome(n):
    t = n
    length = len(str(n))
    sum = ""
    for i in range(length):
        y = n % 10
        sum = sum + str(y)
        n = n//10
    if int(sum) == t:
        print("The {} is a palindrome".format(t))
    elif int(sum) != t:
        print("The given number {} is not palindrome".format(t))

#---------------------------------------------------------------------------------------------------------------


def reverse_the_number(n):
    length = len(str(n))
    sum = ""
    for i in range(length):
        y = n % 10
        sum = sum + str(y)
        n = n//10
    print("The reversed number is {}".format(int(sum)))


reverse_n_natural_number(10)
fibonacci(10)
factorial(5)
sum_of_digits(1234)
palindrome(121)
reverse_the_number(1234)

