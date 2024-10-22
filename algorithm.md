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
* Parameter(s): User inputted number
* Return: Return 1 if int_check is negative, 0 if it's positive (This is used in the deposit and withdraw functions to see if they should still run or not)
* Algorithm:
  * 1. If int_check is negative
        1. Output error message
        2. Return 1
    2. Return 0


* Purpose: To deposit money into the account
* Name: deposit
* Parameter(s): Current balance
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
* Parameter(s): Current balance
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
* Parameter(s): None
* Return: Current balance
* Algorithm:
  * 1. Return current balance


* Purpose: Displays exit message when done
* Name: exit
* Parameter(s): None
* Return: None
* Algorithm:
  * 1. Output Thank for using our ATM


* Purpose: To run full program
* Name: main
* parameter(s): None
* Return: None
* Algorithm:
  * 1. Output the purpose of the code
    2. Create variable balance and set it equal to 1000
    3. Create variable choice and set it equal to the function input_choice
    4. While choice does not equal E
       1. If input choice is D
          1. Update balance by setting it equal to the function deposit
       2. Otherwise, if input choice is W
          1. Update balance by setting it equal to the function withdraw
       3. Otherwise, if input choice is V
          1. call view_balance 
    5. Call exit