---

# Customer Banking System

This project implements a simple customer banking system for calculating and tracking interest earned on savings and CD accounts. Users can input account details such as balance, interest rate (APR), and duration to calculate the interest earned and updated balances.

---

# Project Structure

- Account.py: Contains the Account class, which provides methods for setting and getting account balances and interest.

- savings_account.py: Includes the create_savings_account function, which calculates interest and updates balances for savings accounts.

- cd_account.py: Includes the create_cd_account function, which calculates interest and updates balances for CD accounts.

- customer_banking.py: The main program file that interacts with the user, prompting inputs and displaying results.

---

# How to Use

Requirements

- Python 3.x installed on your system.
- A terminal or command prompt to run the program.

# Steps to Run
 1. Clone the repository
 
 git clone https://github.com/CCIEMikeG/customer_banking.git
cd customer_banking

 2. Run the program:
 python customer_banking.py
 
 3. Follow the on-screen prompts to:
     - Enter the savings account balance, interest rate (APR), and number of months.
	 - Enter the CD account balance, interest rate (APR), and number of months.

4. The program will calculate and display:
     - Interest earned for each account.
     - Updated balances after the specified duration.
	 
---	 
	 
# Example Output

Enter the initial savings account balance: 100000
Enter the annual interest rate (APR) for the savings account: 2
Enter the number of months: 24

Savings Account:
Interest Earned: $4000.00
Updated Balance: $104000.00

Enter the initial CD account balance: 2000
Enter the annual interest rate (APR) for the CD account: 3
Enter the number of months: 24

CD Account:
Interest Earned: $120.00
Updated Balance: $2120.00

---

# File Descriptions

- Account.py:

	- Defines the Account class, which is the foundation for both savings and CD accounts.
	- Methods include:
		- set_balance(balance): Sets the account balance.
		- set_interest(interest): Sets the interest earned.

- savings_account.py:

	- Function: create_savings_account(balance, interest_rate, months)
		- Calculates the interest earned based on the balance, APR, and duration.
		- Returns the updated balance and interest earned.
		
- cd_account.py:

	- Function: create_cd_account(balance, interest_rate, months)
		- Similar to create_savings_account, but tailored for CD accounts.
		
- customer_banking.py:

	- Contains the main program logic.
	- Prompts the user for inputs, calculates interest and balances, and displays the results.

---
		
# Author

- Michael Garner

---

# Repository Link

- https://github.com/CCIEMikeG/customer_banking.git

---

# License

This project is open-source and free to use for educational purposes.