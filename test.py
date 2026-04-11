import random

class Account:
    account_count = 0
    
    def __init__(self, name, balance):
        self.deposit_count = 0

        self.name = name
        self.balance = balance
        self.bank = 'sc은행'

        num1 = random.randint(0,999)
        num2 = random.randint(0,99)
        num3 = random.randint(0,999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)

        self.account_num = f'{num1}-{num2}-{num3}'

        Account.account_count += 1
    
    def get_account_num(self):
        print(Account.account_count)
        
    def deposit(self, d_amount):
        if d_amount >= 1: # 1원 이상 입금하면
            self.balance += d_amount #잔액증가

            self.deposit_count += 1

        if self.deposit_count % 5 == 0:
            self.balance = self.balance * 1.01

    def withdraw(self, w_amount):
        if w_amount > self.balance:
            print('출금 불가')
        else:
            self.balance -= w_amount

    def display_info(self):
        print(f'은행이름: {self.bank}\n예금주: {self.name}\n계좌번호: {self.account_num}\n잔고: {self.balance:,}')
    
bank_list = []

a = Account('용준',1_000_000)
b = Account('용민',20_000)
c = Account('용범',3_000_000)

bank_list.append(a)
bank_list.append(b)
bank_list.append(c)

# bank_list에 객체들이 담겨 있다고 가정합니다.
for account in bank_list:
    account.display_info() # 각 객체의 정보를 출력하는 메서드 호출
    print("-" * 25)

a.deposit(100)
a.deposit(100)
a.deposit(100)
a.deposit(100)
a.deposit(100)
a.deposit(10000)
print(a.balance)