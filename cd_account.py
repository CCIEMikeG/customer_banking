"""Import the Account class from the Account.py file."""
from Account import Account

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        tuple: Updated CD account balance and interest earned.
    """
    # Create an instance of the `Account` class
    cd_account = Account(balance, 0)

    # Calculate interest earned
    interest_earned = balance * (interest_rate / 100) * (months / 12)

    # Update the CD account balance
    updated_balance = balance + interest_earned

    # Set the updated balance and interest in the account instance
    cd_account.set_balance(updated_balance)
    cd_account.set_interest(interest_earned)

    return updated_balance, interest_earned
