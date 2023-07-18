from tkinter import *
from tkinter import messagebox
from Users import User


root = Tk()
mainFrame = Frame(root)
name_text = Entry(mainFrame, font=("Arial", 12), bg="lightblue")
password_text = Entry(mainFrame, font=("Arial", 12), bg="lightblue",show="*")
def create_app():
    #Ventana Principal
   
    root.title("Login User")
    root.geometry("400x400")

    #Frame
    mainFrame.pack()
    mainFrame.config(width=400, height=400) #bg="darkblue"


    #Labels
    title = Label(mainFrame, text="Login User", font=("Arial", 20),  fg="Black")
    title.grid(row=0, column=0, columnspan=2, pady=20)
    name_label = Label(mainFrame, text="Name:", font=("Arial", 12),fg="Black")
    name_label.grid(row=1, column=0, pady=20)
    password_label = Label(mainFrame, text="Password:", font=("Arial", 12),  fg="Black")
    password_label.grid(row=2, column=0, pady=20)

    #Text Box

    name_text.grid(row=1, column=1, pady=20)
    password_text.grid(row=2, column=1, pady=20)

    #Buttons

    login_button = Button(mainFrame, text="Login", font=("Arial", 12), bg="lightblue", command=Startsesion)

    login_button.grid(row=3, column=0, pady=20)

    register_button = Button(mainFrame, text="Register", font=("Arial", 12), bg="lightblue", command=Register)

    register_button.grid(row=3, column=1, pady=20)
    root.mainloop()
 #Functions
def Startsesion():
    for user in users:
        if user.name == name_text.get():
            Connected = user.connect(password_text.get())
            if Connected == True:
                messagebox.showinfo("Login", f"Welcome back to the app {user.name}!\n")
            else:
                messagebox.showerror("Login", Connected)
            break
    else:
            messagebox.showerror("Login", "No found this account")
    
def Register():
    name = name_text.get()
    password = password_text.get()
    new_user = User(name, password)
    users.append(new_user)
    messagebox.showinfo("Register", f"Welcome {new_user.name}!\n")
    name_text.delete(0, END)
    password_text.delete(0, END)
    name_text.focus()
    
    

if __name__ == "__main__":
    user1 = User("Johan","1234")
    users = [user1]
    create_app()