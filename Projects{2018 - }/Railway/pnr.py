def pnr():
    b=int(input("Enter Ticket Number: "))
    if b==5189123456:
        print("Your Train Will Reach At Your Station At 21:00")
        print("Name: Sakshum") 
        print("Age: 29")
        print("Sex:M")
        print("Berth: Top")
        print("M.O.P:Net Banking")
        print("Ph.No.:9756821436")
    elif b==5190123456:
        print("Your Train Will Reach At Your Station At 21:00")
        print("Name: Dev") 
        print("Age: 25")
        print("Sex:M")
        print("Berth: Bottom")
        print("M.O.P:Net Banking")
        print("Ph.No.:8545579120")
    elif b==5191112456:
        print("Your Train Will Reach At Your Station At 21:00")
        print("Name: Raj") 
        print("Age: 32")
        print("Sex:M")
        print("Berth: Side")
        print("M.O.P:Cash")
        print("Ph.No.:9755881436")
    elif b==5192123456:
        print("Your Train Will Reach At Your Station At 21:00")
        print("Name: Harsh") 
        print("Age: 27")
        print("Sex:M")
        print("Berth: Top")
        print("M.O.P: Cash")
        print("Ph.No.:9751821436")
    elif b==5193123456:
        print("Your Train Will Reach At Your Station At 21:00")
        print("Name: Aditi") 
        print("Age: 16")
        print("Sex: F")
        print("Berth: Top")
        print("M.O.P:Net Banking")
        print("Ph.No.:9476729103")
    elif b==5194123456:
        print("Your Train Will Reach At Your Station At 21:00")
        print("Name: Shilpa") 
        print("Age: 22")
        print("Sex:F")
        print("Berth: Bottom")
        print("M.O.P:Cash")
        print("Ph.No.:9756821437")

def ticket():
    log=str(input("Enter Email ID:"))
    pas=str(input("Enter Password:"))
    re=str(input("Reenter Password:"))
    if pas==re:
        n=[]
        a=[]
        s=[]
        pp=[]
        em=[]
        c=str(input("From: "))
        d=str(input("To: "))
        e=int(input("Enter Number Of Tickets You Want To Buy: "))
        cc=e+1
        for i in range(1,cc,1):
            print("Enter Details For",i,"Ticket")
            name=input("Enter Name: ")
            age=input("Enter Age: ")
            sex=input("Enter Sex: ")
            p=input("Enter Ph.No.: ")
            email=input("Enter Email: ")
            n.append(name)
            a.append(age)
            s.append(sex)
            pp.append(p)
            em.append(email)
        print(', '.join(n))
        print(', '.join(a))
        print(', '.join(s))
        print(', '.join(pp))
        print(', '.join(em))
        sure=str(input("1. To Confirm OR 2. To Book Again"))
        if sure=='1':
            print("A Copy Of Ticket Has Been Sent To Your Email")
        else:
            print(ticket())
            more=str(input("1. To Exit"))
    else:
        print("Try again")
        log=str(input("Enter Email ID:"))
        pas=str(input("Enter Password:"))
        re=str(input("Reenter Password:"))
        n=[]
        a=[]
        s=[]
        pp=[]
        em=[]
        c=str(input("From: "))
        d=str(input("To: "))
        e=int(input("Enter Number Of Tickets You Want To Buy: "))
        cc=e+1
        for i in range(1,cc,1):
            print("Enter Details For",i,"Ticket")
            name=input("Enter Name: ")
            age=input("Enter Age: ")
            sex=input("Enter Sex: ")
            p=input("Enter Ph.No.: ")
            email=input("Enter Email: ")
            n.append(name)
            a.append(age)
            s.append(sex)
            pp.append(p)
            em.append(email)
        print(', '.join(n))
        print(', '.join(a))
        print(', '.join(s))
        print(', '.join(pp))
        print(', '.join(em))
        sure=str(input("1. To Confirm OR 2. To Book Again"))
        if sure=='1':
            print("A Copy Of Ticket Has Been Sent To Your Email")
        else:
            print(ticket())
            more=str(input("1. To Exit"))
print("Welcome NAIMIC")
a=str(input("1. for checking your PNR status OR 2. For Booking Ticket"))
if a=="1":
    print(pnr())
else:
    print(ticket())
