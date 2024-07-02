class C:
    def __init__(self) -> None:
        pass

    @staticmethod
    def add(a,b):
        return(a+b)

myInstance = C()
print(myInstance.add(1,3))

print(C.add(1,2))