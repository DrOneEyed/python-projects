import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
def login():
    c = str(input("Do You have A Account? Y/N: "))
    if c == 'Y' or c == 'y':
        d = str(input("Enter Your Email ID: "))
        e = str(input("Enter Your Password: "))
        dd = open(r"emails.txt",'r')
        for i in dd.readline():
            if i in d:
                print("Welcome Back",i)
                print(reservation())
            else:
                print("Try Again!!!!")
                print(login())

    else:
        d = str(input("Enter Your Email ID: "))
        e = str(input("Enter Your Password: "))
        ee = str(input("Reenter Your Password: "))
        if e != ee:
            print("Try Again!!!!!!!!!!")
            print(login())
        else:
            print(reservation())

def reservation():
    root = tk.Tk()
    s = ttk.Style(root)
    s.theme_use('clam')
    ttk.Button(root, text='DateEntry', command=lambda:Calendar()).pack(padx=10, pady=10)
    root.mainloop()


def Calendar():
    top = tk.Toplevel(root)
    ttk.Label(top, text='Choose date').pack(padx=10, pady=10)
    cal = DateEntry(top, width=12, background='darkblue',
                    foreground='white', borderwidth=2)
    cal.pack(padx=10, pady=10)

a = str(input("Enter Your Name: "))
b = int(input("Enter Your Mobile Number: "))
print(login())
