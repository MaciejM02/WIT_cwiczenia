class BankCard:
    def __init__(self,owner,number,provider):
        self.number = number
        self.owner = owner
        self.provider = provider

    
    def get_number(self):
        print("number")
    def get_owner(self):
        print("owner")
    def get_provider(self):
        print("provider")
class BankAccount:
    def __init__(self,owner,balance,bank):
        self.balance = balance
        self.owner = owner
        self.bank = bank

    
    def get_balance(self):
        print("balance")
    def set_balance(self):
        print("balance")
    def get_owner(self):
        print("owner")
    def get_bank(self):
        print("bank")
class Bank:
    def __init__(self,name,bank_accounts,bank_cards):
        self.bank_accounts = bank_accounts
        self.name = name
        self.bank_cards = bank_cards

    
    def get_bank_accounts(self):
        print("bank_accounts")
    def get_bank_cards(self):
        print("bank_cards")
class CreditCard(BankCard):
    def __init__(self,owner,number,provider,balance,payments_history):
        super().__init__(owner,number,provider)
        self.balance = balance
        self.payments_history = payments_history

    
    def get_balance(self):
        print("balance")
    def set_balance(self):
        print("balance")
    def get_payments_history(self):
        print("payments_history")
class GoldenCreditCard(CreditCard):
    def __init__(self,owner,number,provider,balance,payments_history,reward_points):
        super().__init__(owner,number,provider,balance,payments_history)
        self.reward_points = reward_points

    
    def get_reward_points(self):
        print("reward_points")
    def set_reward_points(self):
        print("reward_points")
class PremiumBankAccount(BankAccount):
    def __init__(self,owner,balance,bank,financial_manager):
        super().__init__(owner,balance,bank)
        self.financial_manager = financial_manager

    
    def get_financial_manager(self):
        print("financial_manager")
    def set_financial_manager(self):
        print("financial_manager")
class StudentBankAccount(BankAccount):
    def __init__(self,owner,balance,bank,overdraft_balance,overdraft_limit):
        super().__init__(owner,balance,bank)
        self.overdraft_balance = overdraft_balance
        self.overdraft_limit = overdraft_limit

    
    def get_overdraft_balance(self):
        print("overdraft_balance")
    def set_overdraft_balance(self):
        print("overdraft_balance")
    def get_overdraft_limit(self):
        print("overdraft_limit")
    def get_overdraft_limit(self):
        print("overdraft_limit")


TEST = GoldenCreditCard("me",1,"?","+","?","9999")
TEST.get_number()
TEST.get_owner()
TEST.get_provider()
TEST.get_balance()
TEST.get_reward_points()
print(TEST.number)
print(TEST.owner)
print(TEST.provider)
print(TEST.balance)
print(TEST.reward_points)