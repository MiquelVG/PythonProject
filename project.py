import os

print("You are a prisoner that has been held captive on a Spaceship for 6 months.\n Now it's your time to escape. A guard that you bribed will come at night time to open your cell.")
print("The guard came and opened your cell, where will you go?")
print("1-Go left")
print("2-Go right")
print("3-Go straight")
option = int(input())
while option < 1 and option > 3:
    print("Not valid option. Try again: ")
    option = int(input())
    
if option == 3:
    print("You arrive to the maintenance room. These are your options:")
    print("1-Check the old Spaceship map on the wall.")
    print("2-Grab a rusty pipe on the floor.")
    print("3-Go further on the maintenance room.")
    option = int(input())
    while option < 1 and option > 3:
        print("Not valid option. Try again: ")
        option = int(input())

    if option == 1:
        os.system("cls")
        print("After taking a look to the map you realise that there's an emergency escape ship room.")
        print("That could be your only chance.")
        print("1-Got to the escape pod room.")
        print("2-Not risk it and try to go to the parking station.")
        option = int(input())
        while option < 1 and option > 3:
            print("Not valid option. Try again: ")
            option = int(input())
        if option == 1:
            os.system("cls")
            print("As you approach the room you see two guards patroling the zone. There's only one escape ship left.")
            print("What will you do?")
            print("1-Make a run for it.")
            print("2-Distract the guards.")
            print("3-Wait for the guards to go.")
            option = int(input())
            while option < 1 and option > 3:
                print("Not valid option. Try again: ")
                option = int(input())
                if option == 1:
                    os.system("cls")
                    print("")
                    print("You run as fast as you can towards the escape ship but the guards catch you before you could have entered it.")
                    print("---THE END---")
                if option == 2:
                    os.system("cls")
                    print("You grab a tool you had nearby and throw it, the guards go to check the sound.")
                    print("You did it! You got into the escape ship and returned home")
                    print("---THE END---")
                else:
                    os.system("cls")
                    print("You wait for the guards to leave.")
                    print("After some time you fall asleep and get caught.")
                    print("---THE END---")
        else:
            os.system("cls")
            print("You cautiously get to the parking station where you fin a lot of parked small Spaceships.")
            print("You see a set of keys and decide to take them.")
            print("1-Try to steal a Spaceship from the principal door.")
            print("2-Try to steal a Spaceship from the back door.")
            print("3-Try to force open a Spaceship.")
            option = int(input())
            while option < 1 and option > 3:
                print("Not valid option. Try again: ")
                option = int(input())
            if option == 1:
                os.system("cls")
                print("The keys weren't for the principal door and you set off the alarm. The guards caught you.")
                print("---The End---")
            elif option == 2:
                os.system("cls")
                print("You manage to open the back door of the Spaceship.")
                print("Once you start it you finally get out.")
                print("---The End---")
            elif option == 3:
                os.system("cls")
                print("You try to force open a Spaceship and it sets off the alarm.")
                print("You get caught.")
                print("---The End---")