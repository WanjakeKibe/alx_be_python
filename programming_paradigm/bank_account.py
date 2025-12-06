# bank_account.py

class BankAccount:
    """A class representing a simple bank account."""
    
    def __init__(self, initial_balance=0):
        """
        Initialize a BankAccount with an initial balance.
        
        Args:
            initial_balance (float): Starting balance (default: 0)
        """
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        """
        Deposit money into the account.
        
        Args:
            amount (float): Amount to deposit
        """
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        """
        Withdraw money from the account if sufficient funds are available.
        
        Args:
            amount (float): Amount to withdraw
            
        Returns:
            bool: True if withdrawal successful, False if insufficient funds
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
            
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False
    
    def display_balance(self):
        """
        Display the current account balance.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")
