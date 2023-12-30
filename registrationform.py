from tkinter import *
from tkinter import messagebox

import pymysql

root = Tk()
root.title('Registration Form')
root.resizable(0, 0)
root.config(bg='black')
root.geometry('1530x1500')

country=['India', 'Egypt', 'Pakistan', 'America', 'Dubai']

firstname=StringVar()
lastname=StringVar()
username=StringVar()
gender = StringVar()
om=StringVar()
password=StringVar()
confirmPassword=StringVar()

def register():
    if firstnameentry.get()=='':
        messagebox.showerror('Alert','Please enter first name')
    elif lastnameentry.get() == '':
        messagebox.showerror('Alert', 'Please enter last name')
    elif emailentry.get() == '':
        messagebox.showerror('Alert', 'Please enter Email')
    elif gender.get() == '':
        messagebox.showerror('Alert', 'Please Select gender')
    elif om.get() == '':
        messagebox.showerror('Alert', 'Please Select Country  name')
    elif passwordentry.get() == '':
        messagebox.showerror('Alert', 'Please enter Password')
    elif passwordentry.get() == '':
        messagebox.showerror('Alert', 'Please enter Confirmpasswor')
    elif passwordentry.get() != confirmpsswordentry.get():
        messagebox.showerror('Error','Password and Confirm Password not matches',)
    else:

        db = pymysql.connect(host='localhost', user='root', password='Shaik@123', database='registrationform' )
        cur = db.cursor()
        try:
            query = 'create database registrationform'
            cur.execute(query)
            query = 'use registrationform'
            cur.execute(query)

            query = 'create table registrationdetails (id int auto_increment primary key not null, firstname varchar(40),''lastname varchar(40),email varchar(40),username varchar(40), gender varchar(40), country varchar(40),''password varchar(40), confirmpassword varchar(30))'
            cur.execute(query)
            messagebox.showinfo('sucesss', 'fields created succsefully')

        except:
            cur.execute('use registrationform')
            query = (
                'insert into registrationdetails(firstname, lastname, email,username, gender, country, password,confirmpassword) values(%s,%s,%s,%s,%s,%s,%s,%s)')
            cur.execute(query, (firstnameentry.get(), lastnameentry.get(), emailentry.get(),usernameentry.get(), gender.get(), om.get(),
                                 passwordentry.get(), confirmpsswordentry.get()))
            db.commit()
            db.close()
            messagebox.showinfo('sucess', 'succesfull registration')
            root.destroy()
            import login_form


            firstnameentry.delete(0,END)
            lastnameentry.delete(0,END)
            emailentry.delete(0,END)
            usernameentry.delete(0,END)
            gender.set()
            om.set()
            passwordentry.delete(0,END)
            confirmpsswordentry.delete(0,END)


def show():
    passwordentry.config(show='')
    passwordicon.config(command=hide)

def hide():
    passwordentry.config(show='*')
    passwordicon.config(command=show)



def login():
    root.destroy()
    import login_form





heading=Label(root, text='Registration Form', bg='black',fg='white',font=('calibre',40, 'bold'))
heading.place(x=520,y=0)


registerframe = LabelFrame(root, text='', bg='gray20', fg='white', font=('arial', 20, 'bold'), relief=GROOVE, bd=10)
registerframe.place(x=500, y=240)
registerframe.pack(fill=Y, pady=70)


firstnamelabel = Label(registerframe, text='First Name:', bg='gray20', fg='White', font=('arial', 25, 'bold'))
firstnamelabel.grid(row=0, column=0, pady=10, padx=10, sticky='w')

firstnameentry = Entry(registerframe, width=24, bd=2, font=('calibre', 14, 'bold'))
firstnameentry.grid(row=0, column=1, padx=10, pady=10)

lastnamelabel = Label(registerframe, text='Last Name:', bg='gray20', fg='White', font=('arial', 25, 'bold'))
lastnamelabel.grid(row=1, column=0, pady=10, padx=10, sticky='w')

lastnameentry = Entry(registerframe, width=24, bd=2, font=('calibre', 14, 'bold'), )
lastnameentry.grid(row=1, column=1, padx=10, pady=10)

emaillabel = Label(registerframe, text='Email:', bg='gray20', fg='White', font=('arial', 25, 'bold'))
emaillabel.grid(row=2, column=0, pady=10, padx=10, sticky='w')

emailentry = Entry(registerframe, width=24, bd=2, font=('calibre', 14, 'bold'))
emailentry.grid(row=2, column=1, padx=10, pady=10)

usernamelabel = Label(registerframe, text='User Name:', bg='gray20', fg='White', font=('arial', 25, 'bold'))
usernamelabel.grid(row=3, column=0, pady=10, padx=10, sticky='w')

usernameentry = Entry(registerframe, width=24, bd=2, font=('calibre', 14, 'bold'),)
usernameentry.grid(row=3, column=1, padx=10, pady=10)

selectgender = Label(registerframe, text='Select Gender:', bg='gray20', fg='White', font=('arial', 25, 'bold'))
selectgender.grid(row=4, column=0, pady=10, padx=10, sticky='w')

radio1 = Radiobutton(registerframe, text='Male',bg='gray20',fg='white',font=('arial', 20, 'bold'), variable=gender,
                     value='male')
radio1.place(x=350, y=265)

radio2 = Radiobutton(registerframe, text='Female', bg='gray20',fg='white', font=('arial', 20, 'bold'), variable=gender,
                     value='Female')
radio2.place(x=460, y=265)

countrydropdown1 = OptionMenu(registerframe, om, *country)
countrydropdown1.place(x=360,y=335)
om.set('Select Country')
countrydropdown1.config(font=('calibre',11,'bold'),width=22,)

country = Label(registerframe, text='Select Country:', bg='gray20', fg='White', font=('arial', 25, 'bold'))
country.grid(row=5, column=0, pady=10, padx=10, sticky='w')


passwordlabel=Label(registerframe, text='Password:',bg='gray20',fg='White',font=('arial',25,'bold'))
passwordlabel.grid(row=6,column=0,pady=10,padx=10,sticky='w')

passwordentry=Entry(registerframe, width=24,bd=2,font=('calibre',14,'bold'),show='*')
passwordentry.grid(row=6,column=1,padx=55,pady=10)

passwordicon=Checkbutton(registerframe, width=1,bg='gray20',command=show)
passwordicon.place(x=652,y=405)

confirmpasswordlabel=Label(registerframe, text='confirmPassword:',bg='gray20',fg='White',font=('arial',25,'bold'))
confirmpasswordlabel.grid(row=7,column=0,pady=10,padx=10,sticky='w')


confirmpsswordentry=Entry(registerframe, width=24,bd=2,font=('calibre',14,'bold'),show='*')
confirmpsswordentry.grid(row=7,column=1,padx=55,pady=10)

registerbtn=Button(root, text='Register',bg='green',fg='black',bd=6,width=10,font=('arial',15,'bold'),command=register)
registerbtn.place(x=697,y=620)

backbutton=Button(registerframe, text='Login',bd=5,width=10,font=('calibre',15,'bold'),bg='orange',fg='black',command=login)
backbutton.grid(row=8,column=0,pady=30,sticky='w,s',padx=8)


alreadyuser=Label(registerframe, text='If already user',font=('calibre',15,'bold'),bg='gray20',fg='red')
alreadyuser.place(x=10,y=510)



root.mainloop()
