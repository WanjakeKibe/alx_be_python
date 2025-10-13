import sys
from bank_account import BankAccount

def main():
    # Initialize account with $100 starting balance as per the example
    account = BankAccount(100)
    
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Parse command and parameters
    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    # Execute the appropriate command
    if command == "deposit" and amount is not None:
        if amount > 0:
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")
    elif command == "withdraw" and amount is not None:
        if amount > 0:
            if account.withdraw(amount):
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()