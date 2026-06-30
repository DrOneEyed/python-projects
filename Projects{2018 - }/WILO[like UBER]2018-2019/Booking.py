from geopy.distance import geodesic
import random
import time
def book_ride():
    print("Your Current Location")
    #str(input("Where To? "))  
    book_fee=10
    dest=(28.5355, 77.3910)
    current = (29.8543, 77.8880)
    dist=(geodesic(current, dest).miles)
    z=dist
    vehical=str(input("Press 1 for Auto Or 2 for Sedan Or 3 for SUV Or 4 for Pool('Sedan Only') "))
    if vehical=='1':
        base=5
        fare=base+book_fee+(z*5)
        print(fare)
    elif vehical=='2':
        base=20
        fare=base+book_fee+(z*5)
        print(fare)
    elif vehical=='3':
        base=35
        fare=base+book_fee+(z*5)
        print(fare)
    elif vehical=='4':
        base=10
        fare=(base+book_fee+(z*5))/3
        print(fare)
    else:
        print("Invalid input")
        print(book_ride())
    confirm=str(input("Press 1 to CONFIRM or 2 to CANCEL"))
    if confirm=='1':
        print("Finding your ride")
        print(finding())
    else:
        p=str(input("Are you sure you want to CANCEL your ride. Enter Yes or No "))
        if p=='Yes' or p=='yes'or p=='YES':
            print(book_ride())
        else:
            print("Finding your ride")
            print(finding())
    time.sleep(2)
    print("Your Driver Is Here!")
    time.sleep(5)
    print("You have reached your destination")
    time.sleep(2)
    g=str(input("Enter Number Of Stars For Your Ride: "))
    print("Thank You")

def finding():
    driver=['Ram','Sham',"Ritu",'David','Rajdeep','Rahul','Shubham','Nupur','Sudhir','Majnu']
    print('Driver Name: ',random.choice(driver))
    Number_Plate=['DL','UK','HR']
    print('Number Plate: ',random.choice(Number_Plate))
    phone_no=['12','34','42','56','67','78','45','90','87','11']
    print('Phone Number: ',random.choice(phone_no))
print(book_ride())
