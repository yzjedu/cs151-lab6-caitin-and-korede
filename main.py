# Programmers:  Caitlin Burns and Korede Oni
# Course:  CS151, Professor Zee
# Due Date: 10/23/2024
# Lab Assignment: 6
# Problem Statement: This code allows a user to select from a menu of ATM options using functions
# Data In: deposit, withdrawal, view, exit, and amounts to deposit/withdraw
# Data Out: total balance or negative balance warning
# Credits: building on code from lab 5

#this runs the main menu of the ATM
def input_choice():
    choice = input("\nPlease select an option:"
          "\n\t D - Deposit"
          "\n\t W - Withdraw"
          "\n\t V - View Balance"
          "\n\t E - Exit"
            "\n\t Enter input here:")
    choice = choice.upper()
    while choice != 'D' and choice != 'W' and choice != 'V' and choice != 'E':
        choice = input("\nPlease select an option:")
    return choice

#this checks for negative numbers and reroutes the user
def error_return(int_check):
    if int_check < 0:
        print('Input a valid number')

#this allows the user to make a deposit
def deposit(balance):
    deposit_amt = int(input('How much would you like to deposit?: '))
    while deposit_amt < 0:
        error_return(deposit_amt)
        deposit_amt = int(input('How much would you like to deposit?: '))
    error_return(deposit_amt)
    balance += deposit_amt
    print(f'Your balance is ${balance:.2f}')
    return balance

#this allows the user to make a withdrawal
def withdraw(balance):
    withdraw_amt = int(input('How much would you like to withdraw?: '))
    while withdraw_amt < 0:
        error_return(withdraw_amt)
        withdraw_amt = int(input('How much would you like to withdraw?: '))
    error_return(withdraw_amt)
    balance -= withdraw_amt
    print(f'Your balance is ${balance:.2f}')
    if balance < 0:
        print('You will be charged 5% interest.')
    return balance

#this allows the user to view the balance
def view_balance(balance):
    print(f'Your balance is ${balance}')

#this allows the user to exit the loop
def exit():
    print('Thank you for using the ATM')

#this runs the main part of the program
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


