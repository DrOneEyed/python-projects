import time
import random
def login_Driver():
    b=str(input("Do you alredy have an account.Y/N: "))
    if b=='Y' or b=='y':
        mail=str(input("Email: "))
        pas=str(input("Password: "))
        if mail!='vv@gmail.com' or pas!='GG':
            print("Incorrect email or password")
            o=str(input('Enter 1 to try again or Enter 2 to Reset password'))
            if o=='1':
                print(login_Driver())
            elif o=='2':
                print(reset_driver())
            else:
                print("Invalid input")
        elif mail=='vv@gmail.com' or pas=='GG':
            print(find_ride())
        else:
            print("Invalid input")
            print(login_Driver())
    elif b=='N' or b=='n':
        print(singup_Driver())
        print(find_ride())
    else:
        print("Invalid input")
        print(login_Driver())
def reset_driver():
    e=str(input("Press 1 to try again OR press 2 to reset password"))
    if e=='1':
        print(login())
    elif e=='2':
        f=str(input('Email: '))
        if f=="vv@gmail.com":
            print("Mail has been sent to reset your password")
        elif f!="vv@gmail.com":
            print("Invalid Email")
            print(reset_driver())
        else:
            print("Invalid Figure")
def singup_Driver():
    jj=str(input("Enter Your Email: "))
    kk=str(input("Password: "))
    ll=str(input("Reenter Password: "))
    if kk!=ll:
        print("Password Dont Match")
        print(singup_Driver())
    elif jj=='vv@gmail.com':
        print("An account is alredy liked to this mail!")
        print(login_Driver())
    elif jj!='vv@gmail.com':
        if kk==ll:
            print('welcome to name')
            ss=str(input("Enter Your Linces No.: "))
            ff=str(input("Enter Your Number Plate Number: "))
            print(find_ride())
def find_ride():
    ee=str(input('Are You Available For A Ride? Y/N: '))
    if ee=="Y" or ee=='y':
        rider=['Amit','Ajay','Raju','Manju','Hemanshi','Sanjana','Daksh','Yash','Pramod','Dev']
        print('Rider Name: ',random.choice(rider))
        phoneNo=['45','65','25','30','88','91','97','23','66','10']
        print('Phone Number: ',random.choice(phoneNo))
        stars=['3','4.5','5','4','4','5','4.5','3.5','5','4']
        print('Stars: ',random.choice(stars))
        t=str(input("Do you want to confirm pickup? Y/N: "))
        if t=='y' or t=='Y':
            print("Meet The Rider At Location")
            time.sleep(2)
            print("You Have Reached The Destination")
            h=str(input("Rate the rider: "))
        elif t=='n' or t=='N':
            r=str(input("Enter 1 when you are ready to take a ride. "))
            
print(login_Driver())
