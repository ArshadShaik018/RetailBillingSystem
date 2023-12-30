
from tkinter import *
from tkinter import messagebox
import random, os,tempfile,smtplib

if not os.path.exists('bills'):
    os.mkdir('bills')


def clear():
    bathsoapentry.delete(0, END)
    facecreamentry.delete(0, END)
    facewashentry.delete(0, END)
    hairgelentry.delete(0, END)
    hairsprayentry.delete(0, END)
    bodylotionentry.delete(0, END)

    daalentry.delete(0, END)
    riceentry.delete(0, END)
    oilentry.delete(0, END)
    wheatentry.delete(0, END)
    sugarentry.delete(0, END)
    teaentry.delete(0, END)

    maazaentry.delete(0, END)
    spriteentry.delete(0, END)
    frootientry.delete(0, END)
    dewentry.delete(0,END)
    cocolaentry.delete(0, END)
    pepsientry.delete(0, END)

    bathsoapentry.insert(0,0)
    facecreamentry.insert(0,0)
    facewashentry.insert(0,0)
    hairgelentry.insert(0,0)
    hairsprayentry.insert(0,0)
    bodylotionentry.insert(0,0)

    riceentry.insert(0,0)
    daalentry.insert(0,0)
    oilentry.insert(0,0)
    wheatentry.insert(0,0)
    sugarentry.insert(0,0)
    teaentry.insert(0,0)

    maazaentry.insert(0,0)
    spriteentry.insert(0,0)
    frootientry.insert(0,0)
    dewentry.insert(0,0)
    cocolaentry.insert(0,0)
    pepsientry.insert(0,0)

    cosmatipricecentry.delete(0,END)
    grocerypriceentry.delete(0,END)
    drinkspriceentry.delete(0,END)

    cosmatitaxcentry.delete(0,END)
    grocerytaxentry.delete(0,END)
    drinkstaxentry.delete(0,END)

    nameentry.delete(0,END)
    phonenumberentry.delete(0,END)
    billnumberentry.delete(0,END)

    textarea.delete(1.0,END)










def send_email():
    def send_gmail():
        try:
            ob=smtplib.SMTP('smtp.gmail.com',587)
            ob.starttls()
            ob.login(senderentry.get(),passwordentry.get())
            message=email_textarea.get(1.0,END)
            ob.sendmail(senderentry.get(),reciverentry.get(),message)
            ob.quit()
            messagebox.showinfo('success','Bill is successfully sent',parent=root1)
            root1.destroy()
        except:
            messagebox.showerror('Error','Something went wrong')

    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        root1=Toplevel()
        root1.grab_set()
        root1.title('Send Email')
        root1.config(bg='black')
        root1.resizable(False,False)
        senderframe=LabelFrame(root1, text='SENDER',bg='black',fg='White',font=('arial',17,'bold'),relief=RIDGE)
        senderframe.grid(row=0, column=0,padx=40,pady=20)

        senderlable=Label(senderframe, text="Sender's Mail",fg='white',bg='black',font=('arial',14,'bold'))
        senderlable.grid(row=0,column=0,padx=10,pady=10,sticky='w')

        senderentry=Entry(senderframe, font=('arial',14,'bold'),bd=2,width=20,)
        senderentry.grid(row=0, column=1,padx=10,pady=10,sticky='w')

        passwordlable = Label(senderframe, text="Password", fg='white', bg='black', font=('arial', 14, 'bold'))
        passwordlable.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        passwordentry = Entry(senderframe, font=('arial', 14, 'bold'), bd=2, width=20, show='!')
        passwordentry.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        recipeintframe = LabelFrame(root1, text='RCIPEINT', bg='black', fg='White', font=('arial', 17, 'bold'), relief=RIDGE)
        recipeintframe.grid(row=1, column=0, padx=40, pady=20)

        reciverlable = Label(recipeintframe, text="Email Address", fg='white', bg='black', font=('arial', 14, 'bold'))
        reciverlable.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        reciverentry = Entry(recipeintframe, font=('arial', 14, 'bold'), bd=2, width=20, )
        reciverentry.grid(row=0, column=1, padx=10, pady=10, sticky='w')

        messagelable = Label(recipeintframe, text="Message", fg='white', bg='black', font=('arial', 14, 'bold'))
        messagelable.grid(row=1, column=0, padx=10, pady=10)

        email_textarea=Text(recipeintframe,  font=('arial', 14, 'bold'),bd=2,relief=SUNKEN,width=40,height=14)
        email_textarea.grid(row=2,column=0,columnspan=2)
        email_textarea.delete(1.0, END)
        email_textarea.insert(END,textarea.get(1.0, END).replace('=',' ').replace('-',' ').replace('\t\t\t','\t\t'))


        sendbutton=Button(root1, text='Send',  font=('arial', 16, 'bold'),width=10,command=send_gmail)
        sendbutton.grid(row=2,column=0,pady=20)

        root1.mainloop()
def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')




def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0]== billnumberentry.get():
            f = open(f'bills/{i}', 'r')
            textarea.delete(1.0,END)
            for data in f:
                textarea.insert(END,data)
            f.close()
            break

    else:
        messagebox.showerror('Error', 'Invalid Bill Number')


def save_bill():
    global billnumber
    result = messagebox.askyesno('Confirm', 'Do you want to save')
    if result:
        bill_content = textarea.get(1.0, END)
        file = open(f'bills/{billnumber}.txt', 'w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Sucsess', f'Bill Number {billnumber} is saved successfully')
        billnumber = random.randint(1000, 10000)


billnumber = random.randint(1000, 10000)


def total():
    global soap, facecream, hairspray, hairgel, facewash, bodylotion, rice, daal, wheat, sugar, oil, tea, maaza, sprite, dew, frooti, pepsi, cococola
    global totalbill
    soap = int(bathsoapentry.get()) * 20
    facecream = int(facecreamentry.get()) * 50
    hairspray = int(hairsprayentry.get()) * 30
    hairgel = int(hairgelentry.get()) * 60
    facewash = int(facewashentry.get()) * 150
    bodylotion = int(bodylotionentry.get()) * 100
    totalcosmatics = soap + facecream + hairspray + hairgel + facewash + bodylotion
    cosmatipricecentry.delete(0, END)
    cosmatipricecentry.insert(0, f'{totalcosmatics} Rs')

    cosmatictax = totalcosmatics * 0.6
    cosmatitaxcentry.delete(0, END)
    cosmatitaxcentry.insert(0, str(cosmatictax) + 'Rs')

    rice = int(riceentry.get()) * 100
    oil = int(oilentry.get()) * 95
    daal = int(daalentry.get()) * 55
    wheat = int(wheatentry.get()) * 23
    sugar = int(sugarentry.get()) * 48
    tea = int(teaentry.get()) * 25
    totalgrocery = rice + oil + daal + wheat + sugar + tea
    grocerypriceentry.delete(0, END)
    grocerypriceentry.insert(0, f'{totalgrocery} Rs')

    grocerytax = totalgrocery * 0.8
    grocerytaxentry.delete(0, END)
    grocerytaxentry.insert(0, str(grocerytax) + 'Rs')

    maaza = int(maazaentry.get()) * 65
    pepsi = int(pepsientry.get()) * 50
    sprite = int(spriteentry.get()) * 35
    dew = int(dewentry.get()) * 40
    frooti = int(frootientry.get()) * 60
    cococola = int(cocolaentry.get()) * 90
    totaldrinks = maaza + pepsi + sprite + dew + frooti + cococola
    drinkspriceentry.delete(0, END)
    drinkspriceentry.insert(0, f'{(totaldrinks)} Rs')

    drinkstax = totaldrinks * 0.12
    drinkstaxentry.delete(0, END)
    drinkstaxentry.insert(0, str(drinkstax) + 'Rs')

    totalbill = totalcosmatics + totalgrocery + totaldrinks + cosmatictax + grocerytax + drinkstax


def bill_area():
    if nameentry.get() == '' or phonenumberentry.get() == '':
        messagebox.showerror('error', 'Please enter customer details')
    elif cosmatipricecentry.get() == '' and grocerypriceentry.get() == '' and drinkspriceentry.get() == '':
        messagebox.showerror('Error', 'No Products are selected')
    elif cosmatipricecentry.get() == '0 Rs' and grocerypriceentry.get() == '0 Rs' and drinkspriceentry.get() == '0 RS':
        messagebox.showerror('Error', 'No Products are selected  ')
    else:
        textarea.delete(1.0, END)
        textarea.insert(END, '\t\t***Welcome customer***')
        textarea.insert(END, f'\n\nBill number: {billnumber}')
        textarea.insert(END, f'\nCustomer Name: {nameentry.get()}')
        textarea.insert(END, f'\nPhone Number: {phonenumberentry.get()}')
        textarea.insert(END, '\n*******************************************************')
        textarea.insert(END, '\nProducts\t\t\tQuantity\t\tPrice')
        textarea.insert(END, '\n*******************************************************')
        if bathsoapentry.get() != '0':
            textarea.insert(END, f'\nBath Soap\t\t\t{bathsoapentry.get()}\t\t{soap} Rs')
        if facecreamentry.get() != '0':
            textarea.insert(END, f'\nFace Cream\t\t\t{facecreamentry.get()}\t\t{facecream} Rs')
        if facewashentry.get() != '0':
            textarea.insert(END, f'\nFace Wash\t\t\t{facewashentry.get()}\t\t{facewash} Rs')
        if hairsprayentry.get() != '0':
            textarea.insert(END, f'\nHair Spray\t\t\t{hairsprayentry.get()}\t\t{hairspray} Rs')
        if hairgelentry.get() != '0':
            textarea.insert(END, f'\nHair Gel\t\t\t{hairgelentry.get()}\t\t{hairgel} Rs')
        if bodylotionentry.get() != '0':
            textarea.insert(END, f'\nBody Lotion\t\t\t{bodylotionentry.get()}\t\t{bodylotion} Rs')

        if riceentry.get() != '0':
            textarea.insert(END, f'\nRice\t\t\t{riceentry.get()}\t\t{rice} Rs')
        if oilentry.get() != '0':
            textarea.insert(END, f'\nOil\t\t\t{oilentry.get()}\t\t{oil} Rs')
        if daalentry.get() != '0':
            textarea.insert(END, f'\nDaal\t\t\t{daalentry.get()}\t\t{daal} Rs')
        if wheatentry.get() != '0':
            textarea.insert(END, f'\nWheat\t\t\t{wheatentry.get()}\t\t{wheat} Rs')
        if sugarentry.get() != '0':
            textarea.insert(END, f'\nSugar\t\t\t{sugarentry.get()}\t\t{sugar} Rs')
        if teaentry.get() != '0':
            textarea.insert(END, f'\nTea\t\t\t{teaentry.get()}\t\t{bodylotion} Rs')

        if maazaentry.get() != '0':
            textarea.insert(END, f'\nMaaza\t\t\t{maazaentry.get()}\t\t{maaza} Rs')
        if pepsientry.get() != '0':
            textarea.insert(END, f'\nPepsi\t\t\t{pepsientry.get()}\t\t{pepsi} Rs')
        if spriteentry.get() != '0':
            textarea.insert(END, f'\nSprite\t\t\t{facewashentry.get()}\t\t{sprite} Rs')
        if dewentry.get() != '0':
            textarea.insert(END, f'\nDew\t\t\t{dewentry.get()}\t\t{dew} Rs')
        if frootientry.get() != '0':
            textarea.insert(END, f'\nFrooti\t\t\t{frootientry.get()}\t\t{frooti} Rs')
        if cocolaentry.get() != '0':
            textarea.insert(END, f'\nCocoCola\t\t\t{cocolaentry.get()}\t\t{cococola} Rs')
        if cosmatitaxcentry.get() != '0.0':
            textarea.insert(END, f'\n Cosmetic Tax\t\t\t\t{cosmatitaxcentry.get()}')
        if grocerytaxentry.get() != '0.0':
            textarea.insert(END, f'\n Grocery Tax\t\t\t\t{grocerytaxentry.get()}')
        if drinkstaxentry.get() != '0.0':
            textarea.insert(END, f'\n Drinks  Tax\t\t\t\t{drinkstaxentry.get()}')
        textarea.insert(END, '\n*******************************************************\n')

        textarea.insert(END, f'\n{nameentry.get()} your totalbill is \t\t\t\t{totalbill}')
        textarea.insert(END, '\n*******************************************************\n')
        save_bill()


root = Tk()
root.geometry('1530x1000')
root.resizable(False, False)
root.title('Retail Billing System')
root.iconbitmap('imag.ico')

headinglable = Label(root, text='Retail Billing System', bg='black', fg='blue', font=('times new roman', 35, 'bold'),
                     bd=10, relief=RIDGE)
headinglable.pack(fill=X)

customerlabel = LabelFrame(root, text='Customer Detial', font=('arial', 15, 'bold'), fg='blue', bg='black',
                           relief=RIDGE, bd=8)
customerlabel.pack(fill=X, pady=8)

namelabel = Label(customerlabel, text='Name', bg='black', fg='white', font=('arial', 15))
namelabel.grid(row=0, column=0, padx=10, pady=10)

nameentry = Entry(customerlabel, width=17, bd=3, font=('arial', 15))
nameentry.grid(row=0, column=1, padx=10)

phonenumberlabel = Label(customerlabel, text='Phone Number', bg='black', fg='white', font=('arial', 15), )
phonenumberlabel.grid(row=0, column=3, padx=10, pady=10)

phonenumberentry = Entry(customerlabel, width=17, bd=3, font=('arial', 12))
phonenumberentry.grid(row=0, column=4, padx=10)

billnumberlabel = Label(customerlabel, text='Bill Number', bg='black', fg='white', font=('arial', 15))
billnumberlabel.grid(row=0, column=5, padx=10, pady=10)

billnumberentry = Entry(customerlabel, width=17, bd=3, font=('arial', 12))
billnumberentry.grid(row=0, column=6, padx=10)

searchbutton = Button(customerlabel, text='SEARCH', font=('calibre', 12), width=8, bg='red', fg='yellow', bd=6,
                      command=search_bill)
searchbutton.grid(row=0, column=7, padx=10, pady=10)

productframe = Frame(root)
productframe.pack(fill=X)

cosmeticsframe = LabelFrame(productframe, text='Cosmetics', font=('arial', 15, 'bold'), fg='blue', bg='black',
                            relief=RIDGE, bd=8)
cosmeticsframe.grid(row=0, column=0)

bathsoaplable = Label(cosmeticsframe, text='BathSoap', bg='black', fg='white', font=('times new roman', 15), bd=4)
bathsoaplable.grid(row=1, column=0, pady=10, padx=10, sticky='w')

bathsoapentry = Entry(cosmeticsframe, width=11, bd=3, font=('arial', 12))
bathsoapentry.grid(row=1, column=1, pady=10, padx=10)
bathsoapentry.insert(0, 0)

facecreamlable = Label(cosmeticsframe, text='Face Cream', bg='black', fg='white', font=('times new roman', 15), bd=4)
facecreamlable.grid(row=2, column=0, pady=10, padx=10, sticky='w')

facecreamentry = Entry(cosmeticsframe, width=11, bd=3, font=('arial', 12))
facecreamentry.grid(row=2, column=1, pady=10, padx=10)
facecreamentry.insert(0, 0)

facewashlable = Label(cosmeticsframe, text='Face Wash', bg='black', fg='white', font=('times new roman', 15), bd=4)
facewashlable.grid(row=3, column=0, pady=10, padx=10, sticky='w')

facewashentry = Entry(cosmeticsframe, width=11, bd=3, font=('arial', 12))
facewashentry.grid(row=3, column=1, pady=10, padx=10)
facewashentry.insert(0, 0)

hairspraylable = Label(cosmeticsframe, text='Hair Spray', bg='black', fg='white', font=('times new roman', 15), bd=4)
hairspraylable.grid(row=4, column=0, pady=10, padx=10, sticky='w')

hairsprayentry = Entry(cosmeticsframe, width=11, bd=3, font=('arial', 12))
hairsprayentry.grid(row=4, column=1, pady=10, padx=10)
hairsprayentry.insert(0, 0)

hairgellable = Label(cosmeticsframe, text='Hair Gel', bg='black', fg='white', font=('times new roman', 15), bd=4)
hairgellable.grid(row=5, column=0, pady=10, padx=10, sticky='w')

hairgelentry = Entry(cosmeticsframe, width=11, bd=3, font=('arial', 12))
hairgelentry.grid(row=5, column=1, pady=10, padx=10)
hairgelentry.insert(0, 0)

bodylotionlable = Label(cosmeticsframe, text='Body Lotion', bg='black', fg='white', font=('times new roman', 15), bd=4)
bodylotionlable.grid(row=6, column=0, pady=10, padx=10, sticky='w')

bodylotionentry = Entry(cosmeticsframe, width=11, bd=3, font=('arial', 12))
bodylotionentry.grid(row=6, column=1, pady=10, padx=10)
bodylotionentry.insert(0, 0)

groceryframe = LabelFrame(productframe, text='Grocery', font=('arial', 15, 'bold'), fg='blue', bg='black', relief=RIDGE,
                          bd=8)
groceryframe.grid(row=0, column=1)

ricelable = Label(groceryframe, text='Rice', bg='black', fg='white', font=('times new roman', 15), bd=4)
ricelable.grid(row=1, column=0, pady=10, padx=10, sticky='w')

riceentry = Entry(groceryframe, width=11, bd=3, font=('arial', 12))
riceentry.grid(row=1, column=1, pady=10, padx=10)
riceentry.insert(0, 0)

oillable = Label(groceryframe, text='Oil', bg='black', fg='white', font=('times new roman', 15), bd=4)
oillable.grid(row=2, column=0, pady=10, padx=10, sticky='w')

oilentry = Entry(groceryframe, width=11, bd=3, font=('arial', 12))
oilentry.grid(row=2, column=1, pady=10, padx=10)
oilentry.insert(0, 0)

daallable = Label(groceryframe, text='Daal', bg='black', fg='white', font=('times new roman', 15), bd=4)
daallable.grid(row=3, column=0, pady=10, padx=10, sticky='w')

daalentry = Entry(groceryframe, width=11, bd=3, font=('arial', 12))
daalentry.grid(row=3, column=1, pady=10, padx=10)
daalentry.insert(0, 0)

wheatlable = Label(groceryframe, text='Wheat', bg='black', fg='white', font=('times new roman', 15), bd=4)
wheatlable.grid(row=4, column=0, pady=10, padx=10, sticky='w')

wheatentry = Entry(groceryframe, width=11, bd=3, font=('arial', 12))
wheatentry.grid(row=4, column=1, pady=10, padx=10)
wheatentry.insert(0, 0)

sugarlable = Label(groceryframe, text='Sugar', bg='black', fg='white', font=('times new roman', 15), bd=4)
sugarlable.grid(row=5, column=0, pady=10, padx=10, sticky='w')

sugarentry = Entry(groceryframe, width=11, bd=3, font=('arial', 12))
sugarentry.grid(row=5, column=1, pady=10, padx=10)
sugarentry.insert(0, 0)

tealable = Label(groceryframe, text='Tea', bg='black', fg='white', font=('times new roman', 15), bd=4)
tealable.grid(row=6, column=0, pady=10, padx=10, sticky='w')

teaentry = Entry(groceryframe, width=11, bd=3, font=('arial', 12))
teaentry.grid(row=6, column=1, pady=10, padx=10)
teaentry.insert(0, 0)

cooldrinksframe = LabelFrame(productframe, text='CoolDrinks', font=('arial', 15, 'bold'), fg='blue', bg='black',
                             relief=RIDGE, bd=8)
cooldrinksframe.grid(row=0, column=2)

maazalable = Label(cooldrinksframe, text='Maaza', bg='black', fg='white', font=('times new roman', 15), bd=4)
maazalable.grid(row=1, column=0, pady=10, padx=10, sticky='w')

maazaentry = Entry(cooldrinksframe, width=11, bd=3, font=('arial', 12))
maazaentry.grid(row=1, column=1, pady=10, padx=10)
maazaentry.insert(0, 0)

pepsilable = Label(cooldrinksframe, text='Pepsi', bg='black', fg='white', font=('times new roman', 15), bd=4)
pepsilable.grid(row=2, column=0, pady=10, padx=10, sticky='w')

pepsientry = Entry(cooldrinksframe, width=11, bd=3, font=('arial', 12))
pepsientry.grid(row=2, column=1, pady=10, padx=10)
pepsientry.insert(0, 0)

spritelable = Label(cooldrinksframe, text='Sprite', bg='black', fg='white', font=('times new roman', 15), bd=4)
spritelable.grid(row=3, column=0, pady=10, padx=10, sticky='w')

spriteentry = Entry(cooldrinksframe, width=11, bd=3, font=('arial', 12))
spriteentry.grid(row=3, column=1, pady=10, padx=10)
spriteentry.insert(0, 0)

dewlable = Label(cooldrinksframe, text='Dew', bg='black', fg='white', font=('times new roman', 15), bd=4)
dewlable.grid(row=4, column=0, pady=10, padx=10, sticky='w')

dewentry = Entry(cooldrinksframe, width=11, bd=3, font=('arial', 12))
dewentry.grid(row=4, column=1, pady=10, padx=10)
dewentry.insert(0, 0)

frootilable = Label(cooldrinksframe, text='Frooti', bg='black', fg='white', font=('times new roman', 15), bd=4)
frootilable.grid(row=5, column=0, pady=10, padx=10, sticky='w')

frootientry = Entry(cooldrinksframe, width=11, bd=3, font=('arial', 12))
frootientry.grid(row=5, column=1, pady=10, padx=10)
frootientry.insert(0, 0)

cococolalable = Label(cooldrinksframe, text='Cococola', bg='black', fg='white', font=('times new roman', 15), bd=4)
cococolalable.grid(row=6, column=0, pady=10, padx=10, sticky='w')

cocolaentry = Entry(cooldrinksframe, width=11, bd=3, font=('arial', 12))
cocolaentry.grid(row=6, column=1, pady=10, padx=10)
cocolaentry.insert(0, 0)

billframe = Frame(productframe, bd=7, relief=RIDGE)
billframe.grid(row=0, column=3, padx=10,)

billareaframe = Label(billframe, text='Bill Area', font=('times new roman', 15, 'bold'), bd=6, relief=RIDGE)
billareaframe.pack(fill=X)

scrollbar = Scrollbar(billframe, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

textarea = Text(billframe, height=18, width=55, yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuframe = LabelFrame(root, text='Bill Menu', font=('arial', 15, 'bold'), fg='blue', bg='black', relief=RIDGE,
                           bd=8)
billmenuframe.pack(pady=6,fill=X)

cosmaticpricelable = Label(billmenuframe, text='Cosmatic Price', bg='black', fg='white', font=('times new roman', 15),
                           bd=4)
cosmaticpricelable.grid(row=0, column=0, pady=10, padx=10, sticky='w')

cosmatipricecentry = Entry(billmenuframe, width=11, bd=3, font=('arial', 12))
cosmatipricecentry.grid(row=0, column=1, pady=10, padx=10)

grocerypricelable = Label(billmenuframe, text='Grocery Price', bg='black', fg='white', font=('times new roman', 15),
                          bd=4)
grocerypricelable.grid(row=1, column=0, pady=10, padx=10, sticky='w')

grocerypriceentry = Entry(billmenuframe, width=11, bd=3, font=('arial', 12))
grocerypriceentry.grid(row=1, column=1, pady=10, padx=10)

drinkspricelable = Label(billmenuframe, text='Drinks Price', bg='black', fg='white', font=('times new roman', 15), bd=4)
drinkspricelable.grid(row=2, column=0, pady=10, padx=10, sticky='w')

drinkspriceentry = Entry(billmenuframe, width=11, bd=3, font=('arial', 12))
drinkspriceentry.grid(row=2, column=1, pady=10, padx=10)

cosmatictaxlable = Label(billmenuframe, text='Cosmatic Tax', bg='black', fg='white', font=('times new roman', 15), bd=4)
cosmatictaxlable.grid(row=0, column=2, pady=10, padx=10, sticky='w')

cosmatitaxcentry = Entry(billmenuframe, width=11, bd=3, font=('arial', 12))
cosmatitaxcentry.grid(row=0, column=3, pady=10, padx=10)

grocerytaxlable = Label(billmenuframe, text='Grocery Tax', bg='black', fg='white', font=('times new roman', 15), bd=4)
grocerytaxlable.grid(row=1, column=2, pady=10, padx=10, sticky='w')

grocerytaxentry = Entry(billmenuframe, width=11, bd=3, font=('arial', 12))
grocerytaxentry.grid(row=1, column=3, pady=10, padx=10)

drinkstaxlable = Label(billmenuframe, text='Drinks Tax', bg='black', fg='white', font=('times new roman', 15), bd=4)
drinkstaxlable.grid(row=2, column=2, pady=10, padx=10, sticky='w')

drinkstaxentry = Entry(billmenuframe, width=11, bd=3, font=('arial', 12))
drinkstaxentry.grid(row=2, column=3, pady=10, padx=10)

buttonframe =Frame(billmenuframe, bd=8, relief=RIDGE,)
buttonframe.grid(row=0, column=5, rowspan=3,padx=150)

totalbutton = Button(buttonframe, text='Total', font=('arial', 15, 'bold',), bg='black', fg='white', pady=4, bd=3,
                     width=9, command=total)
totalbutton.grid(row=0, column=0, pady=20, padx=6)

billbutton = Button(buttonframe, text='Bill', font=('arial', 15, 'bold',), bg='black', fg='white', pady=4, bd=3,
                    width=9, command=bill_area)
billbutton.grid(row=0, column=1, pady=20, padx=5)

emailbutton = Button(buttonframe, text='Email', font=('arial', 15, 'bold',), bg='black', fg='white', pady=4, bd=3,
                     width=9,command=send_email)
emailbutton.grid(row=0, column=2, pady=20, padx=5)

printbutton = Button(buttonframe, text='Print', font=('arial', 15, 'bold',), bg='black', fg='white', pady=4, bd=3,
                     width=9,command=print_bill)
printbutton.grid(row=0, column=3, pady=20, padx=5)

clearbutton = Button(buttonframe, text='Clear', font=('arial', 15, 'bold',), bg='black', fg='white', pady=4, bd=3,
                     width=9,command=clear)
clearbutton.grid(row=0, column=4, pady=20, padx=5)




root.mainloop()
