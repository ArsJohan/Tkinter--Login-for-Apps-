from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from Users import User
from User_Interface import GUI_USER
class Login:
    def __init__(self):
        self.users = [User("Johan", "1234")]
        self.root = Tk()
        self.mainFrame = Frame(self.root)
        self.name_text = Entry(self.mainFrame, font=("Arial", 12), bg="lightblue")
        self.password_text = Entry(self.mainFrame, font=("Arial", 12), bg="lightblue", show="*")
        
        #Ventana Principal.
        self.root.title("Login User")
        self.root.geometry("600x400")
        
        #Frame
        self.mainFrame.pack(side="right")
        self.mainFrame.config(width=400, height=400) #bg="darkblue"
        
        #Labels
        title = Label(self.mainFrame, text="Login User", font=("Arial", 20),  fg="Black")
        title.grid(row=0, column=0, columnspan=2, pady=20)
        name_label = Label(self.mainFrame, text="Name:", font=("Arial", 12),fg="Black")
        name_label.grid(row=1, column=0, pady=20)
        password_label = Label(self.mainFrame, text="Password:", font=("Arial", 12),  fg="Black")
        password_label.grid(row=2, column=0, pady=20)
        
        #Text Box
        self.name_text.grid(row=1, column=1, pady=20)
        self.password_text.grid(row=2, column=1, pady=20)
        
        #Buttons Login and Register
        login_button = Button(self.mainFrame, text="Login", font=("Arial", 12), bg="lightblue", command=self.start_session)
        login_button.grid(row=3, column=0, pady=20)

        register_button = Button(self.mainFrame, text="Register", font=("Arial", 12), bg="lightblue", command=self.register)
        register_button.grid(row=3, column=1, pady=20)
        
        self.root.mainloop()
        
    #Function star_session
    #Verificated if user exist and password is correct then open other window call GUI_USER
    #Show error if user or password is incorrect
    #Locked the login if user try more than 3 times wrong password
    def start_session(self): 
        for user in self.users:
            if user.name == self.name_text.get():
                connected = user.connect(self.password_text.get())
                if connected == True:
                    messagebox.showinfo("Login", f"Welcome back to the app {user.name}!\n")
                    GUI_USER(user.name)
                else:
                    if connected == "Your account is now locked":
                        messagebox.showerror("Login", f"{connected}")
                        self.name_text(state=DISABLED)
                        self.password_text(state=DISABLED)
                    else:
                        messagebox.showerror("Login", f"{connected}")
                break
        else:
            messagebox.showerror("Login", "No found this account")
    #Fuction register
    # Create a New User, add it to the list of users, show message "Register, Welcome User" and clean the text box
    def register(self): 
        name = self.name_text.get()
        password = self.password_text.get()
        new_user = User(name, password)
        self.users.append(new_user)
        messagebox.showinfo("Register", f"Welcome {new_user.name}!\n")
        self.name_text.delete(0, END)
        self.password_text.delete(0, END)
        self.name_text.focus()