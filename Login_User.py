from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from Users import User
from User_Interface import GUI_USER
class Login:
    user = User("Johan", "1234")
    users = [user]
    root = Tk()
    mainFrame = Frame(root)
    name_text = Entry(mainFrame, font=("Arial", 12), bg="lightblue")
    password_text = Entry(mainFrame, font=("Arial", 12), bg="lightblue",show="*")
    def __init__(self):
        #Ventana Principal.
        Login.root.title("Login User")
        Login.root.geometry("600x400")
        #Frame
        Login.mainFrame.pack(side="right")
        Login.mainFrame.config(width=400, height=400) #bg="darkblue"
        #Labels
        title = Label(Login.mainFrame, text="Login User", font=("Arial", 20),  fg="Black")
        title.grid(row=0, column=0, columnspan=2, pady=20)
        name_label = Label(Login.mainFrame, text="Name:", font=("Arial", 12),fg="Black")
        name_label.grid(row=1, column=0, pady=20)
        password_label = Label(Login.mainFrame, text="Password:", font=("Arial", 12),  fg="Black")
        password_label.grid(row=2, column=0, pady=20)
        #Text Box
        Login.name_text.grid(row=1, column=1, pady=20)
        Login.password_text.grid(row=2, column=1, pady=20)
        #Buttons

        login_button = Button(Login.mainFrame, text="Login", font=("Arial", 12), bg="lightblue", command=Login.Startsesion)

        login_button.grid(row=3, column=0, pady=20)

        register_button = Button(Login.mainFrame, text="Register", font=("Arial", 12), bg="lightblue", command=Login.Register)

        register_button.grid(row=3, column=1, pady=20)
        Login.root.mainloop()
    #Functions
    def Startsesion():
        for user in Login.users:
            if user.name == Login.name_text.get():
                Connected = Login.user.connect(Login.password_text.get())
                if Connected == True:
                    messagebox.showinfo("Login", f"Welcome back to the app {Login.user.name}!\n")
                    GUI_USER(Login.user.name)
                else:
                     if Connected == "Your account is now locked":
                         messagebox.showerror("Login", f"{Connected}")
                         Login.name_text(state=DISABLED)
                         Login.password_text(state=DISABLED)
                     else:
                         messagebox.showerror("Login", f"{Connected}")
                break
        else:
                messagebox.showerror("Login", "No found this account")
    def Register():
        name = Login.name_text.get()
        password = Login.password_text.get()
        new_user = User(name, password)
        Login.users.append(new_user)
        messagebox.showinfo("Register", f"Welcome {new_user.name}!\n")
        Login.name_text.delete(0, END)
        Login.password_text.delete(0, END)
        Login.name_text.focus()
        
    