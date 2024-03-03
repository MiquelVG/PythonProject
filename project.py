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
    if option == 1:
        print("You arrive at the door leading to the room where the escape pods are located, but the electronic door is closed.")
        print("What do you do?")
        print("1-Try to hack the door from the control panel next to it.")
        print("2-Wait for someone to open the door.")
        print("3-Go in another direction.")
        option = int(input())
        if option < 1 and option > 3:
            while option < 1 and option > 3:
                print("Not valid option. Try again: ")
                option = int(input())
                if option == 1:
                    os.system("cls")
                    print("You fail to hack the panel and an alarm sounds.")
                    print("What do you do?")
                    print("1-Persist and try to hack the panel before the guards arrive.")
                    print("2-Hide in a hiding spot.")
                    print("3-Run away.")
                    option = int(input())
                    if option < 1 and option > 3:
                        while option < 1 and option > 3:
                            print("Not valid option. Try again: ")
                            option = int(input())
                        if option == 1:
                            os.system("cls")
                            print("You manage to open the door just as the guards arrive, and they are armed!")
                            print("You must choose quickly, which escape pod do you pick?")
                            print("1-The first.")
                            print("2-The second.")
                            print("3-The third.")
                            option = int(input())
                            if option < 1 and option > 3:
                                while option < 1 and option > 3:
                                    print("Not valid option. Try again: ")
                                    option = int(input())
                                if option == 1:
                                    os.system("cls")
                                    print("You went as fast as you could, but you didn't realize that the escape pod was under repair.")
                                    print("As a result, the escape pod doesn't start, and the guards capture you.")
                                    print("-------------")
                                    print("--GAME OVER--")
                                    print("--YOU  LOSE--")
                                    print("-------------")
                                elif option == 2:
                                    os.system("cls")
                                    print("You were fast enough and realized that the first escape pod was under repair.")
                                    print("The second escape pod starts, and you manage to escape.")
                                    print("-------------")
                                    print("--GAME OVER--")
                                    print("--YOU  WIN--")
                                    print("-------------")
                                elif option == 3:
                                    os.system("cls")
                                    print("You weren't fast enough, the third capsule was too far away.")
                                    print("One of the guards' shots hits you, and they manage to capture you.")
                                    print("-------------")
                                    print("--GAME OVER--")
                                    print("--YOU  LOSE--")
                                    print("-------------")


                                     