from number_gen import text, fragrance, cosmetics, pharmacy

c = 1
fragrance_gen = fragrance(c)
cosmetics_gen = cosmetics(c)
pharmacy_gen = pharmacy(c)
option = ""

while option != "4":
    print('''
Option 1: Pharmacy
Option 2: Perfume
Option 3: Cosmetic
Option 4: Exit
''')
    option = input("Choose the area where you want to buy: ")
    print("")
    match option:
        case "1":
            text(pharmacy_gen)
        case "2":
            text(fragrance_gen)
        case "3":
            text(cosmetics_gen)
        case "4":
            break
        case _:
            print("Please choose a number between 1 and 4.")
if option == "4":
    print("Thanks for using our services.")