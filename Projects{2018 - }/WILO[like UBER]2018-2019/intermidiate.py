import random
import time
def login():
    b=str(input("Do you alredy have an account.Y/N: "))
    if b=='Y' or b=='y':
        a=str(input("Enter Your Name: "))
        c=str(input('Email or P.H.No.: '))
        d=str(input('Password: '))
        if c=="gg@gmail.com" and d=="VV" or c=="8826027591":
            print("Wellcome back ",a)
        elif c=="gg@gmail.com" or c=="8826027591" and d!="VV":
            print("Password incorrect")
            print("Try again")
            print("Or Reset Password")
            print(Again_Reset())
        elif c!="gg@gmail.com" or c!="8826027591" and d=="VV":
            print("Invalid Email")
            print(login())
        print(book_ride())
    elif b=='N' or b=='n':
        print(singup())
        print(book_ride())
    else:
        print("Invalid input")
        print(login())
def finding():
    driver=['Ram','Sham',"Ritu",'David','Rajdeep','Rahul','Shubham','Nupur','Sudhir','Majnu']
    print('Driver Name: ',random.choice(driver))
    Number_Plate=['DL16BX5440','UP16DF4584','DL14BD4732','DL16BP4521','UP16KL8721']
    print('Number Plate: ',random.choice(Number_Plate))
    phone_no=['1228751736','3478459652','4425730175','5674152176','6778924657','7812847520','4513674258','9010256473','8788773366','1111111111']
    print('Phone Number: ',random.choice(phone_no))
    stars=['3','5','4','5','3','4','4','3','4.5','4.5']
    print('Star Rateing: ',random.choice(stars))
def Again_Reset():
    e=str(input("Press 1 to try again OR press 2 to reset password: "))
    if e=='1':
        print(login())
    elif e=='2':
        f=str(input('Email or P.H.No.: '))
        if f=="vinayak@gmail.com" or f=="8826027591":
            print("Mail has been sent to reset your password")
        elif f!="vinayak@gmail.com":
            print("Invalid Email OR P.H.No.")
            print(Again_Reset())
        else:
            print("Invalid Figure")
            print(Again_Reset())
def singup():
    c=str(input('Email or P.H.No.: '))
    d=str(input('Password: '))
    g=str(input("Reenter Password: "))
    if d==g:
        print("Wellcome to WILO")
    else:
        print("Password don't match")                                
def book_ride():
    m=str(input("Pickup Location"))
    mm=str(input("Where to? "))
    print("Chose Payment Option: ")
    print("1.Cash")
    print("2.Card")
    pay=str(input("Enter Your Choice(by number)")) 
    e=int(input("press 1 for options and 0 to resume: "))
    if e==1:
        print(d)
        print("Press 1 For Book Your Ride")
        print("Press 2 For Refer & Earn")
        print("Press 3 For Support")
        print("Press 4 For About")
        print("Press 5 for going back")
        dd=str(input("Enter Your Choice: "))
        if dd=='1':
              print(book_ride())
        elif dd=='2':
              print("share ur referral code=RFG34K")
              print("invite your friends from:")
              print("WhatsApp, Messenger, Hangouts, Contacts")
        elif dd=='4':
              print("WILO")
              print("v3.5.0")
        elif dd=='5':
            pass
    else:
        pass    
    book_fee=10
    costpermil=5
    print("1.Auto")
    print('2.Sedan')
    print('3.SUV')
    print("4.Pool('Sedan Only')")
    vehicel=str(input("Enter Your Choice"))
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
        print("Finding your ride")
        print(finding())
    else:
        p=str(input("Are you sure you want to CANCEL your ride. Enter Yes or No: "))
        if p=='Yes' or p=='yes'or p=='YES':
            print(book_ride())
        else:
            print("Finding your ride")
            print(finding())
    time.sleep(2)
    print("Your Driver Is Here!")
    time.sleep(2)
    print("You have reached your destination")
    time.sleep(1)
    g=str(input("Enter Number Of Stars For Your Ride: "))
    print("Thank You")

print("Welcome to WILO")

cf=input("Enter Your Name: ")
df=input("Enter Your Mobile Number: ")
print(login())
e=int(input("Press 1 For Options And 0 To Resume: "))
if e==1:
    print(cf,df)
    print("Press 1 For Book Your Ride")
    print("Press 2 For Refer & Earn")
    print("Press 3 For Support")
    print("Press 4 For About")
    dd=str(input("Enter Your Choice: "))
    if dd=='1':
          print(book_ride())
    elif dd=='2':
          print("share ur referral code=RFG34K")
          print("invite ur friends from")
    elif dd=='4':
          print("WILO")
          print("v3.5.0")
elif:                                         
    print(login())
else:
    
