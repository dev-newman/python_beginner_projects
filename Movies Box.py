"""
Movie Box is a virtual assistant that helps the user plan a watchlist of movies and suggests snack options to go with, if required
"""


# ------Functions ------
from time import sleep
from random import choice

def chooseMovies(days):
    while len(moviesToWatch) < int(days):
        chosenMovies = choice(favoriteMovies)
        if chosenMovies not in moviesToWatch:
            moviesToWatch.append(chosenMovies)

    print("Here you go...")
    print()
    for item in moviesToWatch:
        print(item)



def chooseSnack():

    if "Lord of the Rings" in moviesToWatch:
        snackMenu.append("Popcorn")

    if "Transformers: Age of Ultron" in moviesToWatch:
        snackMenu.append("Nachos")

    if "Bumble Bee" in moviesToWatch:
        snackMenu.append("Cheetos")

    if "Avengers: Doomsday" in moviesToWatch:
        snackMenu.append("Tacos")

    if "The Lion King" in moviesToWatch:
        snackMenu.append("Cheeseballs")

    if "Interstellar" in moviesToWatch:
        snackMenu.append("Almond Nuts")

    print("There you go...")
    print()
    for item in snackMenu:
        print(item)
    print()
    print("Enjoy your movies and have fun!")

def endProgram():
    print("Fair Enough. Enjoy your movies and have a great week!")


    
# ------ Lists ------
favoriteMovies = ["Lord of the Rings", "Transformers: Age of Ultron", "Bumble Bee", "Avengers: Doomsday", "The Lion King", "Interstellar"]
moviesToWatch = []
snacksList = ["Popcorn", "Nachos", "Cheetos", "Tacos", "Cheeseballs", "Almond Nuts"]
snackMenu = []


# ------ Introduction ------

name = input("Hello there! What's your name? ")
print()
print("Welcome to Movie Box, " + name + "!" + " I am your virtual assistant and I can help you plan your movies for the weekend. I could also suggest some Snacks to go with, if needed.")
sleep(2)
print()
answer = input("How many movies would you like to watch this weekend? min:1, max:6 ")
print()
chooseMovies(answer)

print()

answer = int(input("Do you want Snack suggestions to go with? Enter '1' for 'Yes' or '2' for 'No' "))
print()
if answer == 1:
    chooseSnack()

else:
    endProgram()


