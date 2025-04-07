class BankAccount:
    """Base class for all bank account types"""
    def __init__(self, account_name, balance=0.0):
        self.account_name = account_name
        self.balance = balance
    
    def deposit(self, amount):
        """Deposit money into account"""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
            return True
        print("Deposit amount must be positive")
        return False
    
    def withdraw(self, amount):
        """Withdraw money from account (base implementation)"""
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return False
        if amount > self.balance:
            print("Insufficient funds!")
            return False
        self.balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        return True
    
    def __str__(self):
        return f"{self.__class__.__name__}('{self.account_name}') - Balance: ${self.balance:.2f}"

class SavingsAccount(BankAccount):
    """Savings account with interest and minimum balance"""
    def __init__(self, account_name, balance=0.0, interest_rate=0.01, min_balance=100.0):
        super().__init__(account_name, balance)
        self.interest_rate = interest_rate
        self.min_balance = min_balance
    
    def add_interest(self):
        """Add monthly interest to account"""
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"Added interest: ${interest:.2f}")
    
    def withdraw(self, amount):
        """Override withdraw to enforce minimum balance"""
        if self.balance - amount < self.min_balance:
            print(f"Withdrawal denied. Must maintain minimum ${self.min_balance:.2f} balance.")
            return False
        return super().withdraw(amount)

class CheckingAccount(BankAccount):
    """Checking account with transaction fees"""
    def __init__(self, account_name, balance=0.0, transaction_fee=1.50):
        super().__init__(account_name, balance)
        self.transaction_fee = transaction_fee
    
    def withdraw(self, amount):
        """Override withdraw to include transaction fee"""
        total_amount = amount + self.transaction_fee
        if super().withdraw(total_amount):
            print(f"Transaction fee: ${self.transaction_fee:.2f}")
            return True
        return False

class Bank:
    """Bank that manages multiple accounts"""
    def __init__(self, name):
        self.name = name
        self.accounts = []
    
    def add_account(self, account):
        """Add an account to the bank"""
        if not isinstance(account, BankAccount):
            raise TypeError("Can only add BankAccount objects")
        self.accounts.append(account)
        print(f"Added account: {account.account_name}")
    
    def find_account(self, account_name):
        """Find account by name"""
        for account in self.accounts:
            if account.account_name == account_name:
                return account
        return None
    
    def withdraw(self, account_name, amount):
        """Withdraw from account using polymorphism"""
        account = self.find_account(account_name)
        if account:
            return account.withdraw(amount)
        print(f"Error: Account '{account_name}' not found.")
        return False
    
    def deposit(self, account_name, amount):
        """Deposit to account"""
        account = self.find_account(account_name)
        if account:
            return account.deposit(amount)
        print(f"Error: Account '{account_name}' not found.")
        return False
    
    def __str__(self):
        return f"{self.name} Bank with {len(self.accounts)} accounts"

# Demonstration
if __name__ == "__main__":
    # Create a bank
    my_bank = Bank("National")
    
    # Create accounts
    savings = SavingsAccount("Alice's Savings", 500.0)
    checking = CheckingAccount("Bob's Checking", 300.0)
    
    # Add accounts to bank
    my_bank.add_account(savings)
    my_bank.add_account(checking)
    
    print("\n--- Transaction Examples ---")
    
    # Demonstrate deposits
    my_bank.deposit("Alice's Savings", 200.0)
    my_bank.deposit("Bob's Checking", 150.0)
    
    # Demonstrate withdrawals (showing polymorphism)
    my_bank.withdraw("Alice's Savings", 650.0)  # Should fail (min balance)
    my_bank.withdraw("Alice's Savings", 100.0)  # Should succeed
    my_bank.withdraw("Bob's Checking", 100.0)   # Includes fee
    
    # Try withdrawing from non-existent account
    my_bank.withdraw("Charlie's Account", 50.0)
    
    # Add interest to savings
    print("\n--- Monthly Interest ---")
    savings.add_interest()
    
    # Show final balances
    print("\n--- Final Account Status ---")
    for account in my_bank.accounts:
        print(account)