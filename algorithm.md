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
* Return: Return 1 if true, 0 if false (This is used in the deposit and withdraw functions to see if they should still run or not)
* Algorithm:
  * 1. If int_check is negative
        1. Output error message
        2. Return 1
    2. Return 0


* Purpose: To deposit money into the account
* Name: deposit
* Parameters: The current balance, the amount the user wants to deposit
* Return: New balance
  * 1. Ask the user how much they want to deposit
    2. If error_return returns 1 using the deposit amount as the parameter
       1. Output message telling user that they will return to the main menu
    3. Otherwise
       1. Add deposit amount to current balance
       2. Output the user's new balance
    4. Return current balance


* Purpose: To withdraw money from the account
* Name: withdraw
* Parameters: The current balance, the amount the user wants to deposit
* Return: New balance
  * 1. Ask the user how much they want to withdraw
    2. If error_return returns 1 using the withdrawal amount as the parameter
       1. Output message telling user that they will return to the main menu
    3. Otherwise
       1. Subtract withdraw amount from current balance
       2. Output the user's new balance
       3. If balance < 0
          1. Output message warning user that they will be charged 5% interest
    4. Return current balance


* Purpose: To display the current balance
* Name: view_balance
* Parameters: None
* Return: Current balance
* Algorithm:
  * 1. Return current balance


* Purpose: Displays exit message when done
* Name: exit
* Parameters: None
* Return: None
* Algorithm:
  * 1. Output Thank for using our ATM


* Purpose: To run full program
* name: main
* parameters: None
* return: None
* Algorithm:
  * 1. output the purpose of the code
    2. Create variable balance and set it equal to 1000
    3. call input_choice
    4. If input choice is D
       1. call deposit and set equal to balance
    5. otherwise if input choice is W
       1. call withdraw and set equal to balance
    6. otherwise if input choice is V
       1. call view_balance 
    7. output thanks for using ATM