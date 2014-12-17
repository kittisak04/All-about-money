import tkFont
import tkMessageBox
import ttk
import Tkinter

home = Tkinter.Tk()
home.geometry('800x600')
home.resizable(width=True, height=True)
home.title('All About Money V.1.01')
home.configure(bg='black')

#calculator ______ edit by tong * *
def calcul():
    money = float(moneyentry.get())
    interest = float(interestentry.get())
    year = int(yearentry.get())
    monthly_interest = interest/(100 * 12)
    payment_number = year * 12
    monthly_payment = money * (monthly_interest / (1 - (1 + monthly_interest) ** ( -1 * payment_number)))
    payments = 100
    rem_principal = money * (1 - ((1 + monthly_interest) ** payments - 1) / ((1 + monthly_interest) ** payment_number - 1))
    if interest >100:
        tkMessageBox.showinfo(message='0% - 100%')
  
    var_1.set("Total loan = %0.2f" % money)
    var_2.set("Interest   = %0.2f%s" % (interest, "%"))
    var_3.set("Years      = %0.f year" % year)
    var_4.set("Number of payments = %0.f  month" % payment_number)
    var_5.set("Payment amount     = %0.2f" % monthly_payment)
    #var_6.set("-"*60)
    var_7.set("Total cost     = %0.2f" % (payment_number * monthly_payment))
    var_8.set("Total interest = %0.2f" % (payment_number * monthly_payment - money))
    #var_9.set("-"*60)
    var_10.set("The outstanding principal after %d payments is %0.2f " % (payments, rem_principal))
    var_11.set("At this point you have paid a total of %0.2f" % (monthly_payment * payments))
    
##Label
hLabel = Tkinter.Label(text='ALL ABOUT MONEY', bg= 'black', fg='green',font=tkFont.Font(size=15, weight=tkFont.BOLD)).pack()
hLabel2 = Tkinter.Label(text='Faculty of Information Technology @ KMITL', bg= 'black', fg='blue' ).place(x=0,y=570)
#hLabe3 = Tkinter.Label(text='This program is demo version').place(x=0,y=550)
interestLabel = Tkinter.Label(text='%', bg= 'black', fg='white', font=tkFont.Font(size=15)).place(x=500,y=110)

## input text
mlabel = Tkinter.Label(text='Money', bg= 'black', fg='white',font=tkFont.Font(size=15)).place(x=230,y=70)
ilabel = Tkinter.Label(text='Interest', bg= 'black',fg='white', font=tkFont.Font(size=15)).place(x=230,y=110)
ylabel = Tkinter.Label(text='Time', bg= 'black', fg='white',font=tkFont.Font(size=15)).place(x=230,y=150)
moneyentry = Tkinter.Entry(home, width=30)
interestentry = Tkinter.Entry(home, width=30)
yearentry = Tkinter.Entry(home, width=30)
moneyentry.place(x=310,y=80)
interestentry.place(x=310,y=115)
yearentry.place(x=310,y=155)

#display of label  ______ edit by tong
var_1 = Tkinter.StringVar()
var_2 = Tkinter.StringVar()
var_3 = Tkinter.StringVar()
var_4 = Tkinter.StringVar()
var_5 = Tkinter.StringVar()
var_6 = Tkinter.StringVar()
var_7 = Tkinter.StringVar()
var_8 = Tkinter.StringVar()
var_9 = Tkinter.StringVar()
var_10 = Tkinter.StringVar()
var_11 = Tkinter.StringVar()
label_1 = Tkinter.Label(home, textvariable=var_1, fg='white', bg= 'black', font = tkFont.Font(size = 15))
label_2 = Tkinter.Label(home, textvariable=var_2, fg='white', bg= 'black', font = tkFont.Font(size = 15))
label_3 = Tkinter.Label(home, textvariable=var_3, fg='white', bg= 'black', font = tkFont.Font(size = 15))
label_4 = Tkinter.Label(home, textvariable=var_4, fg='white', bg= 'black', font = tkFont.Font(size = 15))
label_5 = Tkinter.Label(home, textvariable=var_5, fg='white', bg= 'black', font = tkFont.Font(size = 15))
label_6 = Tkinter.Label(home, textvariable=var_6, fg='white', bg= 'black', font = tkFont.Font(size = 15))
label_7 = Tkinter.Label(home, textvariable=var_7, fg='white', bg= 'black', font = tkFont.Font(size = 15))
label_8 = Tkinter.Label(home, textvariable=var_8, fg='white',bg= 'black', font = tkFont.Font(size = 15))
label_9 = Tkinter.Label(home, textvariable=var_9, fg='white',bg= 'black', font = tkFont.Font(size = 15))
label_10 = Tkinter.Label(home, textvariable=var_10, fg='white',bg= 'black', font = tkFont.Font(size = 15))
label_11 = Tkinter.Label(home, textvariable=var_11, fg='white',bg= 'black', font = tkFont.Font(size = 15))
label_1.place(x=70,y=250)
label_2.place(x=70,y=280)
label_3.place(x=70,y=310)
label_4.place(x=70,y=340)
label_5.place(x=70,y=370)
label_6.place(x=70,y=400)
label_7.place(x=400,y=250)
label_8.place(x=400,y=280)
label_9.place(x=400,y=310)
label_10.place(x=150,y=450)
label_11.place(x=150,y=490)

## list
moneylist = Tkinter.StringVar()
moneybox = ttk.Combobox(home, textvariable=moneylist,state='readonly')
moneybox['values'] = ('Bath')
moneybox.current(0)
moneybox.place(x=500,y=80)

yearlist = Tkinter.StringVar()
yearbox = ttk.Combobox(home, textvariable=yearlist,state='readonly')
yearbox['values'] = ('Year')
yearbox.current(0)
yearbox.place(x=500,y=150)

##menubar func
def about():
    tkMessageBox.showinfo(message='Made By\nKittisak Kaewnan 57070008 \nKhemathat')
def elp():
    tkMessageBox.showinfo(message='This program will help save your time for calculate anything about money\nhope this program will help you')
def xit():
    homeExit = tkMessageBox.askokcancel(title='Quit', message='Are You Sure')
    if homeExit != 0:
        home.destroy()
        return

##menubar
menubar = Tkinter.Menu(home)
           
topmenu = Tkinter.Menu(menubar, tearoff=0)
topmenu.add_command(label='About', command=about)
topmenu.add_command(label='Help', command=elp)
menubar.add_cascade(label='Menu', menu=topmenu)

exitmenu = Tkinter.Menu(menubar, tearoff=0)
exitmenu.add_command(labe='Exit',command=xit)
menubar.add_cascade(label='Exit',menu=exitmenu)

#convert button
convert = Tkinter.Button(text="Calculate",command=calcul,fg='black',bg='light blue',font=tkFont.Font(size = 12))
convert.place(x=360,y=200)

home.config(menu=menubar)

home.mainloop()
