from tkinter import *
from tkinter import messagebox as msgb
#from tkinter import ttk
def book_ride():
    Label( v, bg = '#00CDCD',fg = 'black',text = "Pickup Location:",
       font = ("default",15,"bold")).grid(row = 2,column = 0)
    m = Entry(v)
    m.grid(row = 2,column = 1)
    Label( v, bg = '#00CDCD',fg = 'black',text = "Where To?",
       font = ("default",15,"bold")).grid(row = 2,column = 0)
    mm = Entry(v)
    mm.grid(row = 2,column = 1)
    Button(v,width = 15,text = 'Enter',command = lambda:loc(m.get(),mm.get()) ,activebackground = "cyan",
       bg = '#00CDCD',fg = 'BLACK',relief = "raised").grid(row = 2, column = 3)
def loc(a,b):
    if m==mm:
        msgb.showerror("You Can't Book A Ride For Under 500 Meters Of Distance")
        book_ride()
    else:
        pass
    Label( v, bg = '#00CDCD',fg = 'black',text = "Chose Payment Option",
       font = ("default",15,"bold")).grid(row = 2,column = 0)
    pay_mode = Combobox(v,width = 2, textvariable = StringVar())
    pay_mode['values'] = ('Cash','Online Wallet')
    pay_mode.grid(row =2, column = 1)
    print(payment())
                
    
    book_fee=10
    costpermil=5
    print("1.Auto")
    print("\n")
    print('2.Sedan')
    print("\n")
    print('3.SUV')
    print("\n")
    print("4.Pool('Sedan Only')")
    print("\n")
    vehicel=str(input("Enter Your Choice: "))
    if vehicel=='1':
        base=40
        fare=base+book_fee
        print('Fare =',fare)
    elif vehicel=='2':
        base=60
        fare=base+book_fee
        print('Fare =',fare)
    elif vehicel=='3':
        base=80
        fare=base+book_fee
        print('Fare =',fare)
    elif vehicel=='4':
        base=50
        fare=(base+book_fee)/3
        print('Fare =',fare)
    else:
        print("Invalid input")
        print(book_ride())
    confirm=str(input("Press 1 to CONFIRM or 2 to CANCEL: "))
    if confirm=='1':
        print("\n")
        print("Finding your ride")
        print("\n")
        driver=['Ram','Sham',"Ritu",'David','Rajdeep','Rahul','Shubham','Nupur','Sudhir','Majnu']
        print('Driver Name: ',random.choice(driver))
        print("\n")
        Number_Plate=['DL16BX5440','UP16DF4584','DL14BD4732','DL16BP4521','UP16KL8721']
        print('Number Plate: ',random.choice(Number_Plate))
        print("\n")
        phone_no=['1228751736','3478459652','4425730175','5674152176','6778924657','7812847520','4513674258','9010256473','8788773366','1111111111']
        print('Phone Number: ',random.choice(phone_no))
        print("\n")
        stars=['3','5','4','5','3','4','4','3','4.5','4.5']
        print('Star Rating: ',random.choice(stars))
    else:
        p=str(input("Are you sure you want to CANCEL your ride. Enter Yes or No: "))
        if p=='Yes' or p=='yes'or p=='YES':
            print(book_ride())
        else:
            print("\n")
            print("Finding your ride")
            driver=['Ram','Sham',"Ritu",'David','Rajdeep','Rahul','Shubham','Nupur','Sudhir','Majnu']
            print("\n")
            print('Driver Name: ',random.choice(driver))
            Number_Plate=['DL16BX5440','UP16DF4584','DL14BD4732','DL16BP4521','UP16KL8721']
            print("\n")
            print('Number Plate: ',random.choice(Number_Plate))
            print("\n")
            phone_no=['1228751736','3478459652','4425730175','5674152176','6778924657','7812847520','4513674258','9010256473','8788773366','1111111111']
            print('Phone Number: ',random.choice(phone_no))
            stars=['3','5','4','5','3','4','4','3','4.5','4.5']
            print("\n")
            print('Star Rating: ',random.choice(stars))
            print("\n")
    time.sleep(2)
    print("Your Driver Is Here!".center(50))
    print("\n")
    time.sleep(1.5)
    print("1. For S.O.S")
    print("\n")
    time.sleep(1.5)
    print('2. To Ignore S.O.S')
    print("\n")
    j4=str(input(": "))
    if j4=='1':
        print("\n")
        time.sleep(1)
        print("Sending Your location to nearest police patrol unit".center(50))
            
    else:
        time.sleep(1.5)
        print("You have reached your destination")
        time.sleep(1)
        print('\n')
        g=str(input("Enter Number Of Stars For Your Ride: "))
        print('\n')
        print("Thank You".center(50))
    print('\n')
    print("1. To Book Another Ride")
    print('\n')
    print("2. To Quit")
    suree=str(input(": "))
    if suree=='1':
        print('\n')
        print(book_ride())
    elif suree=='2':
       quit()



v = Tk()
menu_bar = Menu(v)
v.configure(background=("#00CDCD"),menu = menu_bar)
wind = v.geometry('500x400')
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

Label( v, bg = '#00CDCD',fg = 'black',text = "Chose Payment Option",
       font = ("default",15,"bold")).grid(row = 2,column = 0)
pay_mode = Combobox(v,width = 2, textvariable = StringVar())
pay_mode['values'] = ('Cash','Online Wallet')
pay_mode.grid(row =2, column = 1)
