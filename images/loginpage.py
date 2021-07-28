from tkinter import *
from PIL import ImageTk
from  tkinter import messagebox
import sqlite3 as db
import time
import os
class Login_System:
    def __init__(self, root):

        self.root = root
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.overrideredirect(1)
        root.geometry("%dx%d+0+0" % (w, h))
        self.root.title("Attendance Management System")
        self.root.bind("<Escape>", exit)

        # variables
        self.uname=StringVar()
        self.passw=StringVar()
        self.optionvalue=StringVar()

        # images
        self.background=ImageTk.PhotoImage(file="images/background.jpg")
        self.man_icon=ImageTk.PhotoImage(file="images/man.jpg")
        self.user_icon=ImageTk.PhotoImage(file="images/user.jpg")
        self.pass_icon=ImageTk.PhotoImage(file="images/pass.jpg")
        self.top_icon=ImageTk.PhotoImage(file="images/fronttopleft.jpg")
        self.bottom_image=ImageTk.PhotoImage(file="images/frontrightbottom.jpg")
        self.admin_icon=ImageTk.PhotoImage(file="images/admin.jpg")

        # Background Image
        bg_lb = Label(self.root, image=self.background).pack()

        # Top frame
        self.top_frame=Frame(self.root, bg="#112034")
        self.top_frame.place(x=0, y=0, relwidth=1)

        # Top Left Image
        self.lb1=Label(self.top_frame, image=self.top_icon, bd=0)
        self.lb1.grid(row=0, column=0)

        # Top Title
        self.title=Label(self.top_frame, text="FACIAL RECOGNIZATION ATTENDANCE SYSTEM",bg="#112034", fg="#87a81b", height="3", font='Algerian 37 bold underline', width=36, padx=20)
        self.title.grid(row=0, column=1)

        # Login Frame
        self.Login_frame=LabelFrame(self.root, bg="#112034", )
        self.Login_frame.place(x=460,y=200,)

        # Main Icon
        self.Logo_lb=Label(self.Login_frame, image=self.man_icon,compound=TOP, text="Login :-", bg="#112034", font=("Arial", 22, "bold", "underline"), fg="White").grid(row=0, columnspan=3, pady=20)

        # Username
        self.user_lb=Label(self.Login_frame, text="Username", image=self.user_icon, compound=LEFT, font=("Arial", 20, "bold"), bg="#112034", fg="white",)
        self.user_lb.grid(row=1, column=0,  padx=20, sticky=W)

        # Username Semicolon
        self.usersem = Label(self.Login_frame, text=":",bg="#112034", fg="white", font=("Arial", 20, "bold"),)
        self.usersem.grid(row=1, column=1,)

        # Password
        self.pwd_lb = Label(self.Login_frame, text="Password", image=self.pass_icon, compound=LEFT, font=("Arial", 20, "bold"), bg="#112034", fg="white", )
        self.pwd_lb.grid(row=2, column=0, padx=20, sticky=W)

        # Password Semicolon
        self.pwdsem = Label(self.Login_frame, text=":", bg="#112034", fg="white",font=("Arial", 20, "bold"),)
        self.pwdsem.grid(row=2, column=1,)

        # Type
        self.type_lb = Label(self.Login_frame, text="User Type", image=self.admin_icon, compound=LEFT, font=("Arial", 20, "bold"), bg="#112034", fg="white", )
        self.type_lb.grid(row=3, column=0, padx=20, sticky=W)

        # Type Semicolon
        self.type_sem = Label(self.Login_frame, text=":", bg="#112034", fg="white", font=("Arial", 20, "bold"), )
        self.type_sem.grid(row=3, column=1, )


        # Username Entry
        self.user_txt=Entry(self.Login_frame,  textvariable=self.uname, width=14, font=("Arial", 14, "bold"),)
        self.user_txt.grid(row=1, column=2, padx=20, sticky=W)

        # Password Entry
        self.pwd_txt = Entry(self.Login_frame, width=14, show="*", textvariable=self.passw, font=("Arial", 14, "bold"),)
        self.pwd_txt.grid(row=2, column=2, padx=20, sticky=W)

        # Type Entry
        optionvalue=["Admin", "User"]
        self.optionvalue.set("Choose")
        self.type_txt = OptionMenu(self.Login_frame, self.optionvalue, *optionvalue )
        self.type_txt.config(fg="White",font=("Arial", 18, "bold"), bg="#112034", highlightthickness=0)
        self.type_txt["menu"].config(fg="White",font=("Arial", 18, "bold"), bg="#112034" ,)
        self.type_txt.grid(row=3, column=2, padx=20, sticky=W)

        # Login Button
        self.login_btn = Button(self.Login_frame, text="LOGIN", command=self.login,  width=12, height=1,)
        self.login_btn.grid(row=4,  pady=20, sticky=E)

        # Quit Button
        self.login_btn = Button(self.Login_frame, text="QUIT", command=self.quit, width=12, height=1,)
        self.login_btn.grid(row=4, column=2, sticky=W, pady=20, )

        # Bottom Frame
        self.bottom_frame=Frame(self.root)
        self.bottom_frame.place(x=1160,y=600)

        # Bottom Image
        self.botimglb=Label(self.bottom_frame, image=self.bottom_image, bd=0)
        self.botimglb.grid(row=0, columnspan=2)

        # Bottom Label1
        self.bottomlb1 = Label(self.bottom_frame, text="Designed & Developed By:", wraplength=100, width=10, anchor="w", justify=LEFT, font='Arial 11 bold', bg="#112034", fg="#87a81b", )
        self.bottomlb1.grid(row=1, column=0)

        # Bottom Label2
        self.bottomlb2 = Label(self.bottom_frame, text="Sajal Bansal, Vipul Goyal & Abhinav Joshi", wraplength=100, width=11, justify=LEFT, anchor="w", font='Arial 11 bold', bg="#112034", fg="White", )
        self.bottomlb2.grid(row=1, column=1)


    def login(self):
        conn = db.connect('Attendance.db')
        cur = conn.cursor()
        find_user=("SELECT * FROM Login WHERE  admin_id = ? AND admin_pass = ?")
        cur.execute(find_user, [(self.uname.get()),(self.passw.get())])
        results=cur.fetchall()

        if self.uname.get()=="" or self.passw.get()=="" or self.optionvalue.get()=="Choose":
            messagebox.showerror("Error", "All Fields Are Required")
        elif results:
            if self.optionvalue.get()=="Admin":
                messagebox.showinfo("Successfull", f"Welcome {self.uname.get()}")
                time.sleep(0.1)
                os.system('python admin_dashboard.py')
                exit()
            elif self.optionvalue.get()=="User":
                messagebox.showinfo("Successfull", f"Welcome {self.uname.get()}")
                time.sleep(0.1)
                os.system('python user_dashboard.py')
        else:
            messagebox.showerror("Error", "Invalid Username or Password",)
        cur.close()
        conn.commit()
        conn.close()





    def quit(self):
        MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'question')
        if MsgBox == 'yes':
            self.root.destroy()

root=Tk()
objl=Login_System(root)
root.mainloop()