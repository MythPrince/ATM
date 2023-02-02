import tkinter
from tkinter import messagebox
# import playsound
import transaction

window = tkinter.Tk()
window.title("X-LOCKS")
# window.geometry('1000x1000')

window.config(padx=100, pady=100, bg="#222831")
# window.configure(bg='white')

current_balance = transaction.check_balance()

def show_frame(frame):
  frame.tkraise()


def main_menu_fun():
  show_frame(frame2)


def exit_fun():
  show_frame(frame)


def login():
  username = "Oji"
  password = "sree"
  if username_entry.get() == username and password_entry.get() == password:
    messagebox.showinfo(title="Login Success",
                        message="You successfully logged in.")
    # playsound.playsound(C:/Users/Pradn/Documents/mine/GUI/play.mpeg)

    show_frame(frame2)
    username_entry.delete(0,"end")
    password_entry.delete(0,"end")
  else:
    messagebox.showerror(title="Error", message="Invalid login.")


def withdraw_frame_fun():
  show_frame(withdraw_frame)


def withdraw_amount_fun():

  # if  transaction.withdraw(int(withdraw_entry.get()))== :
  #     messagebox.showerror(title= "Error",message="Dont leave blank entry")

  new_list = transaction.withdraw(int(withdraw_entry.get()),current_balance)
  if new_list[0]:
    messagebox.showinfo(
      title="Transaction complete",
      message=
      f"Your withdraw of money Rs: {int(withdraw_entry.get())} is successful\nCurrent balance is {new_list[1]}"
    )
    withdraw_entry.delete(0,"end")
    username_entry.delete(0,"end")
    password_entry.delete(0,"end")
    show_frame(frame2)
  else:
    messagebox.showerror(title="Error", message="Insuffiecient amount")


def deposit_frame_fun():
  show_frame(deposit_frame)


def deposit_amount_fun():
  new_balance = transaction.deposit(int(deposit_entry.get()),current_balance)
  messagebox.showinfo(
    title=" Transaction complete",
    message=
    f"Your deposit of money Rs: {int(deposit_entry.get())} succesful\nCurrent balance id Rs: {new_balance} "
  )
  deposit_entry.delete(0,"end")
  username_entry.delete(0,"end")
  password_entry.delete(0,"end")
  show_frame(frame2)


def balance_frame_fun():
  new_bal = transaction.check_balance()
  # print(f"current balance is -> {new_bal}")
  show_frame(balance_frame)
  balance_amount_label.config(text=f"your current balance is {new_bal}")

def back():
  show_frame(frame2)


frame = tkinter.Frame(bg='#222831')
frame2 = tkinter.Frame(bg='#222831')
withdraw_frame = tkinter.Frame(bg='#222831')
deposit_frame = tkinter.Frame(bg='#222831')
balance_frame = tkinter.Frame(bg='#222831')

for fram in (frame, frame2, withdraw_frame, deposit_frame, balance_frame):
  fram.grid(row=0, column=0, sticky='nsew')

# Creating widgets frame
login_label = tkinter.Label(frame,
                            text="Login",
                            bg='#222831',
                            fg="#A6E3E9",
                            font=("Arial", 30, "bold"))
username_label = tkinter.Label(frame,
                               text="Username: ",
                               bg='#222831',
                               fg="#FFFFFF",
                               font=("Arial", 16))
username_entry = tkinter.Entry(frame, font=("Arial", 16))
username_entry.focus()
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
password_label = tkinter.Label(frame,
                               text="Password: ",
                               bg='#222831',
                               fg="white",
                               font=("Arial", 16))
login_button = tkinter.Button(frame,
                              text="Login",
                              bg="#A6E3E9",
                              fg="black",
                              font=("Arial", 16),
                              command=login)

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame2

login_label2 = tkinter.Label(frame2,
                             text="PS Bank",
                             bg='#222831',
                             fg="#71C9CE",
                             font=("Arial", 30, "bold"))
login_label2.place(x=110, y=30)
canvas=tkinter.Canvas(frame2, width=100, height=100, highlightthickness=0)
img=tkinter.PhotoImage(file="GUI/images.png")
canvas.create_image(31, 50, image=img)
canvas.place(x=8, y=10)
withdraw_button = tkinter.Button(frame2,
                                 text="Withdraw",
                                 bg="#A6E3E9",
                                 fg="black",
                                 font=("Arial", 16),
                                 width=25,
                                 height=2,
                                 command=withdraw_frame_fun)
withdraw_button.place(x=8, y=100)

deposit_button = tkinter.Button(frame2,
                                text="Deposit",
                                bg="#A6E3E9",
                                fg="black",
                                font=("Arial", 16),
                                width=25,
                                height=2,
                                command=deposit_frame_fun)
deposit_button.place(x=8, y=170)

balance_button = tkinter.Button(frame2,
                                text="Balance",
                                bg="#A6E3E9",
                                fg="black",
                                font=("Arial", 16),
                                width=25,
                                height=2,
                                command=balance_frame_fun)
balance_button.place(x=8, y=240)

# Withdraw frame
withdraw_label = tkinter.Label(withdraw_frame,
                               text="PS Bank",
                               bg='#222831',
                               fg="#A6E3E9",
                               font=("Arial", 30, "bold"))
withdraw_label.grid(row=0, column=1, columnspan=2, sticky="news", pady=40)

canvas=tkinter.Canvas(withdraw_frame, width=100, height=100, highlightthickness=0)
img2=tkinter.PhotoImage(file="GUI/images.png")
canvas.create_image(31, 50, image=img2)
canvas.place(x=11, y=21)



withdraw_amount_label = tkinter.Label(withdraw_frame,
                                      text="Amount: ",
                                      bg='#222831',
                                      fg="#FFFFFF",
                                      font=("Arial", 16))
withdraw_amount_label.grid(row=1,
                           column=0,
                           columnspan=2,
                           sticky="news",
                           pady=40)

withdraw_entry = tkinter.Entry(withdraw_frame, width=20, font=("Arial", 16))
withdraw_entry.focus()
withdraw_entry.grid(row=1, column=2, pady=20, padx=10)

withdraw_amount_button = tkinter.Button(withdraw_frame,
                                        text="Withdraw",
                                        bg="#A6E3E9",
                                        fg="black",
                                        font=("Arial", 16),
                                        command=withdraw_amount_fun)
withdraw_amount_button.grid(row=3, column=1, columnspan=2, pady=30)

back_button= tkinter.Button(withdraw_frame,width=8,text="Back",bg="#A6E3E9",fg="black",font=("Arial",16),command=back)
back_button.grid(row=4,column=1,columnspan=2,pady=5)



# deposit frame
deposit_label = tkinter.Label(deposit_frame,
                              text="PS Bank",
                              bg='#222831',
                              fg="#A6E3E9",
                              font=("Arial", 30, "bold"))
deposit_label.grid(row=0, column=1, columnspan=2, sticky="news", pady=40)

canvas=tkinter.Canvas(deposit_frame, width=100, height=100, highlightthickness=0)
img3=tkinter.PhotoImage(file="GUI/images.png")
canvas.create_image(31, 50, image=img3)
canvas.place(x=11, y=21)


deposit_amount_label = tkinter.Label(deposit_frame,
                                     text="Amount: ",
                                     bg='#222831',
                                     fg="#FFFFFF",
                                     font=("Arial", 16))
deposit_amount_label.grid(row=1,
                          column=0,
                          columnspan=2,
                          sticky="news",
                          pady=40)

deposit_entry = tkinter.Entry(deposit_frame, width=20, font=("Arial", 16))
deposit_entry.focus()
deposit_entry.grid(row=1, column=2, pady=20, padx=10)

deposit_amount_button = tkinter.Button(deposit_frame,
                                       text="Deposit",
                                       bg="#A6E3E9",
                                       fg="black",
                                       font=("Arial", 16),
                                       command=deposit_amount_fun)
deposit_amount_button.grid(row=3, column=1, columnspan=2, pady=30)


back_button2= tkinter.Button(deposit_frame,width=8,text="Back",bg="#A6E3E9",fg="black",font=("Arial",16),command=back)

back_button2.grid(row=4,column=1,columnspan=2,pady=5)




# balance frame
balance_label = tkinter.Label(balance_frame,
                              text="PS Bank",
                              bg='#222831',
                              fg="#A6E3E9",
                              font=("Arial", 30, "bold"))
balance_label.grid(row=0, column=3, columnspan=4, sticky="news", pady=40)

canvas=tkinter.Canvas(balance_frame, width=100, height=100, highlightthickness=0)
img4=tkinter.PhotoImage(file="GUI/images.png")
canvas.create_image(31, 50, image=img4)
canvas.place(x=5, y=21)



balance_amount_label = tkinter.Label(
  balance_frame,
  text=f"Your current balance is Rs: {current_balance}",
  bg='#222831',
  fg="#FFFFFF",
  font=("Arial", 16))
  
balance_amount_label.grid(row=2,
                          column=2,
                          columnspan=2,
                          sticky="news",
                          pady=40)

main_menu = tkinter.Button(balance_frame,
                           text="Return to main menu",
                           bg="#A6E3E9",
                           fg="black",
                           font=("Arial", 16),
                           command=main_menu_fun)
main_menu.grid(row=5, column=2, columnspan=2, pady=25)

exit = tkinter.Button(balance_frame,
                      text="Exit",
                      bg="#A6E3E9",
                      fg="black",
                      font=("Arial", 16),
                      command=exit_fun,
                      width=17)
exit.grid(row=6, column=2, columnspan=2, pady=5)

# frame.pack()
# frame2.pack()
show_frame(balance_frame)

window.mainloop()
