# Account Holder Details with personal data

class AccountHolderDetails:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        
        if not hasattr(self, 'name'):
            self.name = input("\nPlease enter a name to continue")
        
        
class MyAccount(AccountHolderDetails):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        if not hasattr(self, 'account_details'):
            self.open_new_account()
    
    
    def open_new_account(self):
        account_number = '123456'
        sort_code = '045454'
        balance = 0
