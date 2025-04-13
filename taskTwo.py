# Basic account class to hold customer details and funds
class Account:
    def __init__(self, holder_name, starting_balance):
        self.name = holder_name 
        self.balance = starting_balance 
    
    def deposit(self, amount):
        self.balance = self.balance + amount
    
  
    def withdraw(self, amount):
        pass 
    
 
    def show_details(self):
        return f"Customer: {self.name}, Current Balance: {self.balance:.2f}"


# Regular checking account
class CurrentAccount(Account):
    def __init__(self, name, initial_deposit):
        super().__init__(name, initial_deposit)
        self.cheques_used = 0 
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount}. Current Balance: {self.balance}"
        return "Insufficient funds!"


# Savings-style account with limits
class DepositAccount(Account):
    def __init__(self, name, deposit, max_withdrawals, interest_pct):
        super().__init__(name, deposit)
        self.max_withdrawals = max_withdrawals
        self.withdrawal_count = 0
        self.interest_rate = interest_pct
    
    def withdraw(self, amount):
        if self.withdrawal_count >= self.max_withdrawals:
            return "All of your withdrawals for this month have been utilized."
        elif amount > self.balance:
            return "Not able to take out more than you have!"
        else:
            self.balance -= amount
            self.withdrawal_count += 1
            return f"Withdrew {amount}. {self.max_withdrawals - self.withdrawal_count} withdrawals left"
    
    def calculate_yearly_interest(self):
        return (self.balance * self.interest_rate)/100


# Account with strict withdrawal limits
class RestrictedAccount(CurrentAccount):
    def __init__(self, name, balance, max_single_withdrawal):
        super().__init__(name, balance)
        self.max_withdrawal = max_single_withdrawal
    
    def withdraw(self, amount):
        if amount > self.max_withdrawal:
            return f"No more than {self.max_withdrawal}  can be taken out at once."
        return super().withdraw(amount)


# Account allowing temporary negative balance
class OverdraftAccount(CurrentAccount):
    def __init__(self, name, balance, overdraft_allowance):
        super().__init__(name, balance)
        self.overdraft_limit = overdraft_allowance
    
    def withdraw(self, amount):
        if (self.balance - amount) >= -self.overdraft_limit:
            self.balance -= amount
            return f"Balance: {self.balance}"
        return "Overdraft limit reached; withdrawal is not possible"


# The bank managing all accounts
class BankSystem:
    def __init__(self):
        self.customer_accounts = [] 
    
    def add_customer_account(self, new_account):
        self.customer_accounts.append(new_account)
    
    def process_withdrawal(self, account_name, amount):
        for acc in self.customer_accounts:
            if acc.name == account_name:
                return acc.withdraw(amount)
        return "There was no account associated with your name."


# Testing the system
if __name__ == "__main__":
   
    alice = CurrentAccount("Tom Holland", 1250.50)
    bob = DepositAccount("Andrew Garfield", 8500, 4, 3.2)
    charlie = RestrictedAccount("Sadie Sink", 3200, 1000)
    dave = OverdraftAccount("David Warner", 75, 400)
    
    # Set up the bank
    my_bank = BankSystem()
    my_bank.add_customer_account(alice)
    my_bank.add_customer_account(bob)
    my_bank.add_customer_account(charlie)
    my_bank.add_customer_account(dave)
    
    # Try some transactions
    print(my_bank.process_withdrawal("Tom Holland", 200)) 
    print(my_bank.process_withdrawal("Andrew Garfield", 1000))  
    print(my_bank.process_withdrawal("Sadie Sink", 1500)) 
    print(my_bank.process_withdrawal("David Warner", 450))  
    print(my_bank.process_withdrawal("Unknown Person", 100)) 