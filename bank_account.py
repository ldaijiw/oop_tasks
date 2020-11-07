# Account Holder Details with personal data

class AccountHolderDetails:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        
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

        print(self.__name)
        print(self.__dob)
        print(self.__address)

    def display(self):
        print(self.__name)

        
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


    
    def deposit(self, amount):
        self.__balance += amount

    
    def withdrawal(self, amount):
        self.__balance -= amount
    

    def bank_fees(self):
        '''
        Bank fees for maintenance, 5% of current balance
        '''
        self.__balance *= 0.95
    
class manageAccount(BankAccount):

    #def __init__(self):
        
    
    @property
    def account_details(self):
        account_details = {
            "Account Holder": self.name,
            "Balance": self.__balance,
            "Account Number": self.__account_number,
            "Sort Code": self.__sort_code
        }
        return account_details

if __name__ == "__main__":
    new_account = AccountHolderDetails(name = "LEO WALTMANN")
    new_account.display()
    #print(new_account.account_details)