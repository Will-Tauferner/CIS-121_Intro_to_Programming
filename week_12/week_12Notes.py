'''
class BankAccount:
    def __init__(self,name,initial_balance =0):
        self.owner = name
        self.balance = initial_balance
    def deposit(self, value):
        self.balance += value
    def withdraw(self, value):
        if value > self.balance:
            print('insufficent funds')
        else:
            print(f'here is your ${value}.')
            self.balance -= value
    def get_owner(self):
        return self.owner
    def get_balance(self):
        return self.balance
    def set_owner(self, new_owner):
        self.owner = new_owner
    def __str__(self):
        msg = ''
        msg += f'owner: {self.owner}, balance: {self.balance}'
        return msg
    def __add__(self,other_account):
        new_owner = f'{self.get_owner()} & {other_account.get_owner()}'
        new_balance = 
    def __eq__(self, other):

    matt_acc = BankAccount('Matt')
    matt_acc.deposit(100)
    matt_acc.deposit(50)

    ashley_acc = BankAccount('Ashley',500)
    joint_acc=matt_acc + ashley_acc

'''
'''
total = 0 
user_input = input('Enter a number of type done: ')
     
while user_input != 'done':
    user_number = float(user_input)
    total += user_number
    user_input = input('Enter a number of type done: ')
print(f'total = {total}')
'''
#var_name = open('whatever your file name is . ext', 'r')
from random import randint
my_file = open('numbers.txt', 'w')

for index in range(0,100):
    number = randint(50,250)
    my_file.write(number)






