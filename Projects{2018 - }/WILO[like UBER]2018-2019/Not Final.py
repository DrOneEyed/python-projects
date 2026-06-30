import random
import time
def login():
    b=str(input("Do you alredy have an account.Y/N: "))
    if b=='Y' or b=='y':
        c=str(input('Email: '))
        d=str(input('Password: '))
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
    elif b=='N' or b=='n':
        print(singup())
        print(book_ride())
    else:
        print("Invalid input")
        print(login())
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
    print('Star Rateing: '.center(50),random.choice(stars))
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
    pay=str(input("Enter Your Choice(by number): "))
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
        print('Star Rateing: ',random.choice(stars))
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
            print('Star Rateing: ',random.choice(stars))
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


print("WELCOME TO WILO".center(50))
cf=input("Enter Your Name: ")
df=input("Enter Your Mobile Number: ")
print(login())

    

