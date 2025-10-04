class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize a BankAccount with an optional initial balance.
        
        Args:
            initial_balance (float): Starting balance for the account (default 0)
        """
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        """
        Deposit the specified amount into the account.
        
        Args:
            amount (float): Amount to deposit
        """
        if amount > 0:
            self.account_balance += amount
    
    def withdraw(self, amount):
        """
        Withdraw the specified amount from the account if funds are sufficient.
        
        Args:
            amount (float): Amount to withdraw
            
        Returns:
            bool: True if withdrawal was successful, False if insufficient funds
        """
        if amount > 0 and self.account_balance >= amount:
            self.account_balance -= amount
            return True
        return False
    
    def display_balance(self):
        """
        Display the current balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")