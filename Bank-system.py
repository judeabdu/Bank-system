class Bank_account:
  def __init__(self, account_number, balance, pin):
    self._account_number = account_number
    self._balance = balance
    self._pin = pin
  def check_pin(self, input_pin):
    return input_pin == self._pin
  def deposit(self, amount):
    if amount > 0:
      self._balance += amount
      return("Deposit successful")
    else:
      return("unable to process negative deposit")
  def withdraw(self, amount):
    if amount <= self._balance:
      self._balance -= amount
      return("withdraw successful")
    else:
      return("you have insufficient funds for this transaction")
  def get_balance(self):
    return self._balance
bank_account = []
count = int(input("How many accounts? ").strip())
for i in range(count):
  print(f"\nAccount number {i+1}")
  account_number = input("Enter account number: ").strip()
  balance =int(input("Enter starting balance: ").strip())
  pin = input("Set a 4-digit PIN: ").strip()
  b_acc = Bank_account(account_number, balance, pin)
  bank_account.append(b_acc)
login_number = input("\nEnter your account number: ")
login_pin = input("Enter your PIN: ")
current_b_acc = None
for b_acc in bank_account:
  if b_acc._account_number == login_number:
    current_b_acc = b_acc
    break
if current_b_acc is None:
  print("Account not found")
else:
  if not current_b_acc.check_pin(login_pin):
    print("Incorrect PIN")
  else:
    while True:
      print("\n---Menu---")
      print("1. deposit")
      print("2. withdraw")
      print("3. Check Balance")
      print("4. Exit")
      choice = input("\nEnter your choice(1-4): ").strip()
    if choice == "1":
      amount = float(input("\nEnter amount to deposit: ").strip())
      print(current_b_acc.deposit(amount))
    elif choice == "2":
      amount = float(input("\nEnter amount to withdraw: ").strip())
      print(current_b_accb.withdraw(amount))
    elif choice == "3":
      print("Your current balance is:", current_b_acc.get_balance())
    elif choice == "4":
      print("thank you for banking with us. Goodbye!")
    else:
      print("invalid choice! Please select 1-4.")

from google.colab import files
uploaded = files.upload()

