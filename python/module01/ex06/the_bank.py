


class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        # if hasattr(self, 'value'):
        #     self.value = 0
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount
    
    def is_corrupted(self):

        attrs = self.__dict__.keys()
        zip_addr = False
        for attr in attrs:
            if attr.startswith('zip') or attr.startswith('addr'):
                zip_addr = True
            if attr.startswith('b'):
                return True
        if not zip_addr or not 'name' in attrs or not 'id' in attrs or not 'value' in attrs:
            return True

        if self.__dict__.__len__() % 2 == 0:
            return True

        return False



class Bank(object):
    """The bank"""

    def __init__(self):
        self.account = []
    
    def add(self, account):
        self.account.append(account)
    
    def transfer(self, origin, dest, amount):
        """
            @origin: int(id) or str(name) of the first account
            @dest: int(id) or str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return True if success, False if an error occured
        """
        
        origin = self.get_account(origin)
        dest = self.get_account(dest)

        if not isinstance(origin, Account) or not isinstance(dest, Account):
            print("ddd")
            return False

        elif amount < 0 or origin.is_corrupted() or dest.is_corrupted():
            return False

        elif origin.value >= amount:
            dest.transfer(amount)
            origin.value -= amount
            return True

        return False
        

    def fix_account(self, account):
        """
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return True if success, False if an error occured
            
        """

        account_name = account
        account = self.get_account(account)

        if isinstance(account, Account):
            if account.is_corrupted():
                attributes = list(account.__dict__.keys())
                if not 'name' in attributes:
                    account.__dict__.update({'name': account_name})

                if not 'value' in attributes:
                    account.__dict__.update({'value': 0})

                if not 'addr' in attributes and not 'zip' in attributes:
                    account.__dict__.update({'zip': ''})

                for attr in attributes:
                    if attr.startswith('b'):
                        tmp = attr
                        while tmp.startswith('b'):
                            tmp = tmp[1:]
                        account.__dict__[tmp] = account.__dict__[attr]
                        del account.__dict__[attr]
                
                if account.__dict__.__len__() % 2 == 0:
                    account.__dict__.update({'fix': True})

            if account.is_corrupted():
                return False
            return True


    def get_account(self, account):
            if isinstance(account, int):
                for acc in self.account:
                    if acc.id == account:
                        return acc
            if isinstance(account, str):
                for acc in self.account:
                    if acc.name == account:
                        return acc
            return None



if __name__ == '__main__':

    print("\n1- Initial tow Accounts 'abdlali' and 'salmi':")
    abdlali = Account("abdelaali", addr="el kelaa des sraghna", value=100, test=10)
    salmi = Account("salmi", addr="bengerir", value=0, test=10)

    print("\n2- Check if any accounr is corrupted:")
    print("\tabdlali : ", abdlali.is_corrupted())
    print("\tsalmi   : ", salmi.is_corrupted())


    print("\n3- Adding the two accounts to the Bank:")
    bank = Bank()
    bank.add(abdlali)
    bank.add(salmi)

    print("\n4- Show the amount of the two accounts:")
    print("\tabdlali : ", abdlali.value)
    print("\tsalmi   : ", salmi.value)

    print("\n5- Make a transfer with 10 from abdlali --> salmi:")
    bank.transfer('abdelaali', 'salmi', 30)

    print("\n6- Show the amount of the two accounts again:")
    print("\tabdlali : ", abdlali.value)
    print("\tsalmi   : ", salmi.value)

    print("\n7- Create a correpted account 'mohammed' and adding it to the Bank:")
    mohammed = Account("mohammed")
    bank.add(mohammed)

    print("\n8- Check if 'mohammed' is a corrupted account:")
    print("\tmohammed : ", mohammed.is_corrupted())

    print("\n9- Try to fixing it:")
    print("\tAttributes before fixing: ", mohammed.__dict__)
    bank.fix_account('mohammed')
    print("\tAttributes after fixing: ", mohammed.__dict__)

    print("\n10- Check if 'mohammed' is still corrupted:")
    print("\tmohammed : ", mohammed.is_corrupted())