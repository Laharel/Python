class User:
    def __init__(self, name, balance, num_accounts=0 ):
        self.name = name
        if num_accounts == 2:
            self.current_account = BankAccount(balance=0)
            self.saving_account = BankAccount(balance=0)
        elif num_accounts > 2:
            print("maximum is 2 accounts")
        else:
            self.current_account = BankAccount(balance=balance)
        print(name, balance)

    def make_deposit(self, amount, name_account):
        # self.balance += amount
        if not (name_account) and self.current_account:
            self.current_account.deposit(amount)
        elif name_account == "saving":
            self.saving_account.deposit(amount)
        elif name_account == "current":
            self.current_account.deposit(amount)

        return self

    def make_withdrawal(self, amount, name_account="current"):
        if not (name_account) and self.current_account:
            self.current_account.withdraw(amount)
        elif name_account == "saving":
            self.saving_account.withdraw(amount)
        elif name_account == "current":
            self.current_account.withdraw(amount)

        return self

    def display_user_balance(self, name_account="current"):
        if not (name_account) and self.current_account:
            print(self.current_account.balance)
        elif name_account == "saving":
            print(self.saving_account.balance)
        elif name_account == "current":
            print(self.current_account.balance)
        return self


        

    # def transfer_money(self, other_user, amount):
    #     self.make_withdrawal(amount)
    #     other_user.deposit(amount)
    #     print(other_user.name+"'s new balance:", other_user.balance,"\n" + self.name+"'s my current balance:", self.balance)
    #     return self
    
class BankAccount:
	def __init__(self, int_rate=0.01, balance=0):
	# don't forget to add some default values for these parameters! your code here! (remember, this is where we specify the attributes for our class) don't worry about user info here; we'll involve the User class soon
		self.int_rate = int_rate
		self.balance = balance
	def deposit(self, amount):
		# your code here
		self.balance += amount
		return self
	def withdraw(self, amount):
		# withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
		if (amount > self.balance):
			self.balance-=5
			print("Insufficient funds: Charging a $5 fee")
		else:
			self.balance -= amount 
		return self


	def display_account_info(self):
		# display_account_info(self) - print to the console: eg. "Balance: $100"
		print("balance: $"+str(self.balance) )

	def yield_interest(self):
		# your code here
		if (self.balance>0):
			self.balance=self.balance+(self.balance*self.int_rate)

		return self

# Creating user account takes (name, balance, number of accounts)
# in case no number of accounts is provided, current_account will only be created
# Note: maximum number of accounts is 2
seham = User("Seham", 0, 2)
user_1 = User("just_user", 0, 4)
user_3 = User("another_user", 0)
# following line will display error because user_3 will only be given one current_account
# user_3.saving_account.display_account_info()

# Choosing which account to deposit into is done through one of two methods
# METHOD 1: depositing 100, and displaying account info through BankAccount().display_account_info()
seham.saving_account.deposit(100).display_account_info()
# METHOD 2: depositing 100, and displaying account balance through User().display_user_balance()
seham.make_deposit(100, "saving").display_user_balance("saving")

# Choosing which account to withdrwa from is done through one of two methods
# METHOD 1: withdrawing 100 through BankAccount().withdraw() 
seham.saving_account.withdraw(100)
# METHOD 2: withdraw 100 through User().make_withdrawal() 
seham.make_withdrawal(50, "saving")

# choosing which account to display info
# METHOD 1: display through BankAccount().display_account_info()
seham.saving_account.display_account_info()
# METHOD 2: display through User().display_user_balance()
seham.display_user_balance("saving")





