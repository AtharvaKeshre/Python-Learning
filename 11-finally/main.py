a = input("Enter the number: ")
def table(a):
    print(f"Multiplication table of {a} is - ")
    try:
        for i in range(1, 11):
            print(f"{a} X {i} = {int(a)*i} ")
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        print("Thank you for using this program")

table(a)
print("End")

