def add(number1,number2):
    try:
        print(number1+number2)
    except:
        print("An error has occured")

def division(num1,num2):
    try:
        print(num1/num2)
    except TypeError:
        print("The arguments must be integer numbers")
    except ZeroDivisionError:
        print("The second argument cannot be zero")

def open_file(file_name):
    try:
        file = open(file_name)
    except FileNotFoundError:
        print("The file was not foud")
    except:
        print("Unknown error")
    else:
        print("Opening successfull")
    finally:
        print("Execution has ended")

def infinite():
    num = 0
    while True:
        num += 1
        yield num
 
generator = infinite()

def mult_7():
    n = 0
    while True:
        n = n + 7
        yield n
generator7 = mult_7()

def message():
    x = "You have 3 lives left"
    yield x
    
    x = "You have 2 lives left"
    yield x
 
    x = "You have 1 live left"
    yield x
    
    x = "Game Over"
    yield x

lose_life = message()