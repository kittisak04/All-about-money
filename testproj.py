import tkFont
import tkMessageBox
import ttk
import Tkinter

def to_interest():
    interest = Tkinter.Tk()
    interest.minsize(width=500, height=500)
    interest.maxsize(width=500, height=500)
    home.destroy()
home = Tkinter.Tk()
home.geometry('800x500')
home.resizable(width=False, height=False)
home.title('All About Money V.Beta')

#calculator ______ edit by tong
def calcul():
    var_1.set("Total loan = $%0.2f" % pmoneyentry)
    var_2.set("Interest   = %0.2f%s" % (interestentry, "%"))
    var_3.set("Years      = %0.f" % yearentry)
    var_4.set("%.2f" % (tempcalc * 1.8)+" Rankine.")

    
##Label
hLabel = Tkinter.Label(text='ALL ABOUT MONEY', font=tkFont.Font(size=15, weight=tkFont.BOLD)).pack()
hLabel2 = Tkinter.Label(text='Faculty of Information Technology @ KMITL' ).place(x=550,y=470)
hLabe3 = Tkinter.Label(text='This program is demo version').place(x=630,y=450)
interestLabel = Tkinter.Label(text='%', font=tkFont.Font(size=15)).place(x=500,y=110)

## input text
mlabel = Tkinter.Label(text='Money', font=tkFont.Font(size=15)).place(x=240,y=70)
ilabel = Tkinter.Label(text='Interest', font=tkFont.Font(size=15)).place(x=230,y=110)
interestentry = Tkinter.Entry(home, width=30)
moneyentry = Tkinter.Entry(home, width=30)
yearentry = Tkinter.Entry(home, width=30)
moneyentry.place(x=310,y=80)
interestentry.place(x=310,y=115)
yearentry.place(x=310,y=155)

#display of label  ______ edit by tong
var_1 = Tkinter.StringVar()
var_2 = Tkinter.StringVar()
var_3 = Tkinter.StringVar()
var_4 = Tkinter.StringVar()
label_1 = Tkinter.Label(home, textvariable=var_1, fg='black',bg="#FFFFFF",font = tkFont.Font(size = 12))
label_2 = Tkinter.Label(home, textvariable=var_2, fg='black',bg="#FFFFFF",font = tkFont.Font(size = 12))
label_3 = Tkinter.Label(home, textvariable=var_3, fg='black',bg="#FFFFFF",font = tkFont.Font(size = 12))
label_4 = Tkinter.Label(home, textvariable=var_4, fg='black',bg="#FFFFFF",font = tkFont.Font(size = 12))
label_1.pack()
label_2.pack()
label_3.pack()
label_4.pack()

## list
moneylist = Tkinter.StringVar()
moneybox = ttk.Combobox(home, textvariable=moneylist,state='readonly')
moneybox['values'] = ('Bath')
moneybox.current(0)
moneybox.place(x=500,y=80)

yearlist = Tkinter.StringVar()
yearbox = ttk.Combobox(home, textvariable=yearlist,state='readonly')
yearbox['values'] = ('Day','Month')
yearbox.current(0)
yearbox.place(x=500,y=150)

def close_window():
    home.destroy()

home = Tkinter.Tk()
home.minsize(width=300, height=500)
home.maxsize(width=300, height=500)

interest_button = Tkinter.Button(home, text='INTEREST', command=to_interest, width=300)
close_button = Tkinter.Button(home, text='EXIT', command=close_window)

interest_button.pack()
close_button.pack()
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

home.config(menu=menubar)

home.mainloop()



