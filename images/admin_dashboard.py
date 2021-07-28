import tkinter.ttk as ttk
from tkinter import *
from PIL import ImageTk, Image
import os
import time
from datetime import datetime


class dashboard:
    def __init__(self, root):
        self.root = root
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        # use the next line if you also want to get rid of the titlebar
        root.overrideredirect(1)
        root.geometry("%dx%d+0+0" % (w, h))
        self.root.title("Attendance Management System")
        self.root.bind("<Escape>", exit)

        self.background = ImageTk.PhotoImage(file="images/background.jpg")
        self.faceimg = ImageTk.PhotoImage(file="images/face.jpg")
        self.top_icon = ImageTk.PhotoImage(file="images/fronttopleft.jpg")
        self.bottom_image = ImageTk.PhotoImage(file="images/frontrightbottom.jpg")

        # Background Image
        bg_lb = Label(self.root, image=self.background).pack()

        # Top frame
        self.top_frame = Frame(self.root, bg="#0c2454")
        self.top_frame.place(x=0, y=0, relwidth=1)
        # Top Left Image
        self.lb1 = Label(self.top_frame, image=self.top_icon, bd=0, )
        self.lb1.grid(row=0, column=0)

        # Top Title
        self.title = Label(self.top_frame, text="FACIAL RECOGNIZATION ATTENDANCE SYSTEM", bg="#0c2454", fg="#87a81b",
                           height="3", font='Algerian 37 bold underline', width=36, padx=20)
        self.title.grid(row=0, column=1)

        # Dashboard Bar
        self.dashboard=Frame(self.root, bg='yellow',)
        self.dashboard.place(x=0, y=171, relwidth=1)

        self.dashlb=Label(self.dashboard, text="Welcome", fg='White', font='Arial 18 bold', bg='#0c2454' )
        self.dashlb.grid(row=0, column=0, padx=20)

        self.clock_lb = Label(self.dashboard, compound=LEFT, fg='White', bg='#0c2454', font='Arial 18 bold', )
        self.clock_lb.grid(row=0, column=1, )
        self.time()







        # Code for about
        self.bottom_frame = Frame(self.root, )
        self.bottom_frame.place(x=1160, y=600)

        self.botimglb = Label(self.bottom_frame, image=self.bottom_image, bd=0)
        self.botimglb.grid(row=0, columnspan=2)

        self.bottomlbl = Label(self.bottom_frame, text="Designed & Developed By:", wraplength=100, width=10, anchor="w",
                               justify=LEFT, font='Arial 11 bold', bg="#0c2454", fg="#87a81b", )
        self.bottomlbl.grid(row=1, column=0)

        self.bottomlb2 = Label(self.bottom_frame, text="Sajal Bansal, Vipul Goyal & Abhinav Joshi", wraplength=100,
                               width=11, justify=LEFT, anchor="w", font='Arial 11 bold', bg="#0c2454", fg="White", )
        self.bottomlb2.grid(row=1, column=1)

    def time(self):

        # self.now = datetime.now.today()
        self.now= datetime.today().strftime('%d-%m-%Y  %I:%M:%S:%p')
        # today = datetime.date.today().strftime("%d-%m-%Y")
        # # print(today)
        # self.string=self.now.strftime('%I:%M:%S:%p %d-%m-%y')
        self.clock_lb.config(text=self.now)
        self.clock_lb.after(1000, self.time)


root=Tk()
objd=dashboard(root)
root.mainloop()


