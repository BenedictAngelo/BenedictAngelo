# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in
from math import e
# local
def func1():
    a = 1   
    print(a) # does not know function 'b'

def func2():
    b = 2   
    print(b) # does not know function 'a'

func1()
func2()

# enclosed

def func3():
    x = 1   
    def func4():
        print(x) # does not know function 'a'

func3()

# global

def func5():
    print(z)

def func6():
    print(z)

z = 20

func5()
func6()

# import

def func7():
    print(e)

func7()
