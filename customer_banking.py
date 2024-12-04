# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """Main function to handle user input and calculate account updates."""

    # Prompt the user to set the savings balance, interest rate, and months for the savings account
    savings_balance = float(input("Enter the initial savings account balance: ").replace(',', ''))
    savings_interest_rate = float(input("Enter the annual interest rate (APR) for the savings account: ").replace(',', ''))
    savings_months = int(input("Enter the number of months: ").replace(',', ''))

    # Call the create_savings_account function
    updated_savings_balance, savings_interest = create_savings_account(savings_balance, savings_interest_rate, savings_months)

    # Print the savings account results
    print("\nSavings Account:")
    print(f"Interest Earned: ${savings_interest:.2f}")
    print(f"Updated Balance: ${updated_savings_balance:.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account
    cd_balance = float(input("\nEnter the initial CD account balance: ").replace(',', ''))
    cd_interest_rate = float(input("Enter the annual interest rate (APR) for the CD account: ").replace(',', ''))
    cd_months = int(input("Enter the number of months: ").replace(',', ''))

    # Call the create_cd_account function
    updated_cd_balance, cd_interest = create_cd_account(cd_balance, cd_interest_rate, cd_months)

    # Print the CD account results
    print("\nCD Account:")
    print(f"Interest Earned: ${cd_interest:.2f}")
    print(f"Updated Balance: ${updated_cd_balance:.2f}")

if __name__ == "__main__":
    # Call the main function
    main()
