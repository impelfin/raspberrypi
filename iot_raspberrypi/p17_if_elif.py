while True:
    i = input("Input the number(q : Quit) : ")

    if (i == 'q'):
        break
    else:
        if int(i) > 0:
            print("This is positive")
        elif int(i) == 0:
            print("This is Zero")
        else:
            print("This is negative")

