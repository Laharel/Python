class User:
    def __init__(self, name, balance ):
        self.name = name
        self.balance = balance
        print(name, balance)

    def deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawal(self, amount):
        if amount > self.balance:
            return "non sufficient funds"
        self.balance -= amount
        return self

    def display_user_balance(self):
        print(self.balance)
        return self.balance

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.deposit(amount)
        print(other_user.name+"'s new balance:", other_user.balance,"\n" + self.name+"'s my current balance:", self.balance)
        return self

Ahmed = User("Ahmed", 100)
Mohammed = User("Mohammed", 0)
Sarah = User("Sarah", 0)

Ahmed.deposit(100).deposit(100).deposit(100)
# Ahmed's new balance is 400
Ahmed.make_withdrawal(50)
# Ahmed's new balance is 350
Ahmed.display_user_balance()

Mohammed.deposit(100).deposit(100)
# Mohammed's new balance is 200
Mohammed.make_withdrawal(50)
# Mohammed's new balance is 150
Mohammed.display_user_balance()

Sarah.deposit(500)
# Sarah's new balance is 500
Sarah.make_withdrawal(50).make_withdrawal(50).make_withdrawal(50)
# Sarah's new balance is 350
Sarah.display_user_balance()

Ahmed.transfer_money(Sarah,100)
# Ahmed's new balance should be 250
# Sarah's new balance should be 450