from tkinter import *
from tkinter import messagebox as msgb
import time
def login():
  
    Label(v, bg = '#00CDCD',fg = 'black',text = " ",
          font = ("default",15,"bold")).grid(row = 3,column = 0)
    Label(v, bg = '#00CDCD',fg = 'black',text = "Do You Have A Account?",
          font = ("default",15,"bold")).grid(row = 4,column = 0)
    Button(v,width = 15,text = 'YES',command = lambda:A_YES() ,activebackground = "cyan",
           bg = '#00CDCD', fg = 'BLACK',relief = "raised").grid(row = 4, column = 1)
    Button(v,width = 15,text = 'NO',command = lambda:A_NO() ,activebackground = "cyan",
           bg = '#00CDCD', fg = 'BLACK',relief = "raised").grid(row = 4, column = 3)
def A_YES():
    Label(v, bg = '#00CDCD',fg = 'black',text = " ",
          font = ("default",15,"bold")).grid(row = 5,column = 0)
    Label(v, bg = '#00CDCD',fg = 'black',text = "Email:",
          font = ("default",15,"bold")).grid(row = 6,column = 0)
    c = Entry(v)
    c.grid(row = 6,column = 1)
    c.focus_set()
    Label(v, bg = '#00CDCD',fg = 'black',text = "Password:",
          font = ("default",15,"bold")).grid(row = 7,column = 0)
    d = Entry(v)
    d.grid(row = 7,column = 1)
    d.focus_set()
    Button(v,width = 15,text = 'OK',command = lambda:Check(c.get(),d.get()) ,activebackground = "cyan",
           bg = '#00CDCD', fg = 'BLACK',relief = "raised").grid(row = 7, column = 3)
def Check(c,d):
    if c=="gg@gmail.com" and d=="VV":
        
        print("WELCOME BACK ".center(50))
        print(book_ride())
    elif c=="gg@gmail.com" and d!="VV":
        print("Password Incorrect")
        print("Try Again")
        print("Or Reset Password")
        print(Again_Reset())
    elif c!="gg@gmail.com" and d=="VV":
        print("Invalid Email")
        print(login())
    elif c!="gg@gmail.com" and d!="VV":
        print("Invalid Email")
        print(login())
def A_NO():
    print(singup())
    print(book_ride())
def Exit():
    ans = msgb.askyesnocancel("Quit Wilo", "Do You Want To Quit?")
    if ans == True:
        v.quit()
        v.destroy()
        time.sleep(1)
    else:
        pass
    
def About():
    msgb.showinfo("About Wilo","Wilo Version \n1.2.1.0.NV")
    
#def book_ride():    
v = Tk()
menu_bar = Menu(v)
v.configure(background=("#00CDCD"),menu = menu_bar)
#wind = v.geometry('500x400')
Canvas(v, width=250, height=300)

v.title("Wilo")
opt = Menu(menu_bar, tearoff = 0)
opt.add_command(label = "Book Ride", command = lambda:book_ride())
opt.add_separator()
opt.add_command(label = "About", command = lambda:About())
opt.add_separator()
opt.add_command(label = "Exit", command = lambda:Exit())
menu_bar.add_cascade(label = "Options", menu = opt)
Label(v, bg = '#00CDCD',fg = 'black',text = "Enter Your Name:",
      font = ("default",15,"bold")).grid(row = 1,column = 0)
cf = Entry(v)
cf.grid(row = 1,column = 1)
cf.focus_set()
Label( v, bg = '#00CDCD',fg = 'black',text = "Enter Your Number:",
       font = ("default",15,"bold")).grid(row = 2,column = 0)
df = Entry(v)
df.grid(row = 2,column = 1)
Label( v, bg = '#00CDCD',fg = 'black',text = " ",
       font = ("default",15,"bold")).grid(row = 2,column = 2)
Button(v,width = 15,text = 'Enter',command = lambda:login() ,activebackground = "cyan",
       bg = '#00CDCD',fg = 'BLACK',relief = "raised").grid(row = 2, column = 3)




v.mainloop()
