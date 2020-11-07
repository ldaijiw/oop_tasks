# Account Holder Details with personal data

class AccountHolderDetails:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        
        print("\n***SETTING UP ACCOUNT\n***\n")

        if not hasattr(self, 'name'):
            self.__name = input("\nPlease enter a name to continue\n").title()
        else:
            self.__name = kwargs["name"].title()
        
        if not hasattr(self, 'dob'):
            self.__dob = input("\nPlease enter your date of birth\n(DD/MM/YYYY)\n")
        else:
            self.__dob = kwargs["dob"]
        
        if not hasattr(self, 'address'):
            self.__address = input("\nPlease enter your address\n").title()
        else:
            self.__address = kwargs["address"].title()

    
    def display_accountholder(self):
        print(f'''
        ACCOUNT HOLDER NAME: {self.__name}
        DATE OF BIRTH: {self.__dob}
        ADDRESS: {self.__address}
        ''')

        
class BankAccount(AccountHolderDetails):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        if not hasattr(self, 'balance'):
            print("MAKING NEW ACCOUNT")
            self.open_new_account()
    
    
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
            print("PLEASE DEPOSIT AMOUNT GREATER THAN ZERO")
            return
        self.__balance += amount
        return f"NEW BALANCE: {self.__balance}"

    
    def withdrawal(self, amount):
        if self.__balance - amount < 0:
            print("YOU DO NOT HAVE ENOUGH IN YOUR BALANCE")
            return
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
        '''
        )
        



if __name__ == "__main__":
    new_account = manageAccount(name = "LEO WALTMANN")
    new_account.display_accountholder()
    new_account.display_bankdetails()