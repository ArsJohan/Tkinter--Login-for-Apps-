from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


class GUI_USER():
    def __init__(self,name):
         self.root = Tk()
         self.mainFrame = Frame(self.root, bg="#f0f0f0")
         self.mainFrame.pack(fill=BOTH, expand=1)
         self.User_name = Label(self.mainFrame, text=f"{name}", font=("times new roman", 40, "bold"), bg="#f0f0f0", fg="black").place(x=0, y=0, relwidth=1)
         self.root.title("Hospital Management System")
         self.root.geometry("800x800")
         self.root.resizable(False, False)
         self.root.config(bg="#f0f0f0")
         self.root.mainloop()
         
