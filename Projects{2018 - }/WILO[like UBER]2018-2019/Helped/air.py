import time 
print("Welcome to TT Airlines!")
time.sleep(0.5) 
def rules_regulationsd():
    print("Rules and Regulations")
    print("1. Domestic Flight Check in opens 150 minutes before departure and closes 60 minutes prior to scheduled departure.")
    print("2. Flight Timings are subject to change with prior notice. Please recheck with carrier prior to departure.")
    print("3. It is mandatory to carry Government recognized photo identifications along with E-Ticket.")
    print("4. Maximum baggage 25 kg only.")
def rules_regulationsii():
    print("Rules and Regulations")
    print("1. International Flight Check in opens 160 minutes before departure and closes 40 minutes prior to scheduled departure.")
    print("2. Flight Timings are subject to change with prior notice. Please recheck with carrier prior to departure.")
    print("3. It is mandatory to carry Passport along with E-Ticket.")
    print("4. Maximum baggage 35 kg only.")

def international_oneway():
    print ("1. TR123   2 hrs       non-stop       18:00-20:00      Economy class",      ipsg,"travellers",       "$",980)
    time.sleep(0.5)
    print("\n")
    print("2. TR234    4 hrs        3 stops       13:00-18:00      Economy class",      ipsg,"travellers",       "$",3400)
    time.sleep(0.5)
    print("\n")
    print("3. TR212    3 hrs        2 stop        04:30-07:30      Economy class",      ipsg,"travellers",        "$",2000)
    time.sleep(0.5)
    print("\n")
    print("4. TR241    1 hr         1 stop        02:30-08:30      Economy class",      ipsg,"travellers",       "$",550)
    time.sleep(0.5)
    print("\n")
    print(ijfmamj())
    


def international_roundway():
    print ("1. TR987      3 hrs     non-stop       10:00-13:00      Economy class",     ipsg,"travellers",       "$",1250)
    time.sleep(0.5)
    print("\n")
    print("2. TR687       2 hrs      1 stop        07:15-:09:15     Economy class",      ipsg,"travellers",       "$",230)
    time.sleep(0.5)
    print("\n")
    print("3. TR657       4 hrs      2 stop        02:30-06:30      Economy class",      ipsg,"travellers",        "$",1000)
    time.sleep(0.5)
    print("\n")
    print("4. TR486       1 hr       non-stop      10:30-11:30      Economy class",      ipsg,"travellers",       "$",950)
    time.sleep(0.5)
    print("\n")
    print(ijasondec())

def ijfmamj(): 
    a=str(input("Enter the No. :"))
    if a=="1":
         print(" You have chosen Flight No. TR123")
         s=input("Do you want to do enquiry for another flight? Y/N:")
         if s=='y' or s=='Y':
           print(international_oneway())
         elif s=='N' or s=='n':
             print("Total fare for", ipsg, "Passengers=","$", ipsg*980)
             time.sleep(0.5)
             print(aa,bb)
             print("Contact No.",mn)
             time.sleep(0.5)
             print("Flight Details -")
             print("Flight No : TR123")
             time.sleep(0.5)
             print("Departure Time- 18:00 hrs")
             print ("Arrival Time-  20:00 hrs")
             print(rules_regulationsii())
    elif a=="2":
         print(" You have chosen Flight No. TR234")
         s=input("Do you want to do enquiry for another flight? Y/N:")
         if s=='Y' or s=='y':
           print(international_oneway())
         elif s=='N' or s=='n':
             print("Total fare for", ipsg, "Passengers=","$", ipsg*3400)
             time.sleep(0.5)
             print(aa,bb)
             print("Contact No.",mn)
             time.sleep(0.5)
             print("Flight Details -")
             print("Flight No : TR234")
             time.sleep(0.5)
             print("Departure Time- 13:00 hrs")
             print ("Arrival Time-  18:00 hrs")
             print(rules_regulationsii())
             
             
    if a=="3":
         print(" You have chosen Flight No. TR212")
         s=input("Do you want to do enquiry for another flight? Y/N:")
         if s=='Y' or s=='y':
           print(international_oneway())
         elif s=='N' or s=='n':
             print("Total fare for", ipsg, "Passengers=","$",  ipsg*2000)
             time.sleep(0.5)
             print(aa,bb)
             print("Contact No.",mn)
             time.sleep(0.5)
             print("Flight Details -")
             print("Flight No : TR212")
             time.sleep(0.5)
             print("Departure Time- 04:30 hrs")
             print ("Arrival Time-  07:00 hrs")
             print(rules_regulationsii())
             
    if a=="4":
         print(" You have chosen Flight No. TR241")
         s=input("Do you want to do enquiry for another flight? Y/N:")
         if s=='Y' or s=='y':
           print(international_oneway())
         elif s=='N' or s=='n':
             print("Total fare for", ipsg, "Passengers=","$", ipsg*550)
             time.sleep(0.5)
             print(aa,bb)
             print("Contact No.",mn)
             time.sleep(0.5)
             print("Flight Details -")
             print("Flight No : TR241")
             time.sleep(0.5)
             print("Departure Time- 02:30 hrs")
             print ("Arrival Time- 08:30 hrs")
             print(rules_regulationsii())
             
def ijasondec(): 
    a=str(input("Enter the No. :"))
    if a=="1":
         print(" You have chosen Flight No. TR987")
         s=input("Do you want to do enquiry for another flight? Y/N:")
         if s=='y' or s=='Y':
           print(international_roundway())
         elif s=='N' or s=='n':
             print("Total fare for", ipsg, "Passengers=","$", ipsg*1250)
             time.sleep(0.5)
             print(aa,bb)
             print("Contact No.",mn)
             time.sleep(0.5)
             print("Flight Details -")
             print("Flight No : TR987")
             time.sleep(0.5)
             print("Departure Time- 10:00 hrs")
             print ("Arrival Time- 13:00 hrs")
             print(rules_regulationsii())
             
    if a=="2":
         print(" You have chosen Flight No. TR687")
         s=input("Do you want to do enquiry for another flight? Y/N:")
         if s=='Y' or s=='y':
           print(international_roundway())
         elif s=='N' or s=='n':
             print("Total fare for", ipsg, "Passengers=","$", ipsg*230)
             time.sleep(0.5)
             print(aa,bb)
             print("Contact No.",mn)
             time.sleep(0.5)
             print("Flight Details -")
             print("Flight No : TR687")
             time.sleep(0.5)
             print("Departure Time- 07:15 hrs")
             print ("Arrival Time-  09:15 hrs")
             print(rules_regulationsii())
             
    if a=="3":
         print(" You have chosen Flight No. TR657")
         s=input("Do you want to do enquiry for another flight? Y/N:")
         if s=='Y' or s=='y':
           print(international_roundway())
         elif s=='N' or s=='n':
             print("Total fare for", ipsg, "Passengers=","$", ipsg*1000)
             time.sleep(0.5)
             print(aa,bb)
             print("Contact No.",mn)
             time.sleep(0.5)
             print("Flight Details -")
             print("Flight No : TR657")
             time.sleep(0.5)
             print("Departure Time- 02:30 hrs")
             print ("Arrival Time-  06:30 hrs")
             print(rules_regulationsii())
             
    if a=="4":
         print(" You have chosen Flight No. TR486")
         s=input("Do you want to do enquiry for another flight? Y/N:")
         if s=='Y' or s=='y':
           print(international_roundway())
         elif s=='N' or s=='n':
             print("Total fare for", ipsg, "Passengers=","$", ipsg*950)
             time.sleep(0.5)
             print(aa,bb)
             print("Contact No.",mn)
             time.sleep(0.5)
             print("Flight Details -")
             print("Flight No : TR486")
             time.sleep(0.5)
             print("Departure Time- 08:30 hrs")
             print ("Arrival Time-  09:30 hrs")
             print(rules_regulationsii())


def flight_onewayd():
    print ("1. LJ230   3 hrs     non-stop     16:00-19:00      Economy class",     psg,"travellers",       "₹",4230)
    time.sleep(0.5)
    print("\n")
    print("2. LJ237    5 hrs      1 stop      13:00-18:00      Economy class",      psg,"travellers",       "₹",6000)
    time.sleep(0.5)
    print("\n")
    print("3. LJ234    3 hrs     non-stop     04:30-07:30      Economy class",      psg,"travellers",        "₹",7000)
    time.sleep(0.5)
    print("\n")
    print("4. LJ768    6 hrs      2 stops     02:30-08:30      Economy class",      psg,"travellers",       "₹",7500)
    time.sleep(0.5)
    print("\n")
    print(jfmamj())
def flightonewayd_winters():
    print("1. LJ567   2 hrs     non-stop     17:00-19:00      Economy class",      psg,"travellers",       "₹",5500)
    time.sleep(0.5)
    print("\n")
    print("2. LJ989    3 hrs      2 stops      12:30-15:30     Economy class",      psg,"travellers",       "₹",7200)
    time.sleep(0.5)
    print("\n")
    print("3. LJ350    4 hrs     non-stop     08:00-12:00      Economy class",      psg,"travellers",       "₹",9000)
    time.sleep(0.5)
    print("\n")
    print("4. LJ134    1 hr      1 stop     08:30-09:30        Economy class",      psg,"travellers",       "₹",3000)
    time.sleep(0.5)
    print("\n")
    print(jasondec())
 
def jfmamj(): 
    a=str(input("Enter the No. :"))
    if a=="1":
         print(" You have chosen Flight No. LJ230")
         s=input("Do you want to do enquiry for another flight? Y/N:")
         if s=='y' or s=='Y':
           print(flight_onewayd())
         elif s=='N' or s=='n':
             print("Total fare for", psg, "Passengers=","₹", psg*4230)
             time.sleep(0.5)
             print(aa,bb)
             print("Contact No.",mn)
             time.sleep(0.5)
             print("Flight Details -")
             print("Flight No : LJ230")
             time.sleep(0.5)
             print("Departure Time- 16:00 hrs")
             print ("Arrival Time- 19:00 hrs")
             print(rules_regulationsd())
    if a=="2":
             print(" You have chosen Flight No. LJ237")
             s=input("Do you want to do enquiry for another flight? Y/N:")
             if s=='Y' or s=='y':
                 print(flight_onewayd())
             elif s=='N' or s=='n':
                 print("Total fare for", psg, "Passengers=","₹", psg*6000)
                 time.sleep(0.5)
                 print(aa,bb)
                 print("Contact No.",mn)
                 time.sleep(0.5)
                 print("Flight Details -")
                 print("Flight No : LJ237")
                 time.sleep(0.5)
                 print("Departure Time- 13:00 hrs")
                 print ("Arrival Time- 18:00 hrs")
                 print(rules_regulationsd())
             
    if a=="3":
         print(" You have chosen Flight No. LJ234")
         s=input("Do you want to do enquiry for another flight? Y/N:")
         if s=='Y' or s=='y':
           print(flight_onewayd())
         elif s=='N' or s=='n':
             print("Total fare for", psg, "Passengers=",'₹',  psg*7000)
             time.sleep(0.5)
             print(aa,bb)
             print("Contact No.",mn)
             time.sleep(0.5)
             print("Flight Details -")
             print("Flight No : LJ234")
             time.sleep(0.5)
             print("Departure Time- 04:30 hrs")
             print ("Arrival Time-  07:00 hrs")
             print(rules_regulationsd())
             
    if a=="4":
         print(" You have chosen Flight No. LJ768")
         s=input("Do you want to do enquiry for another flight? Y/N:")
         if s=='Y' or s=='y':
           print(flight_onewayd())
         elif s=='N' or s=='n':
             print("Total fare for", psg, "Passengers=", "₹",psg*7500)
             time.sleep(0.5)
             print(aa,bb)
             print("Contact No.",mn)
             time.sleep(0.5)
             print("Flight Details -")
             print("Flight No : LJ768")
             time.sleep(0.5)
             print("Departure Time- 02:30 hrs")
             print ("Arrival Time- 08:30 hrs")
             print(rules_regulationsd())
             
def jasondec(): 
    a=str(input("Enter the No. :"))
    if a=="1":
         print(" You have chosen Flight No. LJ567")
         s=input("Do you want to do enquiry for another flight? Y/N:")
         if s=='y' or s=='Y':
           print(flightonewayd_winters())
         elif s=='N' or s=='n':
             print("Total fare for", psg, "Passengers=", "₹",psg*5500)
             time.sleep(0.5)
             print(aa,bb)
             print("Contact No.",mn)
             time.sleep(0.5)
             print("Flight Details -")
             print("Flight No : LJ567")
             time.sleep(0.5)
             print("Departure Time- 17:00 hrs")
             print ("Arrival Time- 19:00 hrs")
             print(rules_regulationsd())
             
    if a=="2":
         print(" You have chosen Flight No. LJ989")
         s=input("Do you want to do enquiry for another flight? Y/N:")
         if s=='Y' or s=='y':
           print(flightonewayd_winters())
         elif s=='N' or s=='n':
             print("Total fare for", psg, "Passengers=","₹", psg*7200)
             time.sleep(0.5)
             print(aa,bb)
             print("Contact No.",mn)
             time.sleep(0.5)
             print("Flight Details -")
             print("Flight No : LJ989")
             time.sleep(0.5)
             print("Departure Time- 12:30 hrs")
             print ("Arrival Time-  15:00 hrs")
             print(rules_regulationsd())
             
    if a=="3":
         print(" You have chosen Flight No. LJ350")
         s=input("Do you want to do enquiry for another flight? Y/N:")
         if s=='Y' or s=='y':
           print(flightonewayd_winters())
         elif s=='N' or s=='n':
             print("Total fare for", psg, "Passengers=","₹", psg*9000)
             time.sleep(0.5)
             print(aa,bb)
             print("Contact No.",mn)
             time.sleep(0.5)
             print("Flight Details -")
             print("Flight No : LJ350")
             time.sleep(0.5)
             print("Departure Time- 08:00 hrs")
             print ("Arrival Time-  12:00 hrs")
             print(rules_regulationsd())
             
    if a=="4":
         print(" You have chosen Flight No. LJ134")
         s=input("Do you want to do enquiry for another flight? Y/N:")
         if s=='Y' or s=='y':
           print(flightonewayd_winters())
         elif s=='N' or s=='n':
             print("Total fare for", psg, "Passengers=", "₹",psg*3000)
             time.sleep(0.5)
             print(aa,bb)
             print("Contact No.",mn)
             time.sleep(0.5)
             print("Flight Details -")
             print("Flight No : LJ2134")
             time.sleep(0.5)
             print("Departure Time- 08:30 hrs")
             print ("Arrival Time-  09:30 hrs")
             print(rules_regulationsd())




def sign_up():
    time.sleep(0.5)
    print("Singup to book your tickets")
    zz=str(input("Enter Your Email id :"))
    dd=str(input("Enter Password :"))
    ee=str(input("Re enter Password :"))
    if dd==ee:
        print("Welcome",aa,bb, '!')
    else:
            print("Password doesn't match")
            print(Password_reset())
def Password_reset():
    time.sleep(0.5)
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
    gg=str(input("Enter your Email id or Phone No. :"))
    ff=str(input("Enter the Password :"))
    if gg=="rai.tanishq@gmail.com" or gg=="9717180804" and ff=="aart1234":
        print("Welcome Back Tanishq Rai!")
    elif gg!="rai.tanishq@gmail.com" or gg!="9717180804" and ff!="aart1234":
        print("User Not Registered With Us")
        print(sign_up())
    elif ee=="rai.tanishq@gmail.com" or ee=="9717180804" and ff!="aart1234":
        print("Password is incorrect")
        print("Try Again or Rest your Password")
        print(Password_reset())
aa=str(input("Enter your First Name :"))
bb=str(input("Enter Your Surname :"))
f=str(input("Do you already have an account. Y/N :"))
mn=int(input("Enter your Phone No."))
if f=='N' or f=='n':
    print(sign_up())
if f=='Y' or f=='y':
    print (login_details())



j=input("DOMESTIC/INTERNATIONAL :")
if j=="International" or j=="INTERNATIONAL" or j=="international" :
    ik=input("One Way/Multi-City/Round Trip :")
    if ik=="One Way" or ik=="ONE WAY" or ik=="one way" :
        idd=input("Departure :")
        iaa=input("Arrival :")
        print("\n")
        imm=input("Month :")
        idd=int(input("Date :"))
        while idd<1 or idd>31:
            print("invalid input")
            idd=int(input("Date :"))
        iyy=int(input("Year:"))
        while iyy<2019 or iyy>2021:
            print("no flights avaiable")
            print("\n")
        ip=int(input("No of Adults (>13years) :"))
        ix=int(input("No of Children (Age 2-12 years) :"))
        iz=int(input("No of Infants( Age 7 days-2years) :"))
        ipsg= ip+ix+iz
        if ip<8 and ix<8 and iz<2:
            print("Total No. of passengers", ipsg)
        if imm=="January" or imm=="JANUARY" or imm=="February" or imm=="FEBRUARY" or imm=="March" or imm=="MARCH" or imm=="April" or imm=="APRIL" or imm=="May" or imm=="MAY"  or imm=="June" or imm=="JUNE":
            print(international_oneway())
        if imm=="July" or imm=="JULY" or imm=="August" or imm=="AUGUST" or imm=="September" or imm=="SEPTEMBER" or imm=="OCTOBER" or imm=="October" or imm=="November" or imm=="NOVEMBER"  or imm=="December" or imm=="DECEMBER":
            print(international_roundway())
    if ik=="ROUND TRIP" or ik=="round trip" or ik=="Round Trip":
        irdd=input("Departure :")
        iraa=input("Arrival :")
        print("\n")
        irmm=input("Month :")
        irddd=int(input("Date :"))
        while irddd<1 or irddd>31:
            print("Invalid Input")
            irddd=int(input("Date :"))
        iryy=int(input("Year:"))
        while iryy<2019 or iryy>2021:
            print("No flights are avaiable")
            print("\n")
        ipp=int(input("No of Adults (>13years) :"))
        ixx=int(input("No of Children (Age 2-12 years) :"))
        izz=int(input("No of Infants( Age 7 days-2years) :"))
        ipsg= ipp+ixx+izz
        if ipp<8 and ixx<8 and izz<2:
            print("Total No. of passengers", ipsg)
        if irmm=="January" or irmm=="JANUARY" or irmm=="February" or irmm=="FEBRUARY" or irmm=="March" or irmm=="MARCH" or irmm=="April" or irmm=="APRIL" or irmm=="May" or irmm=="MAY"  or irmm=="June" or irmm=="JUNE":
            print(international_oneway())
        if irmm=="July" or irmm=="JULY" or irmm=="August" or irmm=="AUGUST" or irmm=="September" or irmm=="SEPTEMBER" or irmm=="OCTOBER" or irmm=="October" or irmm=="November" or irmm=="NOVEMBER"  or irmm=="December" or irmm=="DECEMBER":
            print(international_roundway())
            print("\n")
            print("RETURN DETAILS")
        print("Departure from",iraa,"Arrival At",irdd)
        print("\n")
        irmm=input("Month :")
        rd=int(input("Date :"))
        while rd<1 or rd>31:
            print("invalid input")
            rd=int(input("Date :"))
        ry=int(input("Year :"))
        while ry<2019 or ry>2021:
            print("no flights avaiable")
            print("\n")
        if irmm=="January" or irmm=="JANUARY" or irmm=="February" or irmm=="FEBRUARY" or irmm=="March" or irmm=="MARCH" or irmm=="April" or irmm=="APRIL" or irmm=="May" or irmm=="MAY"  or irmm=="June" or irmm=="JUNE":
            print(international_roundway())
        if irmm=="July" or irmm=="JULY" or irmm=="August" or irmm=="AUGUST" or irmm=="September" or irmm=="SEPTEMBER" or irmm=="OCTOBER" or irmm=="October" or irmm=="November" or irmm=="NOVEMBER"  or irmm=="December" or irmm=="DECEMBER":
            print(international_oneway())

    if ik=="MULTI-CITY" or ik=="multi-city" or ik=="Multi-City":
        idd=input("Departure :")
        iaa=input("Arrival :")
        print("\n")
        imm=input("Month :")
        idd=int(input("Date :"))
        while idd<1 or idd>31:
            print("Invalid Input")
            idd=int(input("Date :"))
        iyy=int(input("Year:"))
        while iyy<2019 or iyy>2021:
            print("No flights are avaiable")
            print("\n")
        ip=int(input("No of Adults (>13years) :"))
        ix=int(input("No of Children (Age 2-12 years) :"))
        iz=int(input("No of Infants( Age 7 days-2years) :"))
        ipsg= ip+ix+iz
        if ip<8 and ix<8 and iz<2:
            print("Total No. of passengers", ipsg)
        if imm=="January" or imm=="JANUARY" or imm=="February" or imm=="FEBRUARY" or imm=="March" or imm=="MARCH" or imm=="April" or imm=="APRIL" or imm=="May" or imm=="MAY"  or imm=="June" or imm=="JUNE":
            print(international_oneway())
        if imm=="July" or imm=="JULY" or imm=="August" or imm=="AUGUST" or imm=="September" or imm=="SEPTEMBER" or imm=="OCTOBER" or imm=="October" or imm=="November" or imm=="NOVEMBER"  or imm=="December" or imm=="DECEMBER":
            print(international_roundway())
        print("\n")
        print("Departure :", iaa)
        qq=input("Arrival :")
        print("\n")
        imm=input("Month :")
        dd=int(input("Date :"))
        while dd<1 or dd>31:
            print("invalid input")
            dd=int(input("Date :"))
        yy=int(input("Year:"))
        while yy<2019 or yy>2021:
            print("no flights avaiable")
            print("\n")
        if imm=="January" or imm=="JANUARY" or imm=="February" or imm=="FEBRUARY" or imm=="March" or imm=="MARCH" or imm=="April" or imm=="APRIL" or imm=="May" or imm=="MAY"  or imm=="June" or imm=="JUNE":
            print(international_roundway())
        if imm=="July" or imm=="JULY" or imm=="August" or imm=="AUGUST" or imm=="September" or imm=="SEPTEMBER" or imm=="OCTOBER" or imm=="October" or imm=="November" or imm=="NOVEMBER"  or imm=="December" or imm=="DECEMBER":
            print(international_oneway())


if j=="Domestic" or j=="DOMESTIC" or j=="domestic" :
    k=input("One Way/Multi-City/Round Trip : ")
    if k=="ROUND TRIP" or k=="Round Trip" or k=="round trip":
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
             print("\n")
        print("RETURN DETAILS")
        print("Departure from",q,"Arrival At",n)
        print("\n")
        rm=input("Month :")
        rd=int(input("Date :"))
        while rd<1 or rd>31:
            print("invalid input")
            rd=int(input("Date :"))
        ry=int(input("Year :"))
        while ry<2019 or ry>2021:
            print("no flights avaiable")
            print("\n")
        if rm=="January" or rm=="JANUARY" or rm=="February" or rm=="FEBRUARY" or rm=="March" or rm=="MARCH" or rm=="April" or rm=="APRIL" or rm=="May" or rm=="MAY"  or rm=="June" or rm=="JUNE":
            print(flightonewayd_winters())
        elif rm=="July" or rm=="JULY" or rm=="August" or rm=="AUGUST" or rm=="September" or rm=="SEPTEMBER" or rm=="OCTOBER" or rm=="October" or rm=="November" or rm=="NOVEMBER"  or rm=="December" or rm=="DECEMBER":
            print (flight_onewayd())
    if k=="One Way" or k=="ONE WAY" or k=="one way":
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
    if k=="MULTI-CITY" or k=="Multi-City" or k=="multi-city":
        dnn=input("Departure :")
        dqq=input("Arrival :")
        print("\n")
        ddmm=input("Month:")
        ddd=int(input("Date:"))
        while ddd<1 or ddd>31:
            print("invalid input")
        dyy=int(input("Year:"))
        while dyy<2019 or dyy>2021:
            print("no flights avaiable")
            print("\n")
        p=int(input("No of Adults (>13) :"))
        x=int(input("No of Children (Age 2-12 years) :"))
        z=int(input("No of Infants( Age 7 days-2years) :"))
        psg= p+x+z
        if p<8 and x<8 and z<2:
            print("Total No. of passengers", psg)
        if ddmm=="January" or ddmm=="JANUARY" or ddmm=="February" or ddmm=="FEBRUARY" or ddmm=="March" or ddmm=="MARCH" or ddmm=="April" or ddmm=="APRIL" or ddmm=="May" or ddmm=="MAY"  or ddmm=="June" or ddmm=="JUNE":

            print(flightonewayd_winters())
        if ddmm=="July" or ddmm=="JULY" or ddmm=="August" or ddmm=="AUGUST" or ddmm=="September" or ddmm=="SEPTEMBER" or ddmm=="OCTOBER" or ddmm=="October" or ddmm=="November" or ddmm=="NOVEMBER"  or ddmm=="December" or ddmm=="DECEMBER":
            print(flight_onewayd())
        print("\n")
        print("Departure :", dnn)
        dqq=input("Arrival :")
        print("\n")
        dmm=input("Month :")
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
        if dmm=="January" or dmm=="JANUARY" or dmm=="February" or dmm=="FEBRUARY" or dmm=="March" or dmm=="MARCH" or dmm=="April" or dmm=="APRIL" or dmm=="May" or dmm=="MAY"  or dmm=="June" or dmm=="JUNE":
            print(flight_onewayd())
        if dmm=="July" or dmm=="JULY" or dmm=="August" or dmm=="AUGUST" or dmm=="September" or dmm=="SEPTEMBER" or dmm=="OCTOBER" or dmm=="October" or dmm=="November" or dmm=="NOVEMBER"  or dmm=="December" or dmm=="DECEMBER":
            print(flightonewayd_winters())
