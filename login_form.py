from tkinter import *
from tkinter import messagebox
import pymysql

root=Tk()
root.resizable(0,0)
root.config(bg='black')
root.title('Login Form')
root.geometry('1530x1500')


def forgot():
    root.destroy()
    import forgotpassword

def show():
    passwordentry.config(show='')
    passwordicon.config(command=hide)
def hide():
    passwordentry.config(show='*')
    passwordicon.config(command=show)

def On_FocusEmailIn(event):
    emailentry.delete(0,END)

def On_FocusEmailOut(event):
    name = emailentry.get()
    if name == '':
        emailentry.insert(0, '@email.com')


def On_FocusPasswordIn(event):
    passwordentry.delete(0,END)

def On_FocusPasswordOut(event):
    name=passwordentry.get()
    if name=='':
        passwordentry.insert(0,'Password')


def createaccount():
    root.destroy()
    import registrationform

def login():
    if emailentry.get()=='':
        messagebox.showerror('ALERT','Please enter your email')
    elif passwordentry.get()=='':
        messagebox.showerror('ALERT','Please enter your Password')

    else:
        db = pymysql.connect(host='localhost', user='root', password='Shaik@123', database='registrationform')
        cur = db.cursor()
        query='select * from registrationdetails where password=%s and email=%s'
        cur.execute(query,(passwordentry.get(),emailentry.get()))

        row=cur.fetchone()
        if row == None:
            messagebox.showerror('alert','Incorrect email or Password')
            return
        else:
            messagebox.showinfo('sucess', 'login Succesful')
            root.destroy()
            import retailbillingsystem




loginframe=LabelFrame(root, text='',bg='gray20',fg='white',font=('arial',20,'bold'),relief=GROOVE,bd=10)
loginframe.place(x=480, y=240)


emaillabel=Label(loginframe, text='Email:',bg='gray20',fg='White',font=('arial',25,'bold'))
emaillabel.grid(row=0,column=0,pady=10,padx=10,sticky='w')

emailentry=Entry(loginframe, width=24,bd=2,font=('calibre',14,'bold'))
emailentry.grid(row=0,column=1,padx=55,pady=10)

passwordlabel=Label(loginframe, text='Password:',bg='gray20',fg='White',font=('arial',25,'bold'))
passwordlabel.grid(row=1,column=0,pady=10,padx=10,sticky='w')

passwordentry=Entry(loginframe, width=24,bd=2,font=('calibre',14,'bold'),show='*')
passwordentry.grid(row=1,column=1,padx=55,pady=10)

donthaveaccnt=Label(loginframe, text="Don't have an account?",bg='gray20',fg='blue',font=('calibre',12,'bold'))
donthaveaccnt.grid(row=2, column=0,pady=20,padx=10)

createaccount=Button(loginframe, text=' Create New Account', bg='yellow',fg='black',font=('arial',14,'bold'),command=createaccount)
createaccount.place(x=10,y=180)

forgetpassword=Button(loginframe, text='Forget Password', bg='gray20',fg='white',font=('arial',12,'bold'),bd=0,command=forgot)
forgetpassword.place(x=385,y=120)


passwordicon=Checkbutton(loginframe, width=1,bg='gray20',command=show)
passwordicon.place(x=545,y=85)


loginbutton=Button(loginframe, text='Login', bg='white',fg='black',font=('arial',19,'bold'),bd=5,width=8,command=login)
loginbutton.grid(row=3,column=1,pady=20,padx=50,sticky='w')

heading=Label(root, text='Login Form', bg='black',fg='white',font=('calibre',40, 'bold'))
heading.place(x=650,y=170)


emailentry.insert(0, 'email@.com')
passwordentry.insert(0,'password')

emailentry.bind('<FocusIn>',On_FocusEmailIn)
emailentry.bind('<FocusOut>',On_FocusEmailOut)

passwordentry.bind('<FocusIn>',On_FocusPasswordIn)
passwordentry.bind('<FocusOut>',On_FocusPasswordOut)


root.mainloop()
