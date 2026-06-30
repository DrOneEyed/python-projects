import time 
x=0
print("Welcome to VMC Electronics")
time.sleep(1)
x=x+1
users={}
status=""
Cart=[]
Rate=[]
aa='799'
def buy():
        buy2=input("What would you like to buy today? Press 1 for Mobile, Press 2 for Tablets, Press 3 for Laptop, Press 4 for watch,  Press 5 for TV, Press 6 for Earphones/Headphones, Press 7 to log out, Press 8 to exit the app (auto-logout), Press 9 to rate us or complain, Press 10 to checkout:")
        if buy2=="1":
            buy3=input("Fphone 8 | $799 Click 1 to see,      Fphone 10 | $999 Click 2 to see,      Fphone 10X | $ 1099 Click 3 to see,     Fphone 10 Max  | $1199 Click 4 to see,     Click 5 to go back,     Click 6 to  log out,     Click 7 to exit:")
            if buy3=="1":
                Fphone8=input("IOS 10, 4.7 inch retina, 148gm, 1334 x 750, 2GB RAM, 12 MP Camera 2160p quality, 1821mAh, 64 GB | Press 1 to add to cart | Press 2 to go back")
                if  Fphone8=="1":
                    Cart.append("Fphone 8")
                    print("Here is your cart",Cart)
                    buy()
                elif Fphone8=="2":
                    buy()
                else:
                    print("We didn't get any valid response")
                    buy()
            elif buy3=="2":
                Fphone10=input("IOS 11.1.1, 5.8 inch retina, 174gm, 1125 x 2436, 3GB RAM, 12 MP Camera 2160p quality, 2716mAh, 256 GB | Press 1 to add to cart | Press 2 to go back")
                if  Fphone10=="1":
                    Cart.append("Fphone 10")
                    print("Here is your cart",Cart)
                    buy()
                elif Fphone10=="2":
                     buy()
                else:
                    print("We didn't get any valid response")
                    buy()
            elif buy3=="3":
                Fphone10X=input("IOS 12, 5.8 inch retina, 177gm, 1125 x 2436, 4GB RAM, 12 MP Camera 2160p quality, 2658mAh, 256 GB | Press 1 to add to cart | Press 2 to go back")
                if  Fphone10X=="1":
                    Cart.append("Fphone 10X")
                    print("Here is your cart",Cart)
                    buy()
                elif Fphone10X=="2":
                     buy()
                else:
                    print("We didn't get any valid response")
                    buy()
            elif buy3=="4":
                Fphone10XMax=input("IOS 12, 6.5 inch retina, 208gm, 1242 x 2688, 4GB RAM, 12 MP Camera 2160p quality, 3174mAh, 512 GB | Press 1 to add to cart | Press 2 to go back")
                if  Fphone10XMax=="1":
                    Cart.append("Fphone 10X Max")
                    print("Here is your cart",Cart)
                    buy()
                elif Fphone10XMax=="2":
                      buy()
                else:
                    print("We didn't get any valid response")
                    buy()
            elif buy3=="5":
                buy()
            elif buy3=="6":
                displaymenu()
            elif buy3=="7":
                exit()
        elif buy2=="2":
            buy4=input("Fpad 6 | $499 Click 1 to see,      Fpad 7 | $799 Click 2 to see,      Fpad 8 | $999 Click 3 to see,     Fpad 8 Pro | $1099 Click 4 to see,     Click 5 to go back,     Click 6 to  log out,     Click 7 to exit:")
            if buy4=="1":
                Fpad6=input("IOS 8.1(Base), 9.7 inch retina, 437gm, 1536 x 2048, 2GB RAM, 8 MP Camera 1080p quality, 7340mAh, 64 GB | Press 1 to add to cart | Press 2 to go back")
                if  Fpad6=="1":
                    Cart.append("Fpad 6")
                    print("Here is your cart",Cart)
                    buy()
                elif Fpad6=="2":
                    buy()
                else:
                    print("We didn't get any valid response")
                    buy()
            elif buy4=="2":
                Fpad7=input("IOS 11.3, 9.7 inch retina, 469gm, 1536 x 2048, 2GB RAM, 8 MP Camera 1080p quality, 8827mAh, 128 GB | Press 1 to add to cart | Press 2 to go back")
                if  Fpad7=="1":
                    Cart.append("Fpad 7")
                    print("Here is your cart",Cart)
                    buy()
                elif Fpad7=="2":
                    buy()
                else:
                    print("We didn't get any valid response")
                    buy()
            elif buy4=="3":
                Fpad8=input("IOS 12(Base), 11 inch retina, 468gm, 1668 x 2388, 4GB RAM, 12 MP Camera 2160p quality, 7812mAh, 1 TB | Press 1 to add to cart | Press 2 to go back")
                if  Fpad8=="1":
                    Cart.append("Fpad 8")
                    print("Here is your cart",Cart)
                    buy()
                elif Fpad8=="2":
                    buy()
                else:
                    print("We didn't get any valid response")
                    buy()
            elif buy4=="4":
                Fpad8Pro=input("IOS 12(Base), 12.9 inch retina, 437gm, 1536 x 2048, 2GB RAM, 8 MP Camera 1080p quality, 7340mAh, 64 GB | Press 1 to add to cart | Press 2 to go back")
                if  Fpad8Pro=="1":
                    Cart.append("Fpad 8 Pro")
                    print("Here is your cart",Cart)
                    buy()
                elif Fpad8Pro=="2":
                    buy()
                else:
                    print("We didn't get any valid response")
                    buy()
            elif buy4=="5":
                buy()
            elif buy4=="6":
                displaymenu()
            elif buy4=="7":
                exit()
        elif buy2=="3":
            buy5=input("Macbook2| $1499 Click 1 to see, Macbook3 | $1999 Click 2 to see, Click 3 to go back, Click 4 to  log out, Click 5 to exit:")
            if  buy5=="1":
                Macbook2=input("  2.3GHz quad-core Intel Core i5-based 13-inch MacBook Pro systems with 8GB of RAM and 512GB SSD| Press 1 to add to cart | Press 2 to go back")
                if  Macbook2=="1":
                    Cart.append("Macbook2")
                    print("Here is your cart",Cart)
                    buy()
                elif Macbook2=="2":
                    buy()
                else:
                     print("We didn't get any valid response")
                     buy()
                    
            elif  buy5=="2":
                Macbook3=input("  2.6GHz quad-core Intel Core i7-based 15-inch MacBook Pro systems with 8GB of RAM and 1TB SSD| Press 1 to add to cart | Press 2 to go back")
                if  Macbook3=="1":
                    Cart.append("Macbook3")
                    print("Here is your cart",Cart)
                    buy()
                elif Macbook3=="2":
                    buy()
                else:
                    print("We didn't get any valid response")
                    buy()
            elif buy5=="3":
                 buy()
            elif buy5=="4":
                displaymenu()
            elif buy5=="5":
                exit()
        elif buy2=="4":
             buy6=input("Max Watch| $799 Click 1 to see, Max Watch Pro | $999 Click 2 to see, Click 3 to go back, Click 4to  log out, Click 5 to exit:")
             if buy6=="1":
                MaxWatch=input(" Dimensions 41.5 x 35.4 x 11.4 mm (1.67 x 1.43 x 0.45)Weight 52.4 g body (1.83 oz) Build Stainless Steel/Ceramic back SIM - 50m waterproof,Press 1 to add to cart | Press 2 to go back")
                if MaxWatch=="1":
                    Cart.append("Max Watch ")
                    print("Here is your cart",Cart)
                    buy()
                elif MaxWatch=="2":
                    buy()
                else:
                     print("We didn't get any valid response")
                     buy()
             elif buy6=="2":
                MaxWatchPro=input("Dimensions 43.5 x 37.4 x 11.4 mm (1.67 x 1.43 x 0.45 in) Weight 52.4 g body (1.83 oz)Build Stainless Steel/Ceramic back SIM No - 100m waterproofPress 1 to add to cart | Press 2 to go back")
                if MaxWatchPro=="1":
                    Cart.append("Max Watch Pro ")
                    print("Here is your cart",Cart)
                    buy()
                elif MaxWatchPro=="2":
                    buy()
                else:
                     print("We didn't get any valid response")
                     buy()
                if buy6=="3":
                   buy()
                elif buy6=="4":
                   displaymenu()
                elif buy6=="5":
                   exit()
        elif buy2=="7":
            displaymenu()
        elif buy2=="8":
            exit()
        elif buy2=="9":
            Rating=input("Enter your review or complain here:")
            print(Rate)
        elif buy2=="10":
            print("Lol")
        elif 
def displaymenu():
        status=input("log in or sign up? press y for log in/press n for sign up? Press q to quit")
        if status=="y":
                olduser()
        elif status=="n":
                newuser()
        elif status=="q":
                exit()
        else:
            print("We didn't recieve a valid response")
            print("Try again\n")
            displaymenu()
def newuser():
        createLogin=input("create login name:")
        if createLogin in users:
                print("\nLogin name already exists!\n")
        else:
                createpassword=input("create password:")
                users[createLogin]= createpassword
                print("\nUser created\n")
                olduser()
def olduser():
        login=input("enter login name:")
        password=input("enter password:")
        if login in users and users[login]==password:
                print("\nLogin successful!\n")
                buy()
        else:
                print("\nuser doesn't exist or wrong pasword!\n")
def price():
    
displaymenu()
