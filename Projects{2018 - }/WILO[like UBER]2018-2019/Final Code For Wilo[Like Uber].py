import random
import time
def login():
    Label(v, bg = '#00CDCD',fg = 'black',text = "Do You Have A Account?",
          font = ("default",15,"bold")).grid(row = 1,column = 0)
    Button(v,width = 15,text = 'YES',command = lambda:A_YES() ,activebackground = "cyan", bg = '#00CDCD',
           fg = 'BLACK',relief = "raised").grid(row = 1, column = 1)
    Button(v,width = 15,text = 'NO',command = lambda:A_NO() ,activebackground = "cyan", bg = '#00CDCD',
           fg = 'BLACK',relief = "raised").grid(row = 1, column = 2)
def A_YES():
    Label(v, bg = '#00CDCD',fg = 'black',text = "Email:",
          font = ("default",15,"bold")).grid(row = 4,column = 0)
    c = Entry(v)
    c.grid(row = 4,column = 1)
    c.focus_set()
    Label(v, bg = '#00CDCD',fg = 'black',text = "Password:",
          font = ("default",15,"bold")).grid(row = 5,column = 0)
    d = Entry(v)
    d.grid(row = 5,column = 1)
    d.focus_set()
    Button(v,width = 15,text = 'OK',command = lambda:A_NO() ,activebackground = "cyan", bg = '#00CDCD',
           fg = 'BLACK',relief = "raised").grid(row = 6, column = 3)
    if c=="gg@gmail.com" and d=="VV":
        print("WELCOME BACK ".center(50))
        print(cf.center(50))
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
    
def finding():
    driver=['Ram','Sham',"Ritu",'David','Rajdeep','Rahul','Shubham','Nupur','Sudhir','Majnu']
    print("\n")
    print('Driver Name: '.center(50),random.choice(driver))
    print("\n")
    Number_Plate=['DL16BX5440','UP16DF4584','DL14BD4732','DL16BP4521','UP16KL8721']
    print('Number Plate: '.center(50),random.choice(Number_Plate))
    print("\n")
    phone_no=['1228751736'.center(50),'3478459652','4425730175','5674152176','6778924657','7812847520','4513674258','9010256473','8788773366','1111111111']
    print('Phone Number: '.center(50),random.choice(phone_no))
    print("\n")
    stars=['3','5','4','5','3','4','4','3','4.5','4.5']
    print('Star Rating: '.center(50),random.choice(stars))
def Again_Reset():
    print("1. To Try Again")
    print("2. To Reset Password")
    ee=str(input("Enter: "))
    if ee=='1':
        print(login())
    elif ee=='2':
        f=str(input('Email: '))
        if f=="gg@gmail.com":
            print("Mail Has Been Sent To Reset Your Password".center(50))
        elif f!="gg@gmail.com":
            print("Invalid Email")
            print(Again_Reset())
        else:
            print("Invalid Figure")
            print(Again_Reset())
def singup():
    c=str(input('Email: '))
    d=str(input('Password: '))
    g=str(input("Reenter Password: "))
    if d==g:
        print("WELCOME TO WILO".center(50))
        print(cf.center(50))
        print(df.center(50))
    else:
        print("Password Doesn't Match")
def payment():
    pay=str(input("Enter Your Choice(by number): "))
    if pay=='1':
        pass
    elif pay=='2':
        print("1. ICICI Bank")
        print("2. SBI Bank")
        print("3. IndusInd Bank")
        print("4. AXIS Bank")
        bank=str(input("Enter The Number Of Your Bank: "))
        if bank=='1':
            print("Welcome To ICICI Bank")
            print("1. Debit Card")
            print("2. Credit Card")
            card_ty=str(input("Enter"))
            if card_ty=="1":
                print("Enter Your Debit Card Details:")
                card_no=str(input("Enter Card Number: "))
                cvv=str(input("Enter CVV Number: "))
                print("Enter Expiry Date")
                mot=str(input("Month: ".center(25)))
                yr=int(input("Year: ".center(25)))
                if yr<2019:
                    if mot=="January" or mot=="JANUARY" or mot=="january":
                        print("Your Card Has Been Expired")
                        print("Try Again")
                        print(payment())
                    else:
                        pass
                else:
                    otp=str(input("Enter OTP: "))
                    print("Your Card Has Been Registered To This Account For This Ride")
            elif card_ty=="2":
                print("Enter Your Credit Card Details:")
                card_no=str(input("Enter Card Number: "))
                cvv=str(input("Enter CVV Number: "))
                print("Enter Expiry Date")
                mot=str(input("Month: ".center(25)))
                yr=int(input("Year: ".center(25)))
                if yr<2019:
                    if mot=="January" or mot=="JANUARY" or mot=="january":
                        print("Your Card Has Been Expired")
                        print("Try Again")
                        print(payment())
                    else:
                        pass
                else:
                    otp=str(input("Enter OTP: "))
                    print("Your Card Has Been Registered To This Account For This Ride")
            else:
                print('Wrong Input')
                print(payment())
        elif bank=='2':
            print("Welcome To SBI Bank".center(50))
            print("1. Debit Card")
            print("2. Credit Card")
            card_ty=str(input("Enter"))
            if card_ty=="1":
                print("Enter Your Debit Card Details:")
                card_no=str(input("Enter Card Number: "))
                cvv=str(input("Enter CVV Number: "))
                print("Enter Expiry Date")
                mot=str(input("Month: ".center(25)))
                yr=int(input("Year: ".center(25)))
                if yr<2019:
                    if mot=="January" or mot=="JANUARY" or mot=="january":
                        print("Your Card Has Been Expired")
                        print("Try Again")
                        print(payment())
                    else:
                        pass
                else:
                    otp=str(input("Enter OTP: "))
                    print("Your Card Has Been Registered To This Account For This Ride")
            elif card_ty=="2":
                print("Enter Your Credit Card Details:")
                card_no=str(input("Enter Card Number: "))
                cvv=str(input("Enter CVV Number: "))
                print("Enter Expiry Date")
                mot=str(input("Month: ".center(25)))
                yr=int(input("Year: ".center(25)))
                if yr<2019:
                    if mot=="January" or mot=="JANUARY" or mot=="january":
                        print("Your Card Has Been Expired")
                        print("Try Again")
                        print(payment())
                    else:
                        pass
                else:
                    otp=str(input("Enter OTP: "))
                    print("Your Card Has Been Registered To This Account For This Ride")
            else:
                print('Wrong Input')
                print(payment())
        elif bank=='3':
            print("Welcome To Indusand Bank".center(50))
            print("1. Debit Card")
            print("2. Credit Card")
            card_ty=str(input("Enter"))
            if card_ty=="1":
                print("Enter Your Debit Card Details:")
                card_no=str(input("Enter Card Number: "))
                cvv=str(input("Enter CVV Number: "))
                print("Enter Expiry Date")
                mot=str(input("Month: ".center(25)))
                yr=int(input("Year: ".center(25)))
                if yr<2019:
                    if mot=="January" or mot=="JANUARY" or mot=="january":
                        print("Your Card Has Been Expired")
                        print("Try Again")
                        print(payment())
                    else:
                        pass
                else:
                    otp=str(input("Enter OTP: "))
                    print("Your Card Has Been Registered To This Account For This Ride")
            elif card_ty=="2":
                print("Enter Your Credit Card Details:")
                card_no=str(input("Enter Card Number: "))
                cvv=str(input("Enter CVV Number: "))
                print("Enter Expiry Date")
                mot=str(input("Month: ".center(25)))
                yr=int(input("Year: ".center(25)))
                if yr<2019:
                    if mot=="January" or mot=="JANUARY" or mot=="january":
                        print("Your Card Has Been Expired")
                        print("Try Again")
                        print(payment())
                    else:
                        pass
                else:
                    otp=str(input("Enter OTP: "))
                    print("Your Card Has Been Registered To This Account For This Ride")
            else:
                print('Wrong Input')
                print(payment())
        elif bank=='4':
            print("Welcome To AXIS Bank".center(50))
            print("1. Debit Card")
            print("2. Credit Card")
            card_ty=str(input("Enter"))
            if card_ty=="1":
                print("Enter Your Debit Card Details:")
                card_no=str(input("Enter Card Number: "))
                cvv=str(input("Enter CVV Number: "))
                print("Enter Expiry Date")
                mot=str(input("Month: ".center(25)))
                yr=int(input("Year: ".center(25)))
                if yr<2019:
                    if mot=="January" or mot=="JANUARY" or mot=="january":
                        print("Your Card Has Been Expired")
                        print("Try Again")
                        print(payment())
                    else:
                        pass
                else:
                    otp=str(input("Enter OTP: "))
                    print("Your Card Has Been Registered To This Account For This Ride")
            elif card_ty=="2":
                print("Enter Your Credit Card Details:")
                card_no=str(input("Enter Card Number: "))
                cvv=str(input("Enter CVV Number: "))
                print("Enter Expiry Date")
                mot=str(input("Month: ".center(25)))
                yr=int(input("Year: ".center(25)))
                if yr<2019:
                    if mot=="January" or mot=="JANUARY" or mot=="january":
                        print("Your Card Has Been Expired")
                        print("Try Again")
                        print(payment())
                    else:
                        pass
                else:
                    otp=str(input("Enter OTP: "))
                    print("Your Card Has Been Registered To This Account For This Ride")
            else:
                print('Wrong Input')
                print(payment())
    elif pay=='3':
        pno=str(input("Enter Phone Number: "))
        otpp=str(input("Enter OTP: "))
        print("Your PayPal Account Has Been Linked To This Account For This Ride")
def book_ride():
    print('1. For Options')
    print("\n")
    print("2. To Resume")
    print("\n")
    e=int(input("Enter: "))
    if e==1:
        print("Options".center(50))
        print(cf.center(50))
        print(df.center(50))
        print("1. To Book A Ride")
        print("\n")
        print("2. To Refer & Earn")
        print("\n")
        print("3. For About")
        print("\n")
        dd=str(input("Enter Your Choice: "))
        if dd=='1':
              print(book_ride())
        elif dd=='2':
              print("Share Your Referral CODE:'RFG34K'")
              print("\n")
              print("Invite Your Friends From:")
              print("\n")
              print("WhatsApp, Messenger, Hangouts, Contacts")
              print("\n")
        elif dd=='3':
              print("WILO".center(50))
              print("\n")
              print("v3.5.0".center(50))
    elif e=='2':
        pass
    m=str(input("Pickup Location: "))
    mm=str(input("Where To? "))
    if m==mm:
        print("You Can't Book A Ride For Under 500 Meters Of Distance")
        print(book_ride())
    else:
        pass
    print('1. For Options')
    print("\n")
    print("2. To Resume")
    print("\n")
    eeee=int(input("Enter: "))
    if eeee==1:
        print("Options".center(50))
        print(cf.center(50))
        print(df.center(50))
        print("1. To Book A Ride")
        print("\n")
        print("2. To Refer & Earn")
        print("\n")
        print("3. For About")
        print("\n")
        print("4. For Going Back")
        print("\n")
        dd=str(input("Enter Your Choice: "))
        if dd=='1':
              print(book_ride())
        elif dd=='2':
              print("Share Your Referral CODE:'RFG34K'")
              print("\n")
              print("Invite Your Friends From:")
              print("\n")
              print("WhatsApp, Messenger, Hangouts, Contacts")
        elif dd=='3':
              print("WILO".center(50))
              print("\n")
              print("v3.5.0".center(50))
        elif dd=='4':
            pass
    else:
        pass 
    print("Chose Payment Option: ")
    print("1.Cash")
    print("2.Card")
    print("3.PayPal")
    print(payment())
                
    print("\n")
    print('1. For Options')
    print("\n")
    print("2. To Resume")
    print("\n")
    eeeee=int(input("Enter: "))
    if eeeee==1:
        print("Options".center(50))
        print(cf.center(50))
        print(df.center(50))
        print("1. To Book A Ride")
        print("\n")
        print("2. To Refer & Earn")
        print("\n")
        print("3. For About")
        print("\n")
        print("4. For Going Back")
        print("\n")
        dd=str(input("Enter Your Choice: "))
        if dd=='1':
              print(book_ride())
        elif dd=='2':
              print("Share Your Referral CODE:'RFG34K'")
              print("\n")
              print("Invite Your Friends From:")
              print("\n")
              print("WhatsApp, Messenger, Hangouts, Contacts")
        elif dd=='3':
              print("WILO".center(50))
              print("\n")
              print("v3.5.0".center(50))
        elif dd=='4':
            pass
    else:
        pass     
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


#print("WELCOME TO WILO".center(50))
from tkinter import *
v = Tk()
v.configure(background=("#00CDCD"))
wind = v.geometry('600x600')
v.title("Wilo")
Label(v, bg = '#00CDCD',fg = 'black',text = "Enter Your Name:",font = ("default",15,"bold")).grid(row = 1,column = 0)
cf = Entry(v)
cf.grid(row = 1,column = 1)
cf.focus_set()
Label( v, bg = '#00CDCD',fg = 'black',text = "Enter Your Number:",font = ("default",15,"bold")).grid(row = 5,column = 0)
df = Entry(v)
df.grid(row = 5,column = 1)
Button(v,width = 15,text = '=',command = lambda:login() ,activebackground = "cyan", bg = '#00CDCD',
       fg = 'BLACK',relief = "raised").grid(row = 7, column = 1)

v.mainloop()
