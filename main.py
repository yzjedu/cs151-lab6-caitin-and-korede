from itertools import filterfalse
from logging import DEBUG


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


def error_return(int_check):
    if int_check < 0:
        print('Invalid input.')
        return 1
    return 0


def deposit(balance):
    deposit_amt = int(input('How much would you like to deposit?: '))
    if error_return(deposit_amt) == 1:
        print("Bringing you back to the main menu.")
    else:
        balance += deposit_amt
        print(f'Your balance is ${balance:.2f}')
    return balance

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

def view_balance(balance):
    print(f'Your balance is ${balance}')

def exit():
    print('Thank you for using the ATM')

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


main()


