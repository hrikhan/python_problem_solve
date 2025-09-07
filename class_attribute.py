# class bank_account:
#     bank_name = "SBI"

#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount


# # creating object
# ACCOUNT1 = bank_account("John Doe", 1000)
# print(bank_account.bank_name)
# print(ACCOUNT1.name)
# print(ACCOUNT1.balance)

# ACCOUNT1.deposit(500)
# print(ACCOUNT1.balance)

# ACCOUNT2 = bank_account("hridoy khan", 2000)
# print(bank_account.bank_name)
# print(ACCOUNT2.name)
# print(ACCOUNT2.balance)

class BankAccount:
    bank_name = "SBI"

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Account Holder: {self.name}, Balance: {self.balance}"


account1 = BankAccount("Alice", 1000)
# Output: Account Holder: Alice, Balance: 1000
print(account1.bank_name, "bank", account1)
