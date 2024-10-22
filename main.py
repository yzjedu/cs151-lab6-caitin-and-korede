# Programmers:  Caitlin Burns and Korede Oni
# Course:  CS151, Professor Zee
# Due Date: 10/23/2024
# Lab Assignment: 5
# Problem Statement: This code allows a user to select from a menu of ATM options
# Data In: deposit, withdrawal, view, exit, and amounts to deposit/withdraw
# Data Out: total balance or negative balance warning
# Credits: this code builds on the code from lab 5

# This allows user to make a choice
def input_choice():
    choice = input("\nPlease select an option:"
          "\n\t D - Deposit"
          "\n\t W - Withdraw"
          "\n\t V - View Balance"
          "\n\t E - Exit"
            "\n\t Enter input here: ")
    choice = choice.upper()
    while choice != 'D' and choice != 'W' and choice != 'V' and choice != 'E':
        choice = input("\nPlease select an option:")
    return choice

# Checks if the number inputted in the withdrawal or deposit functions is a negative number
def error_return(int_check):
    if int_check < 0:
        print('Invalid input.')
        return 1
    return 0

# Allows user to make a deposit
def deposit(balance):
    deposit_amt = int(input('How much would you like to deposit?: '))
    if error_return(deposit_amt) == 1:
        print("Bringing you back to the main menu.")
    else:
        balance += deposit_amt
        print(f'Your balance is ${balance:.2f}')
    return balance

# Allows user to make a withdrawal
def withdraw(balance):
    withdraw_amt = int(input('How much would you like to withdraw?: '))
    if error_return(withdraw_amt) == 1:
       print("Bringing you back to the main menu.")
    else:
        balance -= withdraw_amt
        print(f'Your balance is ${balance:.2f}')
        if balance < 0:
            print('You will be charged 5% interest.')
    return balance

# Allows user to view balance
def view_balance(balance):
    print(f'Your balance is ${balance}')

# Allows user to exit
def exit():
    print('Thank you for using the ATM')

# Main program for everything to run
def main():
    print('This code allows a user to select from a list of options at an ATM. \nThey can deposit, withdraw, or check balance')
    balance = 1000
    choice = input_choice()
    while choice != 'E':
        if choice == 'D':
            balance = deposit(balance)
        elif choice == 'W':
            balance = withdraw(balance)
        elif choice == 'V':
            view_balance(balance)
        choice = input_choice()
    exit()

# Call main
main()


