def tuples():
    t = ("Gokul", 23, True, 34.76, 'd', False, "Raja", 75443, "Data", False)
    #       0      1    2     3     4     5      6        7      8       9        normal index
    #     -10     -9   -8    -7    -6    -5     -4       -3     -2      -1        Reverse index
    print("The first 5 elements are {}".format(t[:5]))
    print("The last 5 elements are {}".format(t[-5:]))
    print("The 4 elements in 3rd to 7th are {}".format(t[3:7]))
    print("-----------------------------for loop------------------------------")
    for i in t:
        print(i)
    print("-----------------------------Slicing------------------------------")
    print(t[:])

    print("The tuple in reverse order is {}".format(t[-1::-1]))
    print("The last four elements are {}".format(t[-4:]))
    print("The element 2nd from last to and 5th from last is {}".format(t[-1:-6:-1]))
    print("The element 8th to 5th is {}".format(t[-2:-7:-1]))


def lists():
    L = ["Data", 23, False, "Raja", 75443, True, 34.76, 'd', "Gokul", False]
    #       0      1    2     3     4     5      6        7      8       9        normal index
    #     -10     -9   -8    -7    -6    -5     -4       -3     -2      -1        Reverse index
    print("The first 5 elements are {}".format(L[:5]))
    print("The last 5 elements are {}".format(L[-5:]))
    print("The elements from 3rd position to 7th position is {}".format(L[3:8]))
    print("-----------------------------for loop------------------------------")
    for i in L:
        print(i)
    print("-----------------------------Slicing------------------------------")
    print(L[:])
    print("The elements in the reverse order {}".format(L[-1::-1]))
    print("The element from 2nd from last to 5th from last is {}".format(L[-2:-6:-1]))
    print("The element 8th to 5th is {}".format(L[-2:-6:-1]))
    #11
    if "Gokul" in L:
        print("Yes , Gokul is vailable in list")
    else:
        print("no, its not present")
    #12
    L3 = [True, 99.99, 234, "Software", "fbi"]
    # 13
    L2 = (L.copy()) * 5
    print(L2)
    #14
    list_merge = L + L2
    print(list_merge)
    # 15
    L4 = L.copy() * 3
    print(L4)


print(
    "*****************************************************************  Tuples  *****************************************************************")
tuples()
print(
    "*****************************************************************  List  *****************************************************************")
lists()
