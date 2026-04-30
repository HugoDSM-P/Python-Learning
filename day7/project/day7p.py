class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Client(Person):
    def __init__(self, name, surname, account_number, balance=0):
        super().__init__(name, surname)
        self.account_number = account_number
        self.balance = balance

    def __str__(self):
        return (
            f"\nClient: {self.name} {self.surname}"
            f"\nAccount Number: {self.account_number}"
            f"\nBalance: {self.balance} €\n"
        )

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful. New balance: {self.balance} €")
        else:
            print("Amount must be positive")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal successful. New balance: {self.balance} €")
        else:
            print("Insufficient funds")


name = input("Enter your name: ")
surname = input("Enter your surname: ")
account_number = input("Enter your account number: ")

client = Client(name, surname, account_number)

while True:
    print("""
--- MENU ---
1. Deposit
2. Withdraw
3. Show client data
4. Exit
""")

    option = input("Choose an option: ")

    if option == "1":
        try:
            amount = float(input("Amount to deposit: "))
            client.deposit(amount)
        except ValueError:
            print("Please enter a valid number")

    elif option == "2":
        try:
            amount = float(input("Amount to withdraw: "))
            client.withdraw(amount)
        except ValueError:
            print("Please enter a valid number")

    elif option == "3":
        print(client)

    elif option == "4":
        print("!Goodbye!")
        break

    else:
        print("Invalid option")