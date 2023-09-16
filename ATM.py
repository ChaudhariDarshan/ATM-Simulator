class ATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, pin, balance=0):
        self.accounts[account_number] = {'pin': pin, 'balance': balance}

    def validate_account(self, account_number, pin):
        if account_number in self.accounts and self.accounts[account_number]['pin'] == pin:
            return True
        else:
            return False

    def check_balance(self, account_number):
        return self.accounts[account_number]['balance']

    def deposit(self, account_number, amount):
        self.accounts[account_number]['balance'] += amount
        return self.accounts[account_number]['balance']

    def withdraw(self, account_number, amount):
        if amount <= self.accounts[account_number]['balance']:
            self.accounts[account_number]['balance'] -= amount
            return self.accounts[account_number]['balance']
        else:
            return "Insufficient funds"

def main():
    atm = ATM()

    # Create some sample accounts
    atm.create_account("123456", "1234", 1000)
    atm.create_account("987654", "5678", 500)

    while True:
        print("Welcome to the ATM Simulator")
        account_number = input("Enter your account number: ")
        pin = input("Enter your PIN: ")

        if atm.validate_account(account_number, pin):
            print("Login successful.")
            while True:
                print("\nChoose an option:")
                print("1. Check Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Logout")

                choice = input("Enter your choice: ")

                if choice == '1':
                    print(f"Your balance is ${atm.check_balance(account_number)}")
                elif choice == '2':
                    amount = float(input("Enter the deposit amount: $"))
                    new_balance = atm.deposit(account_number, amount)
                    print(f"Deposited ${amount}. Your new balance is ${new_balance}")
                elif choice == '3':
                    amount = float(input("Enter the withdrawal amount: $"))
                    result = atm.withdraw(account_number, amount)
                    if result == "Insufficient funds":
                        print("Insufficient funds.")
                    else:
                        print(f"Withdrew ${amount}. Your new balance is ${result}")
                elif choice == '4':
                    print("Logged out.")
                    break
                else:
                    print("Invalid choice. Please try again.")

        else:
            print("Invalid account number or PIN. Please try again.")

if __name__ == "__main__":
    main()
