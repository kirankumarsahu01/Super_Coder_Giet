class customer:
    def __init__(self,cust_id,name,age,wallet_balance):
        self.cust_id=cust_id
        self.name=name
        self.age=age
        self.__wallet_balance=wallet_balance
    def update_balance(self,amount):
        if amount<1000 and amount>0:
            self.__wallet_balance+=amount
    def set_balance(self,amount):
        if amount<5000 and amount>0:
            self.__wallet_balance+=amount        
    '''def show_balance(self):
        print("the balance is ",self.__wallet_balance)'''
#accesing private values
    def get_wallet_balance(self):
        return self.__wallet_balance
c1=customer(100,"gopal",24,1000)
c1.update_balance(500)
#c1.show_balance()
#print(c1.__wallet_balance) #error we are acessing private element 

#wallet_balance is public
#__walletbalance is private
print(c1.get_wallet_balance())
c1.set_balance(5000)
print(c1.get_wallet_balance())


