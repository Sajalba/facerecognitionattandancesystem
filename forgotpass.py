from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import sqlite3 as db
import os

def quit():
    MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'question')
    if MsgBox == 'yes':
        root.destroy()

def update():
    conn = db.connect('Attendance.db')
    cur = conn.cursor()
    if (passw.get()=="" or passwr.get()==""):
        messagebox.showerror("Error", "All Fields Are Required")
    elif(passw.get() != passwr.get()):
        messagebox.showerror("Error", "Password Mismatched")
    else:
        update_query = ("UPDATE Login SET pass = ? WHERE id= ?")
        run=cur.execute(update_query, (passw.get(), eid))

        if run:
            msg=messagebox.showinfo("Successfull", "Password Changed Successfully")
            if msg=='ok':
                os.system('py loginpage.py')
                root.destroy()
        else:
            messagebox.showerror("Oops", "Something Went Wrong")



    cur.close()
    conn.commit()
    conn.close()


class ChangePass:
    def __init__(self, root, passw, passwr, eid ):
        self.root = root
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.overrideredirect(1)
        root.geometry("%dx%d+0+0" % (w, h))
        self.root.title("Attendance Management System")
        self.root.bind("<Escape>", exit)




        # images
        self.background=ImageTk.PhotoImage(file="images/background.jpg")
        self.man_icon=ImageTk.PhotoImage(file="images/man.jpg")
        self.user_icon=ImageTk.PhotoImage(file="images/user.jpg")
        self.pass_icon = ImageTk.PhotoImage(file="images/pass.jpg")
        self.top_icon=ImageTk.PhotoImage(file="images/fronttopleft.jpg")

        # Background Image
        bg_lb = Label(self.root, image=self.background).pack()

        # Top frame
        self.top_frame=Frame(self.root, bg="#112034")
        self.top_frame.place(x=0, y=0, relwidth=1)

        # Top Left Image
        self.lb1=Label(self.top_frame, image=self.top_icon, bd=0)
        self.lb1.grid(row=0, column=0)

        # Top Title
        self.title=Label(self.top_frame, text="FACE RECOGNIZATION ATTENDANCE SYSTEM",bg="#112034", fg="#87a81b", height="3", font='Algerian 37 bold underline', width=36, padx=20)
        self.title.grid(row=0, column=1)

        # Login Frame
        self.Login_frame=LabelFrame(self.root, bg="#112034", )
        self.Login_frame.place(x=460,y=200,)

        # Main Icon
        self.Logo_lb=Label(self.Login_frame, image=self.man_icon,compound=TOP, text="Change Password:-", bg="#112034", font=("Arial", 22, "bold", "underline"), fg="White").grid(row=0, columnspan=3, pady=20)

        # Username
        self.user_lb = Label(self.Login_frame, text="Emp Id", image=self.user_icon, compound=LEFT,
                             font=("Arial", 20, "bold"), bg="#112034", fg="white")
        self.user_lb.grid(row=1, column=0, padx=20, sticky=W)

        # Username Semicolon
        self.usersem = Label(self.Login_frame, text=":", bg="#112034", fg="white", font=("Arial", 20, "bold"), )
        self.usersem.grid(row=1, column=1, )

        # Username Entry

        self.user_txt = Entry(self.Login_frame, width=14, font=("Arial", 14, "bold"))
        self.user_txt.insert(0, eid)
        self.user_txt.config(state='disabled')
        self.user_txt.grid(row=1, column=2, padx=20, sticky=W)

        # Username
        self.user_lb=Label(self.Login_frame, text="Password", image=self.pass_icon, compound=LEFT, font=("Arial", 20, "bold"), bg="#112034", fg="white")
        self.user_lb.grid(row=2, column=0,  padx=20, sticky=W)

        # Username Semicolon
        self.usersem = Label(self.Login_frame, text=":",bg="#112034", fg="white", font=("Arial", 20, "bold"),)
        self.usersem.grid(row=2, column=1,)

        # Username Entry
        self.user_txt=Entry(self.Login_frame, width=14, font=("Arial", 14, "bold"), textvariable=passw, show="*")
        self.user_txt.grid(row=2, column=2, padx=20, sticky=W)

        # Username
        self.user_lb = Label(self.Login_frame, text="Re-Enter", image=self.pass_icon, compound=LEFT,
                             font=("Arial", 20, "bold"), bg="#112034", fg="white")
        self.user_lb.grid(row=3, column=0, padx=20, sticky=W)

        # Username Semicolon
        self.usersem = Label(self.Login_frame, text=":", bg="#112034", fg="white", font=("Arial", 20, "bold"), )
        self.usersem.grid(row=3, column=1, )

        # Username Entry
        self.user_txt = Entry(self.Login_frame, width=14, font=("Arial", 14, "bold"), textvariable=passwr, show="*")
        self.user_txt.grid(row=3, column=2, padx=20, sticky=W)


        # Submit Button
        self.success_btn = Button(self.Login_frame, text="Update", width=12, height=1, justify=CENTER, command=update)
        self.success_btn.grid(row=4, columnspan=3,  pady=20, sticky=W, padx=80)

        # Quit Button
        self.resend_btn = Button(self.Login_frame, text="Quit", width=12, height=1, command=quit, )
        self.resend_btn.grid(row=4, columnspan=3, sticky=E, pady=20, padx=80)


def fileopen():
    global eid
    with open('tempfile.temp', "r") as f:
        data = f.readlines()
        eid = data[0].rstrip()
        return eid

if __name__ == '__main__':
    fileopen()
    root = Tk()
    passw = StringVar()
    passwr = StringVar()
    objo = ChangePass(root, passw, passwr, eid)
    root.mainloop()
