number1 = int(input("Write a number: "))
number2 = int(input("Write another number: "))
if number1 > number2:
    print(f"{number1} is greater than {number2}")
elif number2 > number1:
    print(f"{number2} is greater than {number1}")
else:
    print(f"{number1} are {number2} equals")

age = 16
license = False

if age >= 18:
    if license == True:
        print("Congratulations, you can drive")
    else:
        print("You need a driving license")
else:
    print("You are too young to drive")

students = ["Karen", "Charles", "Elizabeth", "Johan", "Mike", "Thomas", "John"]
for name in students:
    print(f"Hello {name}")

number_list = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
even_add = 0
odd_add = 0
for number in number_list:
    if number % 2 == 0:
        even_add = even_add + number
    else:
        odd_add = odd_add + number
print(f"The odd numbers sum to {odd_add}")
print(f"The even numbers sum to {even_add}")

number_while = 50
while number_while > 0:
    if number_while % 5 == 0:
        print(number_while)
    number_while = number_while -1

number_list2 = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
for n in number_list2:
    if n < 0:
        break
    else:
        print(n)

number_list3 = range(1, 16)
square_add = 0
for n in number_list3:
    square_add = n * n
    print(square_add)

