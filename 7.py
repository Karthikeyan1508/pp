class BankAccount:
    def __init__(self, balance=0):
        self.balances = balance

    def withdraw(self, amount):
        if self.balances >= amount:
            self.balances -= amount
            print(f"{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def deposit(self, amount):
        self.balances += amount
        print(f"{amount} successfully deposited.")

    def balance(self):
        print(f"The balance is {self.balances}")

account = BankAccount(int(input("Enter the opening balance: ")))

loop_runner = True
while loop_runner:
    print("\nBank Account Operations")
    print("1. Withdraw\n2. Deposit\n3. Balance\n4. Exit")
    
    try:
        option = int(input("Choose an option: "))
        if option == 1:
            account.withdraw(int(input("Enter the amount: ")))
        elif option == 2:
            account.deposit(int(input("Enter the amount: ")))
        elif option == 3:
            account.balance()
        elif option == 4:
            loop_runner = False
            print("Exiting the application.")
        else:
            print("Invalid choice. Please select a valid option.")
    except ValueError:
        print("Please enter a valid number.")
