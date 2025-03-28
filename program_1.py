#Programmer: Timothy Pickering
#Date: 3/25/25
#Title: Basic bank account

class BankAccount:
    #Initialize the account with a starting balance
    def __init__(self, balance=0.0):
        self.__balance = balance  #Attribute to store balance

    def deposit(self, amount):
        #Add money to the account
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        #Withdraw money from the account if funds are available
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}")
        elif amount > self.__balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        #Return the current balance
        return self.__balance

#Main function to interact with the user
def main():
    #Create an account with user-defined balance
    account = BankAccount(float(input("Enter initial balance: ")))

    while True:
        print(f"\nCurrent balance: ${account.get_balance():.2f}")
        try:
            amount = float(input("Enter amount to deposit (positive), withdraw (negative), or 0 to check balance: "))
            if amount > 0:
                account.deposit(amount)
            elif amount < 0:
                #Convert negative input to positive for withdrawal
                account.withdraw(abs(amount))
            else:
                print(f"Your current balance is: ${account.get_balance():.2f}")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

        #Ask if the user wants to continue
        choice = input("Do you want to make another transaction? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("Thank you for banking with us!")
            break

#Run the program
if __name__ == "__main__":
    main()