import time

name = input("Hello user." + " What shall I call you? ")
print("Welcome " + name + "!" + " Today we will write a program that tests Fast Thinking!")

integer = int(input("What is 2 + 2 ? "))

if integer == 4:
    answer = "Great!" + " Fast Thinking!"

else:
    answer = "False!."
    #print(answer)

print(answer)
time.sleep(2)

print("Now let's slow down and think thoroughly...")
time.sleep(3)

wholeNumber = int(input("What is 16 + 29 ? "))

if wholeNumber == 45:
    answer = "Correct!" + " That took some deliberate thinking."

else:
    answer = "Incorrect!" + " Slow down, think carefully."
    #print(answer)
    

"""if answer == "Incorrect!" + " Slow down, think carefully.":
    #print(answer)

else:
    print(answer)
time.sleep(2)"""

print(answer)
time.sleep(2)

print("System 1 is responsible for Fast Thinking" + " while System 2 is in charge of slow and deliberate thinking.")

