import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

def Calendar():
    top = tk.Toplevel(root)
    ttk.Label(top, text='Choose date').pack(padx=10, pady=10)
    cal = DateEntry(top, width=12, background='darkblue',
                    foreground='white', borderwidth=2)
    cal.pack(padx=10, pady=10)
root = tk.Tk()
s = ttk.Style(root)
s.theme_use('clam')
ttk.Button(root, text='DateEntry', command=lambda:Calendar()).pack(padx=10, pady=10)
root.mainloop()
