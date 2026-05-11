from tkinter import *
from tkinter import filedialog, messagebox
import random
import datetime

operator = ''

food_prices = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
drink_prices = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
dessert_prices = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


def click_button(number):
    global operator
    operator = operator + number
    calculator_display.delete(0, END)
    calculator_display.insert(END, operator)


def clear():
    global operator
    operator = ''
    calculator_display.delete(0, END)


def get_result():
    global operator
    result = str(eval(operator))
    calculator_display.delete(0, END)
    calculator_display.insert(0, result)
    operator = ''


def check_review():

    x = 0

    for c in food_boxes:

        if food_variables[x].get() == 1:

            food_boxes[x].config(state=NORMAL)

            if food_boxes[x].get() == '0':
                food_boxes[x].delete(0, END)

            food_boxes[x].focus()

        else:

            food_boxes[x].config(state=DISABLED)
            food_text[x].set('0')

        x += 1

    x = 0

    for c in drink_boxes:

        if drink_variables[x].get() == 1:

            drink_boxes[x].config(state=NORMAL)

            if drink_boxes[x].get() == '0':
                drink_boxes[x].delete(0, END)

            drink_boxes[x].focus()

        else:

            drink_boxes[x].config(state=DISABLED)
            drink_text[x].set('0')

        x += 1

    x = 0

    for c in dessert_boxes:

        if dessert_variables[x].get() == 1:

            dessert_boxes[x].config(state=NORMAL)

            if dessert_boxes[x].get() == '0':
                dessert_boxes[x].delete(0, END)

            dessert_boxes[x].focus()

        else:

            dessert_boxes[x].config(state=DISABLED)
            dessert_text[x].set('0')

        x += 1


def total():

    food_subtotal = 0

    p = 0

    for quantity in food_text:
        food_subtotal = food_subtotal + (float(quantity.get()) * food_prices[p])
        p += 1

    drink_subtotal = 0

    p = 0

    for quantity in drink_text:
        drink_subtotal = drink_subtotal + (float(quantity.get()) * drink_prices[p])
        p += 1

    dessert_subtotal = 0

    p = 0

    for quantity in dessert_text:
        dessert_subtotal = dessert_subtotal + (float(quantity.get()) * dessert_prices[p])
        p += 1

    subtotal = food_subtotal + drink_subtotal + dessert_subtotal
    taxes = subtotal * 0.07
    total_cost = subtotal + taxes

    food_cost_var.set(f'$ {round(food_subtotal, 2)}')
    drink_cost_var.set(f'$ {round(drink_subtotal, 2)}')
    dessert_cost_var.set(f'$ {round(dessert_subtotal, 2)}')
    subtotal_var.set(f'$ {round(subtotal, 2)}')
    taxes_var.set(f'$ {round(taxes, 2)}')
    total_var.set(f'$ {round(total_cost, 2)}')


def receipt():

    receipt_text.delete(1.0, END)

    receipt_number = f'N# - {random.randint(1000, 9999)}'

    date = datetime.datetime.now()

    receipt_date = f'{date.day}/{date.month}/{date.year} - {date.hour}:{date.minute}'

    receipt_text.insert(END, f'Data:\t{receipt_number}\t\t{receipt_date}\n')
    receipt_text.insert(END, f'*' * 47 + '\n')
    receipt_text.insert(END, 'Items\t\tQty\tItem Cost\n')
    receipt_text.insert(END, f'-' * 54 + '\n')

    x = 0

    for food in food_text:

        if food.get() != '0':

            receipt_text.insert(
                END,
                f'{food_list[x]}\t\t{food.get()}\t'
                f'$ {int(food.get()) * food_prices[x]}\n'
            )

        x += 1

    x = 0

    for drink in drink_text:

        if drink.get() != '0':

            receipt_text.insert(
                END,
                f'{drink_list[x]}\t\t{drink.get()}\t'
                f'$ {int(drink.get()) * drink_prices[x]}\n'
            )

        x += 1

    x = 0

    for dessert in dessert_text:

        if dessert.get() != '0':

            receipt_text.insert(
                END,
                f'{dessert_list[x]}\t\t{dessert.get()}\t'
                f'$ {int(dessert.get()) * dessert_prices[x]}\n'
            )

        x += 1

    receipt_text.insert(END, f'-' * 54 + '\n')
    receipt_text.insert(END, f' Food Cost: \t\t\t{food_cost_var.get()}\n')
    receipt_text.insert(END, f' Drink Cost: \t\t\t{drink_cost_var.get()}\n')
    receipt_text.insert(END, f' Dessert Cost: \t\t\t{dessert_cost_var.get()}\n')
    receipt_text.insert(END, f'-' * 54 + '\n')
    receipt_text.insert(END, f' Subtotal: \t\t\t{subtotal_var.get()}\n')
    receipt_text.insert(END, f' Taxes: \t\t\t{taxes_var.get()}\n')
    receipt_text.insert(END, f' Total: \t\t\t{total_var.get()}\n')
    receipt_text.insert(END, f'*' * 47 + '\n')
    receipt_text.insert(END, 'Thank you for your visit')


def save_receipt():

    receipt_info = receipt_text.get(1.0, END)

    file = filedialog.asksaveasfile(
        mode='w',
        defaultextension='.txt'
    )

    file.write(receipt_info)
    file.close()

    messagebox.showinfo('Information', 'Your receipt has been saved')


def reset():

    receipt_text.delete(0.1, END)

    for text in food_text:
        text.set('0')

    for text in drink_text:
        text.set('0')

    for text in dessert_text:
        text.set('0')

    for box in food_boxes:
        box.config(state=DISABLED)

    for box in drink_boxes:
        box.config(state=DISABLED)

    for box in dessert_boxes:
        box.config(state=DISABLED)

    for v in food_variables:
        v.set(0)

    for v in drink_variables:
        v.set(0)

    for v in dessert_variables:
        v.set(0)

    food_cost_var.set('')
    drink_cost_var.set('')
    dessert_cost_var.set('')
    subtotal_var.set('')
    taxes_var.set('')
    total_var.set('')

    calculator_display.delete(0, END)

    global operator
    operator = ''


app = Tk()

app.geometry('1020x630+0+0')

app.resizable(0, 0)

app.title("Restaurant Billing System")

app.config(bg='burlywood')

top_panel = Frame(app, bd=1, relief=FLAT)
top_panel.pack(side=TOP)

title_label = Label(
    top_panel,
    text='Billing System',
    fg='azure4',
    font=('Dosis', 32, 'bold'),
    bg='burlywood',
    width=20
)

title_label.grid(row=0, column=0)

left_panel = Frame(app, bd=1, relief=FLAT)
left_panel.pack(side=LEFT)

cost_panel = Frame(left_panel, bd=1, relief=FLAT, bg='azure4', padx=10)
cost_panel.pack(side=BOTTOM)

food_panel = LabelFrame(
    left_panel,
    text='Food',
    font=('Dosis', 12, 'bold'),
    bd=1,
    relief=FLAT,
    fg='azure4'
)

food_panel.pack(side=LEFT)

drink_panel = LabelFrame(
    left_panel,
    text='Drinks',
    font=('Dosis', 12, 'bold'),
    bd=1,
    relief=FLAT,
    fg='azure4'
)

drink_panel.pack(side=LEFT)

dessert_panel = LabelFrame(
    left_panel,
    text='Desserts',
    font=('Dosis', 12, 'bold'),
    bd=1,
    relief=FLAT,
    fg='azure4'
)

dessert_panel.pack(side=LEFT)

right_panel = Frame(app, bd=1, relief=FLAT)
right_panel.pack(side=RIGHT)

calculator_panel = Frame(right_panel, bd=1, relief=FLAT, bg='burlywood')
calculator_panel.pack()

receipt_panel = Frame(right_panel, bd=1, relief=FLAT, bg='burlywood')
receipt_panel.pack()

buttons_panel = Frame(right_panel, bd=1, relief=FLAT, bg='burlywood')
buttons_panel.pack()

food_list = [
    'Chicken',
    'Lamb',
    'Salmon',
    'Kebab',
    'Pizza',
    'Pork',
    'Beef',
    'Pasta'
]

drink_list = [
    'Water',
    'Juice',
    'Wine',
    'Beer',
    'Tea',
    'Coffee',
    'Sparkling Water',
    'CocaCola'
]

dessert_list = [
    'Ice Cream',
    'Apple Pie',
    'Brownies',
    'Fruits',
    'Souffle',
    'Nutella',
    'Carrot Cake',
    'Mousse'
]

food_variables = []
food_boxes = []
food_text = []

counter = 0

for food in food_list:

    food_variables.append('')
    food_variables[counter] = IntVar()

    food = Checkbutton(
        food_panel,
        text=food.title(),
        font=('Dosis', 12, 'bold'),
        onvalue=1,
        offvalue=0,
        variable=food_variables[counter],
        command=check_review
    )

    food.grid(row=counter, column=0, sticky=W)

    food_boxes.append('')
    food_text.append('')

    food_text[counter] = StringVar()
    food_text[counter].set('0')

    food_boxes[counter] = Entry(
        food_panel,
        font=('Dosis', 11, 'bold'),
        bd=1,
        width=4,
        state=DISABLED,
        textvariable=food_text[counter]
    )

    food_boxes[counter].grid(row=counter, column=1)

    counter += 1

drink_variables = []
drink_boxes = []
drink_text = []

counter = 0

for drink in drink_list:

    drink_variables.append('')
    drink_variables[counter] = IntVar()

    drink = Checkbutton(
        drink_panel,
        text=drink.title(),
        font=('Dosis', 12, 'bold'),
        onvalue=1,
        offvalue=0,
        variable=drink_variables[counter],
        command=check_review
    )

    drink.grid(row=counter, column=0, sticky=W)

    drink_boxes.append('')
    drink_text.append('')

    drink_text[counter] = StringVar()
    drink_text[counter].set('0')

    drink_boxes[counter] = Entry(
        drink_panel,
        font=('Dosis', 11, 'bold'),
        bd=1,
        width=4,
        state=DISABLED,
        textvariable=drink_text[counter]
    )

    drink_boxes[counter].grid(row=counter, column=1)

    counter += 1

dessert_variables = []
dessert_boxes = []
dessert_text = []

counter = 0

for dessert in dessert_list:

    dessert_variables.append('')
    dessert_variables[counter] = IntVar()

    dessert = Checkbutton(
        dessert_panel,
        text=dessert.title(),
        font=('Dosis', 12, 'bold'),
        onvalue=1,
        offvalue=0,
        variable=dessert_variables[counter],
        command=check_review
    )

    dessert.grid(row=counter, column=0, sticky=W)

    dessert_boxes.append('')
    dessert_text.append('')

    dessert_text[counter] = StringVar()
    dessert_text[counter].set('0')

    dessert_boxes[counter] = Entry(
        dessert_panel,
        font=('Dosis', 11, 'bold'),
        bd=1,
        width=4,
        state=DISABLED,
        textvariable=dessert_text[counter]
    )

    dessert_boxes[counter].grid(row=counter, column=1)

    counter += 1

food_cost_var = StringVar()
drink_cost_var = StringVar()
dessert_cost_var = StringVar()
subtotal_var = StringVar()
taxes_var = StringVar()
total_var = StringVar()

labels = [
    ('Food Cost', food_cost_var, 0, 0),
    ('Drink Cost', drink_cost_var, 1, 0),
    ('Dessert Cost', dessert_cost_var, 2, 0),
    ('Subtotal', subtotal_var, 0, 2),
    ('Taxes', taxes_var, 1, 2),
    ('Total', total_var, 2, 2)
]

for text, variable, row, column in labels:

    label = Label(
        cost_panel,
        text=text,
        font=('Dosis', 10, 'bold'),
        bg='azure4',
        fg='white'
    )

    label.grid(row=row, column=column)

    entry = Entry(
        cost_panel,
        font=('Dosis', 10, 'bold'),
        bd=1,
        width=8,
        state='readonly',
        textvariable=variable
    )

    entry.grid(row=row, column=column + 1, padx=5)

buttons = ['Total', 'Receipt', 'Save', 'Reset']
created_buttons = []

columns = 0

for button in buttons:

    button = Button(
        buttons_panel,
        text=button,
        font=('Dosis', 10, 'bold'),
        fg='white',
        bg='azure4',
        bd=1,
        width=7
    )

    created_buttons.append(button)

    button.grid(row=0, column=columns, padx=2)

    columns += 1

created_buttons[0].config(command=total)
created_buttons[1].config(command=receipt)
created_buttons[2].config(command=save_receipt)
created_buttons[3].config(command=reset)

receipt_text = Text(
    receipt_panel,
    font=('Dosis', 10, 'bold'),
    bd=1,
    width=42,
    height=10
)

receipt_text.grid(row=0, column=0)

calculator_display = Entry(
    calculator_panel,
    font=('Dosis', 14, 'bold'),
    width=28,
    bd=1
)

calculator_display.grid(
    row=0,
    column=0,
    columnspan=4
)

calculator_buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    'R', 'C', '0', '/'
]

saved_buttons = []

row = 1
column = 0

for button in calculator_buttons:

    button = Button(
        calculator_panel,
        text=button.title(),
        font=('Dosis', 12, 'bold'),
        fg='white',
        bg='azure4',
        bd=1,
        width=5
    )

    saved_buttons.append(button)

    button.grid(row=row, column=column)

    if column == 3:
        row += 1

    column += 1

    if column == 4:
        column = 0

saved_buttons[0].config(command=lambda: click_button('7'))
saved_buttons[1].config(command=lambda: click_button('8'))
saved_buttons[2].config(command=lambda: click_button('9'))
saved_buttons[3].config(command=lambda: click_button('+'))
saved_buttons[4].config(command=lambda: click_button('4'))
saved_buttons[5].config(command=lambda: click_button('5'))
saved_buttons[6].config(command=lambda: click_button('6'))
saved_buttons[7].config(command=lambda: click_button('-'))
saved_buttons[8].config(command=lambda: click_button('1'))
saved_buttons[9].config(command=lambda: click_button('2'))
saved_buttons[10].config(command=lambda: click_button('3'))
saved_buttons[11].config(command=lambda: click_button('*'))
saved_buttons[12].config(command=get_result)
saved_buttons[13].config(command=clear)
saved_buttons[14].config(command=lambda: click_button('0'))
saved_buttons[15].config(command=lambda: click_button('/'))

app.mainloop()