# Account Holder Details with personal data
class AccountHolderDetails:
    def __init__(self, **kwargs):
        print("\n***\nSETTING UP ACCOUNT\n***\n")

        # if personal details not specified in init, will prompt user to enter details
        if 'name' in kwargs.keys():
            self.__name = kwargs["name"].title()
        else:
            self.__name = input("\nPlease enter a name to continue\n").title()
        
        if 'dob' in kwargs.keys():
            self.__dob = kwargs["dob"]
        else:
            self.__dob = input("\nPlease enter your date of birth\n(DD/MM/YYYY)\n")
        
        if 'address' in kwargs.keys():
            self.__address = kwargs["address"].title()
        else:
            self.__address = input("\nPlease enter your address\n").title()

    
    # displays personal details
    def display_accountholder(self):
        print(f'''
        ACCOUNT HOLDER NAME: {self.__name}
        DATE OF BIRTH: {self.__dob}
        ADDRESS: {self.__address}
        ''')


# bank account class to hold bank account details and methods to deposit/withdraw etc.
class BankAccount(AccountHolderDetails):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # if balance 
        if not hasattr(self, 'balance'):
            print("MAKING NEW ACCOUNT")
            self.open_new_account()
        else:
            self.__balance = kwargs["balance"]
        
    
    
    def open_new_account(self):
        self.__account_number = '123456'
        self.__sort_code = '045454'
        self.__balance = 0
        
    

    def display_bankdetails(self):
        print(f'''
        ACCOUNT NUMBER: ***{self.__account_number[-3:]}
        SORT CODE: ***{self.__sort_code[-3:]}
        BALANCE: {self.__balance}
        ''')

    
    def deposit(self, amount):
        if amount <= 0:
            return "PLEASE DEPOSIT AMOUNT GREATER THAN ZERO"
        self.__balance += amount
        return f"NEW BALANCE: {self.__balance}"

    
    def withdraw(self, amount):
        if self.__balance - amount < 0:
            return "YOU DO NOT HAVE ENOUGH IN YOUR BALANCE"
        self.__balance -= amount
        return f"NEW BALANCE: {self.__balance}"


    def bank_fees(self):
        '''
        Bank fees for maintenance, 5% of current balance
        '''
        self.__balance *= 0.95
    
class manageAccount(BankAccount):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.display_menu()

    def display_menu(self):
        print('''
        DISPLAY MENU
        AVAILABLE ACTIONS:
        personal details        displays relevant personal information
        bank details            displays current bank account balance
        deposit                 deposit money into your account
        withdraw                withdraw money from your account
        '''
        )

        self.continue_display = True
        while self.continue_display:
            self.user_action()    
        
        print("Thank you for using our services")

    def user_action(self):
        action = input("\nWhat would you like to do?\n(exit to stop program)\n").lower().replace(' ','')

        if 'personaldetails' in action:
            self.display_accountholder()
        
        elif 'bankdetails' in action:
            self.display_bankdetails()
        
        elif 'deposit' in action:
            value = float(input("\nHow much would you like to deposit?"))
            print(self.deposit(value))

        elif 'withdraw' in action:
            value = float(input("\nHow much would you like to withdraw?"))
            print(self.withdraw(value))

        elif 'exit' in action:
            self.continue_display = False
            return
        else:
            print("ACTION NOT RECOGNISED, PLEASE TRY AGAIN.")
            return
        

if __name__ == "__main__":
    new_account = manageAccount(dob = '13/07/1999', address = '210 hamer')