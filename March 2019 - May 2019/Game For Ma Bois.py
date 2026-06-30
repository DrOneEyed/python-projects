import random
n=random.randrange(0,100)
Check="wrong"
print("Welcome to Number Guess")
print("There is a surprise at the end for you boi. ")

while Check=="wrong":
    v=int(input("Enter A Number Between 0 and 100: "))
    if v<n:
        print("This is lower than actual number. ")
        print("Galat MC")
        print("Jitni bar galat karega utne Mukke khae ga tu")
    elif v>n:
        print("This is higher than actual number. ")
        print("Galat MC")
        print("Jitni bar galat karega utne Mukke khae ga tu")
    else:
        print("Just tell me u didn't get in first try.")
        Check="correct"

print("Thank you for playing Number Guess. \nSee you tommo boi")
print("Now Enjoy the prize: ")
print("Loading......")
import time
time.sleep(2)
import urllib as url
import webbrowser as web
import requests
w= url.request.urlopen("https://www.marvel.com/articles/movies/check-out-the-latest-marvel-studios-avengers-infinity-war-posters")
u=w.geturl()
web.open_new(u)
print("Well Now Go And Check Te Code Bete")
