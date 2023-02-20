def SI():
    try:
        x = int(input("Enter the amount you bought in bank, for ex : 150000 "))
        y = int(input("Enter the interst rate, for ex : 7 "))
        z = int(input("how many year, for ex : 2 "))
    except ValueError as v:
        print("'Enter the integer only' {}".format(v))
    else:
        a = (x * y * z)/100
        print("Your simple interst is {}".format(a))
        print("Your Total amount was {}".format(x + a))
    finally:
        print("Simple interst completed")

    print("-------------------------------------------------------------------------------------------------------------")


def CI():
    try:
        principle = int(input("Enter the amount you bought in bank "))
        interst = int(input("Enter the interst rate "))
        years = int(input("how many year "))
        n = int(input("Number of times interst is compound per year "))
    except ValueError as v:
        print("'Enter the integer only' {}".format(v))
    else:
        A = principle * (1 + (interst/n)**(n*years))
        ci = A - principle
        print("Your compound interst is {}".format(ci))
    finally:
        print("Compound interst completed")


def interst():
    print('''What type of interst do you want to find 
            1 . Simple interst(SI)
            2 . Compound interst(CI) 
    ''')
    i = input("Enter type you want 1 or 2 ")
    if i == "si" or i == "SI" or i == '1':
        SI()
    elif i == "ci" or i == "CI" or i == '2':
        CI()



def div_error():
    print("-----------------------------Zero division error---------------------------------------- ")
    try:
        a = int(input("Enter the 1st value "))
        b = int(input("Enter the 2st value "))
        x = a/b
    except ValueError as v:
        print("Enter the Number only {}".format(v))
    except ZeroDivisionError as z:
        print("Its not divisible by zero only {}".format(z))
    else:
        print(x)
    finally:
        print("Division completed")


interst()
div_error()
