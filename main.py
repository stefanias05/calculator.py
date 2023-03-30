import math
from math import *
from tkinter import *
fereastra = Tk() # am creat fereastra window
fereastra.geometry("400x400")  # am setat lungimea ferfestrei
fereastra.resizable()  # am setat ca utilizatorul sa nu poata modif fereastra
fereastra.title("Calculator")

def adauga(n):
    global variabila

    variabila = variabila + str(n)
    text.set(variabila)


#sterg ce se afla in textdate, "c" buton

def sterge():
    global variabila

    variabila = ""
    text.set("")


# Calculez ce e in expresie

def egal():
    global variabila
    rez = int(eval(variabila))  #'eval':evalueaza automat expresia adunare/scad etc
    text.set(rez)
    variabila = ""



variabila = ""


text = StringVar()

# am creat un cadru pt textul de intrare unde vor fi introduse datele

textdate = Frame(fereastra,width=30, height=50,bd=0, highlightbackground="white", highlightcolor="black",
                    highlightthickness=2)

#am pus frame-ul in windows

textdate.pack(side=TOP)

# am creat fereastra de introducere date in interiorul textdate care e afisat in fereastra

introduceredate = Entry(textdate, font=('arial', 18, 'bold'), textvariable=text, width=24, bg="#eee", bd=0,
                    justify=RIGHT)

introduceredate.grid(row=0, column=0)   #inserez in fereastra

introduceredate.pack(ipady=8)  # afisez in fereastra'ipady:cresc inltimea campului de intrare cu 8

# creez un cadru nou pe care il afise in fereastra. Am pus butoanele

cadru = Frame(fereastra, width=312, height=272.5, bg="grey")

cadru.pack()

#creez butoanele

butonsterge = Button(cadru, text="C", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2",command=lambda: sterge())

butonimpartire = Button(cadru, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",command=lambda: adauga("/"))

buton7 = Button(cadru, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",command=lambda: adauga(7))

buton8 = Button(cadru, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",command=lambda: adauga(8))

buton9 = Button(cadru, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",command=lambda: adauga(9))

inmultire = Button(cadru, text="*", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",command=lambda: adauga("*"))

buton4 = Button(cadru, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",command=lambda: adauga(4))

buton5 = Button(cadru, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",command=lambda: adauga(5))

buton6 = Button(cadru, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",command=lambda: adauga(6))

butonminus = Button(cadru, text="-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",command=lambda: adauga("-"))


buton1 = Button(cadru, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",command=lambda: adauga(1))

buton2 = Button(cadru, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",command=lambda: adauga(2))

buton3 = Button(cadru, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",command=lambda: adauga(3))

butonplus = Button(cadru, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",command=lambda: adauga("+"))

buton0 = Button(cadru, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2",command=lambda: adauga(0))

butonvirgula = Button(cadru, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",command=lambda: adauga("."))

butonegal = Button(cadru, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: egal())



#afisez butoanele in cadru
butonsterge.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
butonimpartire.grid(row=0, column=3, padx=1, pady=1)
buton7.grid(row=1, column=0, padx=1, pady=1)
buton8.grid(row=1, column=1, padx=1, pady=1)
buton9.grid(row=1, column=2, padx=1, pady=1)
inmultire.grid(row=1, column=3, padx=1, pady=1)
buton4.grid(row=2, column=0, padx=1, pady=1)
buton5.grid(row=2, column=1, padx=1, pady=1)
buton6.grid(row=2, column=2, padx=1, pady=1)
butonminus.grid(row=2, column=3, padx=1, pady=1)
buton1.grid(row=3, column=0, padx=1, pady=1)
buton2.grid(row=3, column=1, padx=1, pady=1)
buton3.grid(row=3, column=2, padx=1, pady=1)
butonplus.grid(row=3, column=3, padx=1, pady=1)
buton0.grid(row=4, column=0, columnspan=2,  padx=1, pady=1)
butonvirgula.grid(row=4, column=2, padx=1, pady=1)
butonegal.grid(row=4, column=3, padx=1, pady=1)


#rulez pana cand utilizatorul inchide fereastra
fereastra.mainloop()



