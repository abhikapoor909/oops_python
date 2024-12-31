class bank:
    def __init__(self,balance):
        self.balance=balance
        

    def deposit(self,amount):
        self.balance = self.balance+amount
        self.amount=amount
        self.display()

        
    # use self to make the variable global in that class

    ## use self to call the method of same class


    def display(self):
        print(f"hello your balance was {self.balance}")
        print(f"your new balance is {self.balance}")


bank1=bank(1200)
bank1.deposit(500)
