while True:
    e = float(input("write your degree : "))

    if 100 >= e >= 90:
        if e >= 94:
            print("+a")
        else:
            print("a")
    elif 90 > e >= 80:
        if e >= 84:
            print("+b")
        else:
            print("b")
    elif 80 > e >= 70:
        if e >= 74:
            print("+c")
        else:
            print("c")
    elif 70 > e >= 60:
        if e >= 64:
            print("+d")
        else:
            print("d")
    elif 60 > e >= 50:
        if e >= 54:
            print("+e")
        else:
            print("e")
    elif e < 50:
        print("f")
    else:
        print("try again")