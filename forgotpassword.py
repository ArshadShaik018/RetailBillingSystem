from tkinter import *
from tkinter import messagebox

import pymysql

root = Tk()
root.config(bg='black')
root.geometry('1550x1500')
root.resizable(0, 0)
def submit():
    if usernameentry.get()=='' or emailentry== '' or passwordentry.get()=='' or confirmpasswordentry.get()=='':
        messagebox.showerror('Alert', 'Entry feilds must be entered')
        return
    elif passwordentry.get()!= confirmpasswordentry.get():
        messagebox.showerror('Alert','Password doesnt match')
    else:
        db = pymysql.connect(host='localhost', user='root', password='Shaik@123', database='registration_form')
        cur = db.cursor()

        query='select * from registration_details where email=%s'
        cur.execute(query, (emailentry.get()))

        row=cur .fetchone()
        if row == None:
            messagebox.showerror('Alert','This email does not exist')
            return
        else:
            query = 'update registration_details set password=%s where email=%s'
            cur.execute(query, (passwordentry.get(), emailentry.get()))
        db.commit()
        db.close()
        messagebox.showinfo('success', 'Successful Changes. Please login with the new password')

        usernameentry.delete(0,END)
        emailentry.delete(0,END)
        confirmpasswordentry.delete(0,END)


def show():
    passwordentry.config(show='')
    passwordicon.config(command=hide)

def hide():
    passwordentry.config(show='*')
    passwordicon.config(command=show)


def newone():
    root.destroy()
    import login_form

heading = Label(root, text='Forgot Password', bg='black', fg='white', font=('calibre', 40, 'bold'))
heading.place(x=530, y=165)

forgotframe = LabelFrame(root, text='', bg='gray20', fg='white', font=('arial', 20, 'bold'), relief=GROOVE, bd=10)
forgotframe.place(x=400, y=240)

usernamelabel = Label(forgotframe, text='User Name:', bg='gray20', fg='White', font=('arial', 25, 'bold'))
usernamelabel.grid(row=0, column=0, pady=10, padx=10, sticky='w')

usernameentry = Entry(forgotframe, width=24, bd=2, font=('calibre', 14, 'bold'), show='*')
usernameentry.grid(row=0, column=1, padx=10, pady=10)

passwordlabel = Label(forgotframe, text='Password:', bg='gray20', fg='White', font=('arial', 25, 'bold'))
passwordlabel.grid(row=2, column=0, pady=10, padx=10, sticky='w')

passwordentry = Entry(forgotframe, width=24, bd=2, font=('calibre', 14, 'bold'), show='*')
passwordentry.grid(row=2, column=1, padx=55, pady=10)

confirmpasswordlabel = Label(forgotframe, text='Confirm Password:', bg='gray20', fg='White', font=('arial', 25, 'bold'))
confirmpasswordlabel.grid(row=3, column=0, pady=10, padx=10, sticky='w')

confirmpasswordentry = Entry(forgotframe, width=24, bd=2, font=('calibre', 14, 'bold'), show='*')
confirmpasswordentry.grid(row=3, column=1, padx=55, pady=10)

passwordicon = Checkbutton(forgotframe, width=1, bg='gray20', fg='black',command=show)
passwordicon.place(x=650, y=150)

trylogin = Label(forgotframe, text='Try to Login', bg='gray20', fg='red', font=('arial', 16, 'bold'))
trylogin.grid(row=4, column=0, pady=40, sticky='w')

backbutton = Button(forgotframe, text='Login', bd=5, width=10, font=('calibre', 12, 'bold'), bg='orange', fg='black',
                    command=newone)
backbutton.place(x=10, y=260)

submitbtn = Button(forgotframe, text='Submit', bd=5, width=10, font=('calibre', 15, 'bold'), bg='green', fg='black',command=submit)
submitbtn.place(x=300, y=290)


emaillabel = Label(forgotframe, text='Email:', bg='gray20', fg='White', font=('arial', 25, 'bold'))
emaillabel.grid(row=1, column=0, pady=10, padx=10, sticky='w')

emailentry = Entry(forgotframe, width=24, bd=2, font=('calibre', 14, 'bold'), show='*')
emailentry.grid(row=1, column=1, padx=10, pady=10)


root.mainloop()
