from tkinter import messagebox
balance = 0
check_flag = False

def deposit(amount,bal):
  global balance
  balance = balance + amount
  print(f"Balance is -> {balance}")
  return balance
  # print(f"Deposit of rs: {amount} succesful\nCurrent balance = {balance}")


def withdraw(amount,bal):
  global balance
  check_list = []
  if balance < amount:
    # print("insuffiecient funds")
    check_flag = False
    check_list.append(check_flag)
    check_list.append(balance)
    print(check_list)
    return check_list
  else:
      if amount %100 ==0:
        check_flag = True
        balance = balance - amount
        # print(f"Withdrawl of Rs: {amount} succesful\nCurrrent balance = {balance}")
        check_list.append(check_flag)
        check_list.append(balance)
        print(check_list)
        return check_list
      else:
        messagebox.showinfo(title="Information",message="Enter amount in multiple of 100's")


def check_balance():
  global balance
  bal = balance
  return bal
  # print(f"Your balance is Rs: {balance}")


# withdraw(100,100)
# withdraw(10000)
# deposit(1000)
# check_balance()
