from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from Users import User
from User_Interface import GUI_USER

class Login:
    def __init__(self):
        self.users = [User("Johan", "1234")]#-> Here to save your users previous registered
        self.root = Tk()
        self.mainFrame = Frame(self.root)
        self.name_text = Entry(self.mainFrame, font=("Arial", 15), bg="white", border=0)
        self.name_text.config(width=25)
        self.password_text = Entry(self.mainFrame, font=("Arial", 15), bg="white", show="*", border=0)
        self.password_text.config(width=25)
        
        #Variables of the Properties
        color_background = "#fcfefd"
        color_font = "#071a3b"
        x_label = 470
        y_label =180
        x_img = 50
        y_img = 70
        
        #Main Window
        self.root.title("Login User")
        self.root.geometry("800x600")
        self.root.config(bg=color_background)
        self.root.resizable(False, False)
        #Frame
        self.mainFrame.pack(fill=BOTH, expand=1)
        self.mainFrame.config(background= color_background) 
        #images
        img = ImageTk.PhotoImage(Image.open("Tkinter-Project/images/Logo.jpg"))
        panel = Label(self.mainFrame, image=img, border=0)
        panel.place(x=x_img, y=y_img)
        log_login = ImageTk.PhotoImage(Image.open("Tkinter-Project/images/user.png"))
        log_panel = Label(self.mainFrame, image=log_login, border=0, bg=color_background)
        log_panel.place(x=x_label+100, y=100)
        
    
        #Lines
        line_V= Label(self.mainFrame, text="",background=color_font, borderwidth=0.1)
        line_V.place(x=430, y=100,relheight=0.70)
        
        line_UnderName= Label(self.mainFrame, text="",background="#FE6894", borderwidth=0.1)
        line_UnderName.place(x=x_label, y=y_label+68,relwidth=0.35, relheight=0.0040)
        line_UnderPass= Label(self.mainFrame, text="",background="#FE6894", borderwidth=0.1)
        line_UnderPass.place(x=x_label, y=y_label+163,relwidth=0.35, relheight=0.0040)
        
        line_V_Button= Label(self.mainFrame, text="",background="#FE6894", borderwidth=0.1)
        line_V_Button.place(x=x_label+140, y=y_label+220,relheight=0.060)

        #Labels
        name_label = Label(self.mainFrame, text="Name", font=("Optima", 12, "bold"),fg=color_font, background=color_background, border=1)
        name_label.place(x=x_label,y=y_label+10)
        self.error_name = Label(self.mainFrame, text="", font=("Optima", 8), fg="Red", background=color_background)
        self.error_name.place(x=x_label, y=y_label + 70)
        password_label = Label(self.mainFrame, text="Password", font=("Optima",12, "bold"),  fg=color_font, background=color_background)
        password_label.place(x=x_label, y=y_label + 110)
        self.error_password = Label(self.mainFrame, text="", font=("Optima", 8), fg="Red", background=color_background)
        self.error_password.place(x=x_label, y=y_label +165)
        
        #Text Box
        self.name_text.place(x=x_label, y=y_label+40)
        self.password_text.place(x=x_label, y=y_label+135)
        
        
        #Buttons Login and Register
        login_button = Button(self.mainFrame, text="Sign In",font=("Optima", 13,"bold"), fg=color_font,bg=color_background,activebackground=color_background,activeforeground="#FE6894", command=self.start_session, border=0, cursor="hand2")
        login_button.place(x=x_label+50, y=y_label+220)
        register_button = Button(self.mainFrame, text="Sign Up",font=("Optima", 12, "bold"),fg=color_font,bg= color_background,activebackground=color_background, activeforeground="#FE6894", command=self.register, border=0, cursor="hand2")
        register_button.place(x=x_label+160, y=y_label+220)

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
                    GUI_USER(user) #--> Here put the name of the class of window what you prefer 
                    #ALT + CLIC --> to open the class of window
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
        
