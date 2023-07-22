from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from Users import User

class GUI_USER():
    
    def __init__(self,user):
        #Variables of Properties
         self.color_background = "#302C2C"
         self.color_backgroundbuttons = "#28e0be"
         self.color_fonts = "#28e0be"
         self.user = user
         #Main Window
         self.root = Tk()
         self.mainFrame = Frame(self.root, bg="#f0f0f0")
         self.mainFrame.pack(fill="both", expand=1)
         self.root.title("Notes")
         self.root.geometry("800x600")
         self.root.resizable(False, False)
         self.root.config(bg="#f0f0f0")
         
         #Menu
         self.name = Label(self.mainFrame,text="Welcome, "+self.user.name,font=("Arial",20),bg="#302C2C",fg=self.color_fonts, border=50, justify="center")
         self.name.place(x=0, y=0, relwidth=1)
         self.logout = Button(self.mainFrame,text="Logout",font=("Arial",10),bg=self.color_backgroundbuttons,fg="black",width=10,border=0,command=self.Logout).place(x=720, y=0)
         self.menu = Button(self.mainFrame,text="Menu",font=("Arial",10),bg=self.color_backgroundbuttons,width=10,fg="black",border=0).place(x=0, y=120)
         
         self.root.mainloop()
        
    def Logout(self):
        messagebox.showinfo("Logout",self.user.disconnect())
        self.root.destroy()