x = int(input("Enter the value : "))

match x:
    case 1: print(x, " : The value of x is",x )
    case _: print("default")