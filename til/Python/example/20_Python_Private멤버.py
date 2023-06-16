class BankAccount:
    __id=0
    __name=""
    __balance=0
    def __init__(self,id,name,balance):
        self.__id=id
        self.__name=name
        self.__balance=balance
    
    def deposit(self,amount):
        self.__balance+=amount
    
    def withdraw(self,amount):
        self.__balance-=amount
    
    def __str__(self):
        return "{},{},{}".format(self.__id,self.__name,self.__balance)

account1=BankAccount(100,"전우치",1500)
print(BankAccount._BankAccount__balance)
BankAccount._BankAccount__balance=35000

print(account1)
# print(account1.__balance) 그냥 바로 접근하려고 하면 문제가 발생하게 만들어 두었다.
account1.withdraw(5000)
print(account1)
account1.deposit(2000)
print(account1)