from random import *

name = "Mike"
def welcome():
    print(f"¡Welcome {name}!")
welcome()

number = 25
def square():
    print(number ** 2)
square()

def exponentiation(number2, number3):
    power = number2 ** number3
    return power
result = exponentiation(2, 3)
print(result)

def usd_to_eur(dollars):
    change = round(dollars * 0.90)
    return change
money = usd_to_eur(100)
print(money)

def reverse_word(word):
    return word[::-1]
print(reverse_word("Python"))

numbers_list = sample(range(-100, 100), 2)
def positives(numbers_list):
    for n in numbers_list:
        if n < 0:
            return False
        else:
            pass
    return True
print(positives(numbers_list))

numbers_list2 = sample(range(-100, 2000), 5)
def add_between_0_1000(numbers_list2):
    number_add = 0
    for n in numbers_list2:
        if n in range(1, 1000):
            number_add += n
    return(number_add)
print(add_between_0_1000(numbers_list2))

numbers_list3 = sample(range(1, 100), 10)
def even_numbers(numbers_list3):
    counter = 0
    for n in numbers_list3:
        if n % 2 == 0:
            counter += 1
    return(counter)
print(even_numbers(numbers_list3))

def throw_dice():
    return randint(1,6), randint(1,6)
def play():
    dice1, dice2 = throw_dice()
    result = dice1 + dice2
    if result <= 6:
        print(f"The result is {result} very unlucky")
    elif result > 6 and result < 10:
        print(f"The result is {result} it's not a bad play")
    else:
        print(f"The result is {result} seems like a winning play")
play()

my_list = choices(range(1, 10), k = 14)
def no_dupes_list(ndlist):
    no_d_list = list(set(ndlist))
    biggest_number = max(no_d_list)
    no_d_list.remove(biggest_number)
    return no_d_list
def average():
    avg = 0
    list_count = len(no_dupes_list(my_list))
    for n in no_dupes_list(my_list):
        avg = avg + n
    avg = avg / list_count
    return round(avg, 2)
print(average())

def add_no_sign(*args):
    total = 0
    for arg in args: 
        if arg < 0:
            arg = arg * 2
            total = total + arg
        else:
            total = total + arg
    return total
print(add_no_sign(2, 4, 6, 2, 7, 2, 8, 4, 7, 2))

def name_numbers(name, *args):
    return print(f"{name} the sum of your numbers is {sum(args)}")
name_numbers("Jane", 1, 2, 2, 5, 6, 2, 7)

def describe(name, **kwargs):
    print(f"Physic details of {name}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    return
describe("Jane", eye_color="blue", hair_color="blonde", height="170cm")
