def flight_onewayd():
    print ("1. TR212   3 hrs     non-stop     16:00-19:00      Economy class",     psg,"travellers",       "₹",4230)
    print("\n")
    print("2. TR232    5 hrs      1 stop      13:00-18:00      Economy class",      psg,"travellers",       "₹",6000)
    print("\n")
    print("3. TR231    3 hrs     non-stop     04:30-07:30      Economy class",      psg,"travellers",        "₹",7000)
    print("\n")
    print("4. TR252    6 hrs      2 stops     02:30-08:30      Economy class",      psg,"travellers",       "₹",7500)
    print("\n")
    print(jfmamj())
def flightonewayd_winters():
    print ("1. TR215   2 hrs     non-stop     17:00-19:00      Economy class",      psg,"travellers",       "₹",5500)
    print("\n")
    print("2. TR250    3 hrs      2 stops      12:30-15:30     Economy class",      psg,"travellers",       "₹",7200)
    print("\n")
    print("3. TR255    4 hrs     non-stop     08:00-12:00      Economy class",      psg,"travellers",       "₹",9000)
    print("\n")
    print("4. TR257    1 hr      1 stop     08:30-09:30        Economy class",      psg,"travellers",       "₹",3000)
    print("\n")
    print(jasondec())
 
def jfmamj(): 
    a=str(input("Enter the No. :"))
    if a=="1":
         print(" You have chosen Flight No. TR212")
         s=input("Do you want to do enquiry for another flight? Y/N:")
         if s=='y' or s=='Y':
           print(flight_onewayd())
         elif s=='N' or s=='n':
             print("Total fare for", psg, "Passengers=", psg*4230)
    if a=="2":
         print(" You have chosen Flight No. TR232")
         s=input("Do you want to do enquiry for another flight? Y/N:")
         if s=='Y' or s=='y':
           print(flight_onewayd())
         elif s=='N' or s=='n':
             print("Total fare for", psg, "Passengers=", psg*6000)
    if a=="3":
         print(" You have chosen Flight No. TR231")
         s=input("Do you want to do enquiry for another flight? Y/N:")
         if s=='Y' or s=='y':
           print(flight_onewayd())
         elif s=='N' or s=='n':
             print("Total fare for", psg, "Passengers=", psg*7000)
    if a=="4":
         print(" You have chosen Flight No. TR252")
         s=input("Do you want to do enquiry for another flight? Y/N:")
         if s=='Y' or s=='y':
           print(flight_onewayd())
         elif s=='N' or s=='n':
             print("Total fare for", psg, "Passengers=", psg*7500)
def jasondec(): 
    a=str(input("Enter the No. :"))
    if a=="1":
         print(" You have chosen Flight No. TR215")
         s=input("Do you want to do enquiry for another flight? Y/N:")
         if s=='y' or s=='Y':
           print(flightonewayd_winters())
         elif s=='N' or s=='n':
             print("Total fare for", psg, "Passengers=", psg*5500)
    if a=="2":
         print(" You have chosen Flight No. TR250")
         s=input("Do you want to do enquiry for another flight? Y/N:")
         if s=='Y' or s=='y':
           print(flightonewayd_winters())
         elif s=='N' or s=='n':
             print("Total fare for", psg, "Passengers=", psg*7200)
    if a=="3":
         print(" You have chosen Flight No. TR255")
         s=input("Do you want to do enquiry for another flight? Y/N:")
         if s=='Y' or s=='y':
           print(flightonewayd_winters())
         elif s=='N' or s=='n':
             print("Total fare for", psg, "Passengers=", psg*9000)
    if a=="4":
         print(" You have chosen Flight No. TR257")
         s=input("Do you want to do enquiry for another flight? Y/N:")
         if s=='Y' or s=='y':
           print(flightonewayd_winters())
         elif s=='N' or s=='n':
             print("Total fare for", psg, "Passengers=", psg*3000)



def sign_up():
    print("Singup to book your tickets")
    a=str(input("Enter your First Name :"))
    b=str(input("Enter Your Surname :"))
    c=str(input("Enter your Email id or Phone No. :"))
    d=str(input("Enter Password :"))
    e=str(input("Re enter Password :"))
    if d==e:
        print("Welcome",a,b)
    else:
            print("Password doesn't match")
            print(Password_reset())
def Password_reset():
    i=str(input("Press 1 to Try Again OR Press 2 to Reset Password: "))
    if i=='1':
        print(login_details())
    elif i=='2':
        jj=str(input("Enter Email or Phone No :"))
        if jj=="rai.tanishq@gmail.com" or jj=="9717180804":
            print("Mail has been sent to reset your password")
        elif jj!="rai.tanishq@gmail.com" :
            print("Invalid Email or Phone No. :")
            print(Password_reset())
        else:
            print("Invalid Entry ")
            print(sign_up())
            
def login_details():
    ee=str(input("Enter your Email id or Phone No. :"))
    ff=str(input("Enter the Password :"))
    if ee=="rai.tanishq@gmail.com" or ee=="9717180804" and ff=="aart1234":
        print("Welcome Back Tanishq Rai!")
    elif ee!="rai.tanishq@gmail.com" or ee!="9717180804" and ff!="aart1234":
        print("User Not Registered With Us")
        print(sign_up())
    elif ee=="rai.tanishq@gmail.com" or ee=="9717180804" and ff!="aart1234":
        print("Password is incorrect")
        print("Try Again or Rest your Password")
        print(Password_reset())
f=str(input("Do you already have an account. Y/N :"))
if f=='N' or f=='n':
    print(sign_up())
if f=='Y' or f=='y':
    print (login_details())




j=input("DOMESTIC/INTERNATIONAL:")
if j=="Domsetic" or j=="DOMESTIC" or j=="DOMESTIC" :
    k=input("One Way/Round Trip :")
    if k=="One Way" or k=="ONE WAY" or k=="one way" :
        n=input("Departure :")
        q=input("Arrival :")
        print("\n")
        m=input("Month:")
        d=int(input("Date:"))
        while d<1 or d>31:
            print("invalid input")
            d=int(input("Date:"))
        y=int(input("Year:"))
        while y<2019 or y>2021:
            print("no flights avaiable")
            print("\n")
        p=int(input("No of Adults (>13) :"))
        x=int(input("No of Children (Age 2-12 years) :"))
        z=int(input("No of Infants( Age 7 days-2years) :"))
        psg= p+x+z
        if p<8 and x<8 and z<2:
            print("Total No. of passengers", psg)
        if m=="January" or m=="JANUARY" or m=="February" or m=="FEBRUARY" or m=="March" or m=="MARCH" or m=="April" or m=="APRIL" or m=="May" or m=="MAY"  or m=="June" or m=="JUNE":
            print (flight_onewayd())
        if m=="July" or m=="JULY" or m=="August" or m=="AUGUST" or m=="September" or m=="SEPTEMBER" or m=="OCTOBER" or m=="October" or m=="November" or m=="NOVEMBER"  or m=="December" or m=="DECEMBER":
             print(flightonewayd_winters())
    if k=="Round Trip" or k=="ROUND TRIP" or k=="round trip":
        nn=input("Departure :")
        qq=input("Arrival :")
        print("\n")
        mm=input("Month:")
        dd=int(input("Date:"))
        while dd<1 or dd>31:
            print("invalid input")
        yy=int(input("Year:"))
        while yy<2019 or yy>2021:
            print("no flights avaiable")
            print("\n")
        p=int(input("No of Adults (>13) :"))
        x=int(input("No of Children (Age 2-12 years) :"))
        z=int(input("No of Infants( Age 7 days-2years) :"))
        psg= p+x+z
        if p<8 and x<8 and z<2:
            print("Total No. of passengers", psg)
        if mm=="January" or mm=="JANUARY" or mm=="February" or mm=="FEBRUARY" or mm=="March" or mm=="MARCH" or mm=="April" or mm=="APRIL" or mm=="May" or mm=="MAY"  or mm=="June" or mm=="JUNE":
            print(flightonewayd_winters())
        if mm=="July" or mm=="JULY" or mm=="August" or mm=="AUGUST" or mm=="September" or mm=="SEPTEMBER" or mm=="OCTOBER" or mm=="October" or mm=="November" or mm=="NOVEMBER"  or mm=="December" or mm=="DECEMBER":
            print(flight_onewayd())

        print("RETURN DETAILS")
        nn=input("Departure :")
        qq=input("Arrival :")
        print("\n")
        mm=input("Month:")
        dd=int(input("Date:"))
        while dd<1 or dd>31:
            print("invalid input")
            dd=int(input("Date:"))
        yy=int(input("Year:"))
        while yy<2019 or yy>2021:
            print("no flights avaiable")
            print("\n")
        p=int(input("No of Adults (>13) :"))
        x=int(input("No of Children (Age 2-12 years) :"))
        z=int(input("No of Infants( Age 7 days-2years) :"))
        psg= p+x+z
        if p<8 and x<8 and z<2:
            print("Total No. of passengers", psg)
        if mm=="January" or mm=="JANUARY" or mm=="February" or mm=="FEBRUARY" or mm=="March" or mm=="MARCH" or mm=="April" or mm=="APRIL" or mm=="May" or mm=="MAY"  or mm=="June" or mm=="JUNE":
            print(flight_onewayd())
        if mm=="July" or mm=="JULY" or mm=="August" or mm=="AUGUST" or mm=="September" or mm=="SEPTEMBER" or mm=="OCTOBER" or mm=="October" or mm=="November" or mm=="NOVEMBER"  or mm=="December" or mm=="DECEMBER":
            print(flightonewayd_winters())
            
