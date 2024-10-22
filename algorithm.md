# Lab 5/6 Algorithm

* Purpose: To take input from the user
* Name: input_choice
* Parameter(s): None
* Return: Letter from the user
* Algorithm:
  * 1. Ask user to input either D, W, V, or E
    2. While input is not D, W, V, or E
       1. Display error message and ask user to input a letter
    3. Convert letter to uppercase
    4. Return letter


* Purpose: To check for when user inputs negative number
* Name: error_return
* Parameter: User inputted number
* Return: None
* Algorithm:
  * 1. If int_check is negative
        1. Output error message


* Purpose: To deposit money into the account
* Name: deposit
* Parameters: The current balance, the amount the user wants to deposit
* Return: New balance
  * 1. Ask the user how much they want to deposit
    2. Call error_return using the deposit amount as the parameter
    3. Add deposit amount to current balance
    4. Return current balance


* Purpose: To withdraw money from the account
* Name: withdraw
* Parameters: The current balance, the amount the user wants to deposit
* Return: New balance
  * 1. Ask the user how much they want to withdraw
    2. Call error_return using the withdrawal amount as the parameter
    3. Subtract withdraw amount from current balance
    4. If balance < 0
       1. Output message warning user that they will be charged 5% interest
    5. Return current balance


* Purpose: To display the current balance
* Name: view_balance
* Parameters: None
* Return: Current balance
* Algorithm:
  * 1. Return current balance


* Purpose: To run full program
* name: main
* parameters: None
* return: None
* Algorithm:
  * 1. output the purpose of the code
    2. call input_choice
    3. If input choice is D
       1. call deposit
    4. otherwise if input choice is W
       1. call withdraw
    5. otherwise if input choice is V
       1. call view_balance 
    6. output thanks for using ATM