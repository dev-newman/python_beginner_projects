#Thinking_Fast_Part_2

import time

name = input("What's your name? ")

print("Hello " + name + "!" + " Today we will be practising exercises that involve System 1 and 2." + " Get ready...")

number = int(input("What is the answer to 2 + 2 ? "))

if number == 4:
    print("Correct!")

else:
    number = 4
    print(number)

time.sleep(2)

color = input("What color comes to mind when I mention the word Banana? ")

if color == "Yellow":
    print("Perfect!")

else:
    color = "Yellow"
    print(color)

system1_Thoughts = []

system1_Thoughts.extend([4, "Yellow"])


time.sleep(2)

print("Now think carefully...")


time.sleep(2)

product = int(input("What is the product of 15 * 15 ? "))

if product == 225:
    print("Correct again!")

else:
    product = "False!" + " Think thoroughly."
    print(product)

time.sleep(2)

answer = input("What would be your reaction if a Stranger walked up to you, and handed you 5 dollar bills ? ")

system2_Thoughts = []

system2_Thoughts.extend([225, "Surprised"])

print(system1_Thoughts)

print(system2_Thoughts)

#print("Your System1_Thoughts conatined: " + system1_Thoughts + ", while your System2_Thoughts contained: " + system2_Thoughts)

print("System1_Thoughts had a length of: " + str(len(system1_Thoughts)) + ", while System2_Thoughts had a length of: " + str(len(system2_Thoughts)))



    
