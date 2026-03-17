# Encapsulation -
# bind the data variables with the methods
# Data Member - / Class Variables
# Methods - Def function within the class
# Wrapping or binding the data variables with the methods - Encapsulation.

# Hide the data members(class variables, instance variables) by using only the methods.

class Car:
    name = None
    password = "123"

    def __init__(self):
        print("I am called when a Object is created")

    def change_password(self):
        self.password = "345"
# This is end of the class

xuv = Car()
xuv.password = "345"


# class BankAccount:
#     def __init__(self):
#         self.balance = 0
#
#     def deposit(self, amount):
#         self.balance = self.balance + amount
#
#     def _withdraw(self, amount):
#         self.balance = self.balance - amount
#
#     def __show_balance(self): #Hidden method, that will not read by class
#         print(f'Available Account Balance: {self.balance}')
#
#
# account_1 = BankAccount()
# account_1.deposit(1000)
# account_1._withdraw(200)
# account_1.__show_balance() #Gives Error

# __method → name-mangled (pseudo-private), Not Recommended to use
# account_1._BankAccount__show_balance()