import os

print("You are a prisoner that has been held captive on a Spaceship for 6 months.\n Now it's your time to escape. A guard that you bribed will come at night time to open your cell.")
print("The guard came and opened your cell, where will you go?")
print("1-Go left")
print("2-Go right")
print("3-Go straight")
option = int(input())
if option < 1 and option > 3:
    while option < 1 and option > 3:
        print("Not valid option. Try again: ")
        option = int(input())
    if option == 3:
        print("You arrive to the maintenance room. These are your options:")
        print("1-Go to the Observatory on the next room.")
        print("2-Grab a rusty pipe on the floor.")
        print("3-Go further on the maintenance room.")
        option = int(input())