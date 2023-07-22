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
        self.mainFrame_img = Frame(self.root)
        self.name_text = Entry(self.mainFrame, font=("Arial", 12), bg="lightblue", border=0)
        self.password_text = Entry(self.mainFrame, font=("Arial", 12), bg="lightblue", show="*", border=0)
        
        #Variables 
        color_background = "#fcfefd"
        color_font = "#071a3b"
        #Ventana Principal.
        self.root.title("Login User")
        self.root.geometry("600x400")
        self.root.config(bg=color_background)
        
        #Frame
        self.mainFrame.pack(fill=BOTH,side="right", expand=1)
        self.mainFrame.config(width=400, height=400, borderwidth= 20, background= color_background) 
        self.mainFrame_img.pack(fill=BOTH, side="left", expand=1)
        self.mainFrame_img.config(width=400, height=400, background= color_background)
        #image
        img = ImageTk.PhotoImage(Image.open("Images\Logo.jpg"))
        panel = Label(self.mainFrame_img, image=img, border=0)
        panel.grid(row=0, column=0)
        
        

        #Labels
        name_label = Label(self.mainFrame, text="Name", font=("Optima", 10),fg=color_font, background=color_background)
        name_label.grid(row=0, column=0)
        self.error_name = Label(self.mainFrame, text="", font=("Optima", 8), fg="Red", background=color_background)
        self.error_name.grid(row=2, column=0)
        password_label = Label(self.mainFrame, text="Password", font=("Optima", 10),  fg=color_font, background=color_background)
        password_label.grid(row=3, column=0)
        self.error_password = Label(self.mainFrame, text="", font=("Optima", 8), fg="Red", background=color_background)
        self.error_password.grid(row=5, column=0)
        
        #Text Box
        self.name_text.grid(row=1, column=0, pady=10)
        self.password_text.grid(row=4, column=0, pady=10)
        
        
        #Buttons Login and Register
        login_button = Button(self.mainFrame, text="Login", font=("Optima", 12), fg=color_font,bg="#28e0be",activebackground=color_font,activeforeground="#28e0be", command=self.start_session, border=0, width=15)
        login_button.grid(row=6, column=0, pady=10)

        register_button = Button(self.mainFrame, text="Register", font=("Optima", 12),fg=color_font,bg="#28e0be",activebackground=color_font, activeforeground="#28e0be", command=self.register, border=0, width=10)
        register_button.grid(row=7, column=0)
        
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
                    self.root.destroy()
                    GUI_USER(user) 
                    #add when you want to close the window, then Logging
                else:
                    self.error_name.config(text="Incorrect Name or Incorrect password")
                    self.error_password.config(text="Incorrect Name or Incorrect password")
                break
        if self.name_text.get() == "" or self.password_text.get() == "":
             self.error_name.config(text="Please fill all the fields"), self.error_password.config(text="Please fill all the fields")
        else:
             self.error_name.config(text="No found this account")
             self.error_password.config(text=None)
    #Fuction register
    # Verified if the text box is not empty and the name and password are more than 3 characters
    # Verified if user not registered, then add it to the list of users
    # Create a New User, show message "Register, Welcome User" and clean the text box
    def register(self): 
        if self.name_text.get() == "" or self.password_text.get() == "":
            return self.error_name.config(text="Please fill all the fields"), self.error_password.config(text="Please fill all the fields")
        elif len(self.name_text.get()) < 3:
            return self.error_name.config(text="Please enter a name with more than 3 characters"), self.error_password.config(text="")
        elif len(self.password_text.get()) < 4:
            return self.error_password.config(text="Please enter a password with more than 4 characters")
        elif self.name_text.get() in [user.name for user in self.users]	:
            return self.error_name.config(text="This name already exist"),self.error_password.config(text=None)
        else:
            name = self.name_text.get()
            password = self.password_text.get()
            new_user = User(name, password)
            self.users.append(new_user)
            messagebox.showinfo("Register", f"Welcome {new_user.name}!\n")
            self.name_text.delete(0, END)
            self.password_text.delete(0, END)
            self.name_text.focus()
        
        
if __name__ == "__main__":
    Login()
    #Only testing this window, not the main window