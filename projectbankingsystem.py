#BANKING SYSTEM
from datetime import datetime
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.transactions = []

    def login(self):
        print("\nWelcome to the kdc Bank!")
        print("\nPlease Login")
        userid = input("Enter your UserID:")
        if userid == "spsuchiraj":
            password = input("Enter your password:")
            if password == "334567":
                print("Login successful,Welcome Suchithra")
                self.display_balance()
            else:
                print("Incorrect password. Login failed")

    def deposit(self):
        amount = float(input("Enter the amount to deposit: $"))
        self.balance += amount
        transaction = f"Deposit: +${amount} | {self._get_current_datetime()}"
        self.transactions.append(transaction)
        print(f"Amount ${amount} deposited successfully.")
        self.display_balance()

    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: $"))
        if amount > self.balance:
            print("Insufficient funds. Withdrawal failed.")
            self.insufficient_balance()
        else:
            self.balance -= amount
            transaction = f"Withdrawal: -${amount} | {self._get_current_datetime()}"
            self.transactions.append(transaction)
            print(f"Amount ${amount} withdrawn successfully.")
            self.display_balance()

    def insufficient_balance(self):
        print("Additional options:")
        print("1. Deposit more funds\n2. Go back to main menu")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            self.deposit()
        elif choice == 2:
            print("Returning to the main menu.")
        else:
            print("Invalid choice. Returning to the main menu.")

    def display_balance(self):
        print(f"Current balance: ${self.balance}")

    def generate_statement(self):
        print("\nBank Statement:")
        for transacation in self.transactions:
            print(transacation)
    def _get_current_datetime(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Main program loop
account = BankAccount()
while True:
    print("\n1. Login\n2. Deposit\n3. Withdraw\n4.Balance Enquiry \n5.Bank Statement\n6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        account.login()
    elif choice == 2:
        account.deposit()
    elif choice == 3:
        account.withdraw()
    elif choice == 4:
        account.display_balance()
    elif choice == 5:
        print("Thank you for using the banking system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")


        #THAMK YOU