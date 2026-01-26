"""
Fit'N'Fun is a fitness app that helps you plan and organize weekly workouts and goes ahead to suggest healthy snacks when prompted
"""


# ------ Function to auo-populate workout plan ------

from time import sleep

from random import choice

def chooseWorkout(weeks):
    
    while len(workoutPlan) < int(weeks):
        chosenWorkout = choice(favoriteWorkouts)
        if chosenWorkout not in workoutPlan:
            workoutPlan.append(chosenWorkout)
    print()

    print("Perfect!. Here you go...")

    print()

    for workouts in workoutPlan:
        print (workouts)
    

def shoppingLists():

    if "Sit-ups" in workoutPlan:
        healthysnacks.append("Greek Yoghurt")
        
    if "Push-ups" in workoutPlan:
        healthysnacks.append("Protein Bars")

    if "Squats" in workoutPlan:
        healthysnacks.append("Chickpeas")

    if "Planks" in workoutPlan:
        healthysnacks.append("Almond nuts")

    if "Jogging" in workoutPlan:
        healthysnacks.append("Blueberries")

    if "Pull-ups" in workoutPlan:
        healthysnacks.append("Fish pies")

    if "Burpees" in workoutPlan:
        healthysnacks.append("Cereal")

    print()

    print("Done! Here are some healthy snacks that can aid your workouts ;)")
    print()
    for item in healthysnacks:
        print(item)
    sleep(2)
    print()
    print("Enjoy your workouts and have a superb week!")

def endProgram():

    print("Fair Enough!. Enjoy your workouts and have a great week!")
        

# ------- Lists of hardcoded favorite workouts ------

favoriteWorkouts = ["Sit-ups", "Push-ups", "Squats", "Planks", "Jogging", "Pull-ups", "Burpees"]

# ------ Lists of healthy snacks ------

healthySnacks = ["Greek Yoghurt", "Protein Bars", "Chickpeas", "Almond nuts", "Blueberries", "Fish pies", "Cereal"]

# ------ Auto-populated List of workoutPlan/Schedules/healthySnacks ------

workoutPlan = []
healthysnacks = []

# ------ Function to auto-populate healthy snacks when required ------



# ------ Introduction ------

name = input("Hello there! What's your name? ")
print("Hi " + name + "!" + " Welcome to Fit'N'Fun, your powerful assistant that helps you plan your weekly workout(s). I even go further to suggest healthy snacks to aid your fitness if needed ;)")
print()

sleep(2)
# ------ How many weeks does the User want to plan for ? ------

answer = input("Great!" + " Now you know what I can do, how many weeks shall I plan for? min:1, max:4 ")

chooseWorkout(answer)

sleep(2)
print()

answer = int(input("Would you like me to suggest some healthy snacks to aid your workout?. Enter '1' for 'Yes' or '2' for 'No' "))

if answer == 1:

    shoppingLists()

else:
    print()
    endProgram()
    


