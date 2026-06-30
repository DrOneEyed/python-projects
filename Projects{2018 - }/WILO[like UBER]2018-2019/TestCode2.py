def Again_Reset():
    e=str(input("Press 1 to try again OR press 2 to reset password"))
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
        print("Wellcome to Name")
    else:
        print("Password don't match")
def login():
    b=str(input("Do you alredy have an account.Y/N "))
    if b=='Y' or b=='y':
        c=str(input('Email or P.H.No.: '))
        d=str(input('Password: '))
        if c=="vinayak@gmail.com" and d=="Vinayak" or c=="8826027591":
            print("Wellcome back Vinayak")
        elif c=="vinayak@gmail.com" or c=="8826027591" and d!="Vinayak":
            print("Password incorrect")
            print("Try again")
            print("Or Reset Password")
            print(Again_Reset())
        elif c!="vinayak@gmail.com" or c!="8826027591" and d=="Vinayak":
            print("Invalid Email")
            print(login())
    elif b=='N' or b=='n':
        print(singup())
        
    else:
        print("Invalid input")
        print(login())
def Start():
    print("WELLCOME TO NAME")
    print("Login as Driver or Rider")
    a=str(input("To login as DRIVER press 1 or press 2 to login as RIDER "))
    if a=='1':
        print("Wellcome to NAME as a Driver")
        print(login())
    elif a=='2':
        print("Wellcome to NAME as a Rider")
        print(login())
    else:
        print("Invalid input")
        print(Start())
print(Start())

