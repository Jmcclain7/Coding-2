class JamesFirstBank:
    def _init_ (self, name, password, address, balance):
        self.balance = balance
    self.name = name
    self.password = password
    self.adress = adress
    self.balance = balance 

    def deposit(self, amount):
        self.balance += amount
        print('thanks'+ self.name + 'your new balance is'  + str (self.balance)) 

    def withdraw(self,amount):
        print('thanks' + self.name + 'your new balance is' + str(self.balance))

    def accessAccount(self, name, password):
        print('')
        # send all user info

    def closeAccount(self, name, password):
        return

    def createAccount(self):
        return

    def transfer(self):
        return

account_1 = JamesFirs+tBank('Jim', 'Vipermoney$9', 'NA', 100)
account_2 = JamesFirstBank('Void', 'Vipermaxmoney', 'NA', 200)

account_1.deposit(50)
account_2.withdraw(30)

def createAccount():
    print('Welcome to James first bank')
    print("please complete the following questions to create your account: ")
    name = input("name: ")
    password = input("password: ")
    address= input("address: ")
    balance= input("How much would you like to add to the new account?: ")

    print("Congratulations! your bank account is done.")

    account_3= JamesFirstBank(name, password, address, balance)
    users.append(account_3)

createAccount()