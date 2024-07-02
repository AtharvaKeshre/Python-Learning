
def greet(fx):
    def modify(*args,**kwargs):
        print("Good Morning")
        fx(*args,**kwargs)
        print("Thanks for using this program")
    return modify # here I am returning the object withour executing it so that I can execute it later

# @greet 
def hello():
    print("Hello, world!")

def add(a,b):
    return print(a+b)

# greet(hello)() # this is used to manually run a decorator
greet(add)(1,2) 