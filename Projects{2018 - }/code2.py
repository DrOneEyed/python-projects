import time


# Start Program

users={'gg': 'gg','GG':'GG'}
status=""
loginSuccess=0
global cartTotal
Cart=[]
Rate=[]


def headerBanner():
    print("\n"*5)
    print("\nWelcome to VMC Electronics")
    print("==========================\n")

def ShoppingCart():
    headerBanner()
    print("What would you like to buy today?")
    print("[1] Mobile")
    print("[2] Tablets")
    print("[3] Laptop")
    print("[4] Watch")
    print("[5] TV")
    print("[6] Earphones/Headphones")
    print("\n")
    print("[7] Check-Out")
    print("\n")
    print("[8] Rate Us/ Complain")
    print("[0] Quit ")
    mainCategory=input("\nChoose your option? ")
    if mainCategory=="1":
        mobileShop()
    elif mainCategory=="2":
        tabletShop()
    elif mainCategory=="3":
        laptopShop()
    elif mainCategory=="4":
        watchShop()
    elif mainCategory=="5":
        tvShop()
    elif mainCategory=="6":
        headphoneShop()
    elif mainCategory=="7":
        CheckOutCart()
    elif mainCategory=="8":
        headerBanner()
        Rating=input("Enter your review or complain here: ")
        print("Thanks for your feedback/ review.")
        print("We will get in touch with you with the resolution/ update.\n")
        input("Press any key to continue...")
    elif mainCategory=="0":
        exit()

def DisplayMenu():
    ShoppingCart()

def loginShop():
    headerBanner()
    status=input("[L]ogin/ [S]ign-up/ [Q]uit? ").upper()
    if status=="L":
        OldUser()
    elif status=="S":
        NewUser()
    elif status=="Q":
        exit()
    else:
        loginShop()

def NewUser():
    headerBanner()
    print("Sign-Up (New User)")
    print("==================\n")
    createLogin=input("New User name:").upper()
    if createLogin in users:
        print("\nUser Name already exists!\nChoose another...")
        input("Press any key to continue...")
        loginSuccess=1
        loginShop()
    else:
        createPassword=input("Password: ")
        users[createLogin]=createPassword
        print("\nUser Created...\n")
        input("Press any key to continue...")
        loginSuccess=0

def OldUser():
    headerBanner()
    print("Login (Existing User)")
    print("=====================\n")
    login=input("User Name: ").upper()
    password=input("Password: ")
    if(login in users and users[login]==password):
        print("\nLogin successful!\n")
        input("Press any key to continue...")
        loginSuccess=0
    else:
        print("User doesn't exist or wrong password!\n");
        input("Press any key to continue...")
        loginSuccess=1
        loginShop()
           
def mobileShop():
    global cartTotal
    headerBanner()
    print("Mobile Shop")
    print("===========\n")
    AddToCart="0";
    print("[1] FPhone 8       | $799")
    print("[2] FPhone 10      | $999")
    print("[3] FPhone 10X     | $1099")
    print("[4] FPhone 10 Max  | $1199")
    print("\n")
    print("[7] Check-Out")
    print("\n")
    print("[9] Prvious Menu")
    print("[0] Quit")
    shopOption=input("Choose your option? ")
    if shopOption=="1":
        print("OS        : iOS 10")
        print("Display   : 4.7\" Retina")
        print("Weight    : 148gm")
        print("Dimension : 1334 x 750")
        print("RAM       : 2GB")
        print("Camera    : 12MP")
        print("Resolution: 2160p")
        print("Battery   : 1821mAh")
        print("Memory    : 64GB")
        print("[1] Add to cart, [2] Go Back")
        AddToCart=input("Choose your option? ")
        if  AddToCart=="1":
            Cart.append("Fphone 8                :  $799")
            cartTotal=cartTotal+799
            mobileShop()
        elif AddToCart=="2":
            mobileShop()
        else:
            print("We didn't get any valid response, returning to main menu...")
            mobileShop()
    elif shopOption=="2":
        print("OS        : iOS 11.1.1")
        print("Display   : 5.8\" Retina")
        print("Weight    : 174gm")
        print("Dimension : 1125 x 2436")
        print("RAM       : 3GB")
        print("Camera    : 12MP")
        print("Resolution: 2160p")
        print("Battery   : 2716mAh")
        print("Memory    : 256GB")
        print("[1] Add to cart, [2] Go Back")
        AddToCart=input("Choose your option? ")
        if  AddToCart=="1":
            Cart.append("Fphone 10               :  $999")
            cartTotal=cartTotal+999
            mobileShop()
        elif AddToCart=="2":
            mobileShop()
        else:
            print("We didn't get any valid response, returning to main menu...")
            mobileShop()
    elif shopOption=="3":
        print("OS        : iOS 12")
        print("Display   : 5.8\" Retina")
        print("Weight    : 177gm")
        print("Dimension : 1125 x 2436")
        print("RAM       : 4GB")
        print("Camera    : 12MP")
        print("Resolution: 2160p")
        print("Battery   : 2658mAh")
        print("Memory    : 256GB")
        print("[1] Add to cart, [2] Go Back")
        AddToCart=input("Choose your option? ")
        if  AddToCart=="1":
            Cart.append("Fphone 10X              : $1099")
            cartTotal=cartTotal+1099
            mobileShop()
        elif AddToCart=="2":
            mobileShop()
        else:
            print("We didn't get any valid response, returning to main menu...")
            mobileShop()
    elif shopOption=="4":
        print("OS        : iOS 12")
        print("Display   : 6.5\" Retina")
        print("Weight    : 208gm")
        print("Dimension : 1242 x 2688")
        print("RAM       : 4GB")
        print("Camera    : 12MP")
        print("Resolution: 2160p")
        print("Battery   : 3174mAh")
        print("Memory    : 512GB")
        print("[1] Add to cart, [2] Go Back")
        AddToCart=input("Choose your option? ")
        if  AddToCart=="1":
            Cart.append("Fphone 10X Max          : $1199")
            cartTotal=cartTotal+1199
            mobileShop()
        elif AddToCart=="2":
            mobileShop()
        else:
            print("We didn't get any valid response, returning to main menu...")
            mobileShop()
    elif shopOption=="7":
        CheckOutCart()
    elif shopOption=="9":
        ShoppingCart()
    elif shopOption=="0":
        exit()

def tabletShop():
    global cartTotal
    headerBanner()
    print("TabletnShop")
    print("===========\n")
    AddToCart="0";
    print("[1] Fpad 6        | $499")
    print("[2] Fpad 7        | $799")
    print("[3] Fpad 8        | $999")
    print("[4] Fpad 8 Pro    | $1099")
    print("\n")
    print("[7] Check-Out")
    print("\n")
    print("[9] Prvious Menu")
    print("[0] Quit")
    shopOption=input("Choose your option? ")
    if shopOption=="1":
        print("OS        : iOS 8.1(Base)")
        print("Display   : 9.7\" Retina")
        print("Weight    : 437gm")
        print("Dimension : 1536 x 2048")
        print("RAM       : 2GB")
        print("Camera    : 8MP")
        print("Resolution: 1080p")
        print("Battery   : 7340mAh")
        print("Memory    : 64GB")
        print("[1] Add to cart, [2] Go Back")
        AddToCart=input("Choose your option? ")
        if  AddToCart=="1":
            Cart.append("Fpad 6                  :  $499")
            cartTotal=cartTotal+499
            tabletShop()
        elif AddToCart=="2":
            tabletShop()
        else:
            print("We didn't get any valid response, returning to main menu...")
            tabletShop()
    elif shopOption=="2":
        print("OS        : iOS 11.3")
        print("Display   : 9.7\" Retina")
        print("Weight    : 469gm")
        print("Dimension : 1536 x 2048")
        print("RAM       : 2GB")
        print("Camera    : 8MP")
        print("Resolution: 2160p")
        print("Battery   : 8827mAh")
        print("Memory    : 128GB")
        print("[1] Add to cart, [2] Go Back")
        AddToCart=input("Choose your option? ")
        if  AddToCart=="1":
            Cart.append("Fpad 7                  :  $799")
            cartTotal=cartTotal+799
            tabletShop()
        elif AddToCart=="2":
            tabletShop()
        else:
            print("We didn't get any valid response, returning to main menu...")
            tabletShop()
    elif shopOption=="3":
        print("OS        : iOS 12")
        print("Display   : 11.9\" Retina")
        print("Weight    : 468gm")
        print("Dimension : 1668 x 2388")
        print("RAM       : 4GB")
        print("Camera    : 12MP")
        print("Resolution: 2160p")
        print("Battery   : 8812mAh")
        print("Memory    : 1TB")
        print("[1] Add to cart, [2] Go Back")
        AddToCart=input("Choose your option? ")
        if  AddToCart=="1":
            Cart.append("Fpad 8                  :  $999")
            cartTotal=cartTotal+999
            tabletShop()
        elif AddToCart=="2":
            tabletShop()
        else:
            print("We didn't get any valid response, returning to main menu...")
            tabletShop()
    elif shopOption=="4":
        print("OS        : iOS 12")
        print("Display   : 12.5\" Retina")
        print("Weight    : 550gm")
        print("Dimension : 1788 x 2688")
        print("RAM       : 4GB")
        print("Camera    : 12MP")
        print("Resolution: 2500p")
        print("Battery   : 9000mAh")
        print("Memory    : 1TB")
        print("[1] Add to cart, [2] Go Back")
        AddToCart=input("Choose your option? ")
        if  AddToCart=="1":
            Cart.append("Fpad 8 Pro              : $1099")
            cartTotal=cartTotal+1099
            tabletShop()
        elif AddToCart=="2":
            tabletShop()
        else:
            print("We didn't get any valid response, returning to main menu...")
            tabletShop()
    elif shopOption=="7":
        CheckOutCart()
    elif shopOption=="9":
        ShoppingCart()
    elif shopOption=="0":
        exit()

def laptopShop():
    global cartTotal
    headerBanner()
    print("Laptop Shop")
    print("===========\n")
    AddToCart="0";
    print("[1] Macbook2      | $1499")
    print("[2] Macbook3      | $1999")
    print("\n")
    print("[7] Check-Out")
    print("\n")
    print("[9] Prvious Menu")
    print("[0] Quit")
    shopOption=input("Choose your option? ")
    if shopOption=="1":
        print("CPU        : 2.3GHz Quad Core")
        print("Processor  : Intel Core i5-based")
        print("Monitor    : 13\"")
        print("RAM        : 8GB")
        print("HDD/ SSD   : 512GB SSD")
        print("[1] Add to cart, [2] Go Back")
        AddToCart=input("Choose your option? ")
        if  AddToCart=="1":
            Cart.append("Macbook2                : $1499")
            cartTotal=cartTotal+1499
            laptopShop()
        elif AddToCart=="2":
            laptopShop()
        else:
            print("We didn't get any valid response, returning to main menu...")
            laptopShop()
    elif shopOption=="2":
        print("CPU        : 2.6GHz quad-core")
        print("Processor  : Intel Core i7-based")
        print("Monitor    : 15\"")
        print("RAM        : 8GB")
        print("HDD/ SSD   : 1TB SSD")
        print("[1] Add to cart, [2] Go Back")
        AddToCart=input("Choose your option? ")
        if  AddToCart=="1":
            Cart.append("Macbook3                : $1999")
            cartTotal=cartTotal+1999
            laptopShop()
        elif AddToCart=="2":
            laptopShop()
        else:
            print("We didn't get any valid response, returning to main menu...")
            laptopShop()
    elif shopOption=="7":
        CheckOutCart()
    elif shopOption=="9":
        ShoppingCart()
    elif shopOption=="0":
        exit()

def watchShop():
    global cartTotal
    headerBanner()
    print("Watch Shop")
    print("==========\n")
    AddToCart="0";
    print("[1] Max Watch     | $799")
    print("[2] Max Watch Pro | $999")
    print("\n")
    print("[7] Check-Out")
    print("\n")
    print("[9] Prvious Menu")
    print("[0] Quit")
    shopOption=input("Choose your option? ")
    if shopOption=="1":
        print("Dimensions : 41.5 x 35.4 x 11.4 mm (1.67 x 1.43 x 0.45 Inch)")
        print("Weight     : 52.4gm (1.83 oz)")
        print("Body       : Build Stainless Steel/Ceramic back")
        print("Waterproof : 50m")
        print("SIM        : No")
        print("[1] Add to cart, [2] Go Back")
        AddToCart=input("Choose your option? ")
        if  AddToCart=="1":
            Cart.append("Max Watch               :  $799")
            cartTotal=cartTotal+799
            watchShop()
        elif AddToCart=="2":
            watchShop()
        else:
            print("We didn't get any valid response, returning to main menu...")
            watchShop()
    elif shopOption=="2":
        print("Dimensions : 43.5 x 37.4 x 11.4 mm (1.67 x 1.43 x 0.45 Inch)")
        print("Weight     : 52.4gm (1.83 oz)")
        print("Body       : Build Stainless Steel/Ceramic back")
        print("Waterproof : 50m")
        print("SIM        : -")
        print("[1] Add to cart, [2] Go Back")
        AddToCart=input("Choose your option? ")
        if  AddToCart=="1":
            Cart.append("Max Watch Pro           :  $999")
            cartTotal=cartTotal+999
            watchShop()
        elif AddToCart=="2":
            watchShop()
        else:
            print("We didn't get any valid response, returning to main menu...")
            watchShop()
    elif shopOption=="7":
        CheckOutCart()
    elif shopOption=="9":
        ShoppingCart()
    elif shopOption=="0":
        exit()

def tvShop():
    global cartTotal
    headerBanner()
    print("TV Shop")
    print("=======\n")
    AddToCart="0";
    print("[1] Max TV        | $1599")
    print("\n")
    print("[7] Check-Out")
    print("\n")
    print("[9] Prvious Menu")
    print("[0] Quit")
    shopOption=input("Choose your option? ")
    if shopOption=="1":
        print("Model       : 65 Q9F")
        print("Description : 4K Smart QLED TV, , , ")
        print("            : Q Colour")
        print("            : Q Contrast")
        print("            : Q HDR Elite (HDR 10+)")
        print("[1] Add to cart, [2] Go Back")
        AddToCart=input("Choose your option? ")
        if  AddToCart=="1":
            Cart.append("Max TV                  : $1599")
            cartTotal=cartTotal+1599
            tvShop()
        elif AddToCart=="2":
            tvShop()
        else:
            print("We didn't get any valid response, returning to main menu...")
            tvShop()
    elif shopOption=="7":
        CheckOutCart()
    elif shopOption=="9":
        ShoppingCart()
    elif shopOption=="0":
        exit()

def headphoneShop():
    global cartTotal
    headerBanner()
    print("Headphone Shop")
    print("==============\n")
    AddToCart="0";
    print("[1] Wireless God  | $100")
    print("[2] Gaming God    | $300")
    print("\n")
    print("[7] Check-Out")
    print("\n")
    print("[9] Prvious Menu")
    print("[0] Quit")
    shopOption=input("Choose your option? ")
    if shopOption=="1":
        print("Description/ Features : JBL Signature Sound")
        print("                      : Up to 16-hour battery life")
        print("                      : Two-hour recharge time")
        print("                      : Comfort-fit fabric headband")
        print("                      : One-button universal remote with microphone")
        print("[1] Add to cart, [2] Go Back")
        AddToCart=input("Choose your option? ")
        if  AddToCart=="1":
            Cart.append("Wireless God            :  $100")
            cartTotal=cartTotal+100
            headphoneShop()
        elif AddToCart=="2":
            headphoneShop()
        else:
            print("We didn't get any valid response, returning to main menu...")
            headphoneShop()
    elif shopOption=="2":
        print("Description/ Features : Latency-free wireless performance audio on PC and works with PS4")
        print("                      : Wireless 7.1 virtual surround sound for pinpoint precision")
        print("                      : 7 days of wireless gaming on a single charge")
        print("                      : Retractable digital mic for uncompromised vocal clarity")
        print("                      : 1 Year Warranty")
        print("[1] Add to cart, [2] Go Back")
        AddToCart=input("Choose your option? ")
        if  AddToCart=="1":
            Cart.append("Gaming God              :  $300")
            cartTotal=cartTotal+300
            headphoneShop()
        elif AddToCart=="2":
            headphoneShop()
        else:
            print("We didn't get any valid response, returning to main menu...")
            headphoneShop()
    elif shopOption=="7":
        CheckOutCart()
    elif shopOption=="9":
        ShoppingCart()
    elif shopOption=="0":
        exit()

def CheckOutCart():
    headerBanner()
    print("Check-Out Cart")
    print("==============\n")
    for item in Cart:
        print(item)
    print("                        =======")    
    print("                         $", cartTotal)
    Modeofpay=input("Press 1 to pay with Cash, Press 2 to pay with Credit card/Debit Card:")
    Address=input("Enter your delivery address:")
    if Modeofpay=="1":
        print("Your product will be delivered to ",Address," by next 5 days. Keep your $",cartTotal," ready")
    elif Modeofpay=="2":
        print("We have recieved your payment of $",cartTotal," Your product will be delivered to ",Address," by next 5 days. ")
        
    print("Thanks for shopping with us.")
    print("Please do return next time.")
    input("Press any key to continue...")

loginShop()
while loginSuccess==0:
    cartTotal=0
    DisplayMenu()
