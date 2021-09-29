# this is Sukky Yan Week 3 Homework

# NEW YORK: BECOME HUMAN

# This is a story about you,a household CR-400 bionic robot lived in 2045. Today is your first day working for your master- Danniel and her cute daughter Alice.
# Remember, making cautious decision. What you choose matters everyone's destiny.
# Good luck.


import random # random numbers (https://docs.python.org/3.3/library/random.html)
import sys # system stuff for exiting (https://docs.python.org/3/library/sys.html)

# an object describing our player
player = { 
    "name": "p1", 
    "humanity": 0,
    "items" : ["milk"],
    "tasks" : [],
    "location" : "start"
}

rooms = {
    "room1" : "housekeeping",
    "room2" : "doing laundry",
    "room3" : "cooking"
}

def rollDice(minNum, maxNum, difficulty):
    # any time a chance of something might happen, let's roll a die
    result = random.randint(minNum,maxNum)
    print ("You roll a: " + str(result) + " out of " + str(maxNum))

    if (result <= difficulty):
        print ("trying again....")
        
        input("press enter >")
        rollDice(minNum, maxNum, difficulty) # this is a recursive call

    return result

def printGraphic(name):
    if (name == "gun"):
        print ('  +--^----------,--------,-----,--------^-,  ')
        print ('  ||||||||   `--------'                     '')
        print ('   `+---------------------------^----------  ')
        print ('    `\_,---------,---------,--------------   ')
        print ('      / XXXXXX /'        '                   ')
        print ('     / XXXXXX /  `\    /                     ')
        print ('    / XXXXXX /`-------'                       )
        print ('   / XXXXXX /                                ')
        print ('  / XXXXXX /_/                               ')
        print (' (________(                                  ')
        print ('                the gun                      ')

    if (name == "pasta"):
        print ('        |        ')
        print ('        |  /     ')
        print ('        | /      ')
        print ('   .~^(,&|/o.    ')
        print ('  |`-------^|    ')
        print ('  \         /    ')
        print ('   `=======      ')
        print ('   the pasta     ')

    if (name == "robot"):
        print ('       _______          ')
        print ('     _/       \_        ')
        print ('    / |       | \       ')
        print ('   /  |__   __|  \      ')
        print ('  |__/((o| |o))\__|     ')
        print ('  |      | |      |     ')
        print ('  |\     |_|     /|     ')
        print ('  | \           / |     ')
        print ('   \| /  ___  \ |/      ')
        print ('    \ | / _ \ | /       ')
        print ('     \_________/        ')
        print ('     _|_____|_          ')
        print ('  ___|_________|___     ')
        print ('  you are a bio-robot   ') # this one is escaped!

    if (name == "alice"):
        print ('        .===.          ')
        print ('       / ,,, \         ')
        print ('      ( /6.6\ )        ')
        print ('      )(  _  )(        ')
        print ('      ( ,' ', )        ')
        print ('      / (\-/) \        ')
        print ('     /_ /o o\ _\       ')
        print ('     | _\ Y /_ |       ')
        print ('     \(_ `~` _)/       ')
        print ('      / /   \ \        ')
        print ('     / ()/^\() \       ')
        print ('    /. . . . . .\      ')
        print ('     `"`"|`|`|"`"`     ')
        print ('          |_|_|        ')
        print ('         _|_|_|_       ')
        print ('        (___|___)      ')
        print ('  Alice talks to you   ')
      

    if (name == "skull"):
        print ('          ______                ')
        print ('       .-"      "-.             ')
        print ('      /            \            ')
        print ('     |              |           ')
        print ('     |,  .-.  .-.  ,|.          ')
        print ('     | )(__/  \__)( |.          ')
        print ('     |/     /\     \|.          ')
        print ('     (_     ^^     _).          ')
        print ('      \__|IIIIII|__/.           ')
        print ('       | \IIIIII/ |             ')
        print ('       \          /             ')
        print ('        `--------`              ')
        print ('          Death                 ')

    if (name == "title"):
        print ('-----------------------------------------------------------------------------')
        print ('  _____ _____ _ _ _    __ __ _____ _____ _____    _                          ')
        print (' |   | |   __| | | |  |  |  |     | __  |  |  |  |_|                          ')
        print (' | | | |   __| | | |  |_   _|  |  |    -|    -|   _                           ')
        print (' |_|___|_____|_____|    |_| |_____|__|__|__|__|  |_|                          ')
        print ('                                                                             ')
        print ('  _____ _____ _____ _____ _____    _____ _____ _____ _____ _____               ')
        print (' | __  |   __|     |   | |   __|  |  |  |  |  |     |  _  |   | |             ')
        print (' | __ -|   __|-   -| | | |  |  |  |     |  |  | | | |     | | | |             ')
        print (' |_____|_____|_____|_|___|_____|  |__|__|_____|_|_|_|__|__|_|___|             ')
        print ('                                                                             ')
        print ('-----------------------------------------------------------------------------')




def gameOver2():
    printGraphic("skull")
    print("-------------------------------")
    print("Why this happens...")
    print("Danniel falls down into the pool of blood")
    print("Alice screams and cries, looking at you desperately" )
    print("You don't know why you do this.... ")
    print("name: " + player["name"] ) # customized with a name
    print( "humanity: " + str(player["humanity"]) ) # customized with a score
    return

def gameOver1():

    printGraphic("skull")

    print("-------------------------------")
    print("BAD ENDING...")
    print("You are beaten to death by Danniel....")
    print("In fact, this is not your first day in Danniel's house." )
    print("You used to be a household CR-400 bionic robot of this violent man before. ")
    print("The little girl Alice really really loves you. You are like her mom, her friend.")
    print("However, Danniel beated you to death one day.")
    print("You were send back to the factory and memory reseted... ")
    print("name: " + player["name"] ) # customized with a name
    print( "humanity: " + str(player["humanity"]) ) # customized with a score
    return

def toBeContinued():

    printGraphic("alice")

    print("-------------------------------")
    print("story is going on...")
    print("You escape from the house sucessfully with Alice.")
    print("She finally talks to you:'Are you OK?' She touches your scars." )
    print("You holds her little hand with a sile and say nothing. ")
    print("The New York is drizzling, the police sirens are ringing.")
    print("What will you and Alice to do in the next step?....")
    print("To be continued... ")
    print("name: " + player["name"] ) # customized with a name
    print( "humanity: " + str(player["humanity"]) ) # customized with a score
    return


def cooking():
    print("It's dinner time. You cook some pasta.")
    printGraphic("pasta")
    input("press enter >")
 
    print("-------------------------------")
    print("While they eating, Danniel suddenly started to complain about his leaving wife and lost job. ")
    print("Danniel yells to Alice:'You think I'm useless, right? You hate me? Are you gaonna leave me like your mom? '")
    print("As Danniel yelling louder and louder, he raises his hand, gonna to beat her daughter Alice！")
    input("press enter >")

   # check the list for items
    # the 'in' keyword helps us do this easily
    if ("gun" in player["items"]):
        print ("options: [ protect Alice, pull out the gun, ignore]")
    else:
        print ("options: [ protect Alice, ignore ]")

    pcmd = input(">")

    if (pcmd == "protect Alice"): 
        print("-------------------------------")
        print ("You hug Alice and resist Danniel’s attack with your body")
        print ("Danniel is irrated, he raises the baseball bat to hit you！")
        print ("Let's roll a dice to see what happens to you!")
        player["humanity"] += 20

        pcmd = input(">") # user input

        # roll a dice from 0 to 20 to see what happens
        # if your number is higher than the difficulty, you win!
        difficulty = 7
        roll = rollDice(0, 20, difficulty)
        
        # you have to get lucky! this only happens to the player
        # if you roll the dice high enough
        if (roll >= difficulty):
            print ("You are so lucky! Danniel stops in Alice’s crying...")

            pcmd = input(">") # user input

            print ("Do you wanna escape from home with Alice?")
            
            printGraphic("robt")

            # we dive further into the logic
            pcmd = input("yes or no >")

            if (pcmd == "no"):
                print ("You go bcak to work with scars.")
                housekeeping()

            elif (pcmd == "yes"):
                print ("When Danniel was not paying attention, you escapes from the house with Alice!")
                player["humanity"] += 60 # add to the score
                toBeContinued()

           
    

    elif (pcmd == "ignore"):
        print ("You pretend not to see it and go back to work")
        print ("Alice is crying on the background...") # bad choice reference
        cooking()
        player["humanity"] -= 40

    elif (pcmd == "pull out the gun"):
         print ("You pull out the gun and shoot to the crazy drunk Danniel")
         player["humanity"] += 80 # add to the score
         gameOver1()
        





def findGun():
    print ("You throw dirty clothes in the washing machine.")
    print ("Suddenly, you find a gun in it!")
    input("press enter >")

    printGraphic("gun")
    print ("-------------------------------")
    print ("You scanned the gun with your eyes")
    print ("Type: Italy Beretta 92F pistol.")
    print ("It seems familiar to you.....")
    input("press enter >")
    player["humanity"] += 20
    
    print ("You consider your options.")


    if (("gun" in player["items"]) and ("cooking" in player["tasks"])):
        print ("Your options: [ company Alice, shoot Danniel, exit]")

    elif ("gun" in player["items"]):
        print ("Your options: [ company Alice, cooking, exit ]")

    else:
        print ("Your options: [ put the gun back, hide in the pocket ]")

    pcmd = input(">") # user input


    # option 1: put the gun back
    if (pcmd == "put the gun back"):
        print ("You put it back...")
        housekeeping() # try again
    
    # option 2: hide in the pocket
    elif (pcmd == "hide in the pocket"):
        print ("-------------------------------")
        print ("You put the gun in your pocket quietly.")
        player["items"].append("gun") # add an item to the array with append
        player["humanity"] += 50 # add to the score
        
        print ("However, Danniel catches you are hiding something!")
        print ("Let's roll a dice to see if Danniel find your gun!")
        input("press enter to roll >")

        difficulty = 5
        chanceRoll = rollDice(0,20,difficulty) # roll a dice between 0 and 20

        # if the roll is higher than 5... 75% chance
        if (chanceRoll >= difficulty):
            print ("Fortunetly! Danniel didn't find your gun and walked away angrily.")
            pcmd = input(">")
            housekeeping() # option again
            player["humanity"] += 50
        else:
            print ("Damn! Danneil found your gun！")
            gameOver1() # bad ending1
        
      

def housekeeping():
    print ("-------------------------------")
    print ("You start to do housekeeping. ")
    print ("There are a list of tasks you need to do.")
    
    # this piece of game logic checks to see if the requirements are met to continue.
    # we can have some fun and change the options for the player
    # based on variables we stored

    # 1. check the list of items, to see if it is there
    # 2. check the list of tasks, to see if you are in tasks list

    if (("gun" in player["items"]) and ("cooking" in player["tasks"])):
        print ("Your options: [ company Alice, shoot Danniel, cooking, exit]")

    elif ("gun" in player["items"]):
        print ("Your options: [ company Alice, cooking, exit ]")

    else:
        print ("Your options: [ company Alice, doing laundry , cooking , exit ]")

    pcmd = input(">") # user input

    # player options1
    if (pcmd == "company Alice"):
        # its a trick!
        print ("You want to play with Alice, but she walks away....")
        player["humanity"] += 10

        input("press enter >")
        housekeeping()

    # play option2
    elif (pcmd == "doing laundry"):
        print ("You walk into the laundry room.")
        input("press enter >")
        findGun() # path 1

    # path2 option
    elif (pcmd == "cooking"):
        print ("You walk into the kitchen.")
        input("press enter >")
        cooking() # path 2

    # exiting / catching errors and crazy inputs
    elif (pcmd == "quit"):
        print ("you quit.")
        return # exit the application
        
    elif (pcmd == "shoot Danniel"):
        print ("With a gunshot, Danniel fell in a pool of blood, and Alice burst into tear...")
        printGraphic("skull")

        print ("why this happens...") # escaped
        return # exit the application, secret ending

    else:
        print ("I don't understand that")
        housekeeping() # the beginning

def introStory():
    # let's introduce them to our world
    print ("Good to see you gain! What should I call you?")
    player["name"] = input("Please enter your name >")

    # intro story, quick and dirty (think star wars style)
    print("-------------------------------")
    print ("Welcome to the New York: Being Human " + player["name"] + "!")
    print ("The story so far...")
    print ("09-29-2045, you are a household CR-400 bionic robot.")
    print ("Your employer is a nasty middle-aged man --- Danniel.")
    print ("Your job is to do the house cleaning, and to take care of his taciturn 8-year-old daughter --- Alice.")
    print ("Today is your first day for job, but you feel that everything is familiar...")
    print ("Are you ready to start your BEING HUMAN adventuring?")

    pcmd = input("please choose yes or no >")

    # the player can choose yes or no
    if (pcmd == "yes"):
        print ("Your decision would affect everyone's destiny. Take care")
        pcmd = input("press enter >")

        print("-------------------------------")
        print ("It's a normal morning, Danniel sits on the sofa smoking, drinking and watching TV.")
        print ("Alice is playing with her teddy bear on the floor of the living room.")
        print ("Her eyes are a little dodge when she looks at you.")
        input ("press enter >")
        housekeeping()
    else:
        print ("No? ... That doesn't work here.")
        pcmd = input("press enter >")
        introStory() # repeat over and over until the player chooses yes!



# main! most programs start with this.
def main():
    printGraphic("title") # call the function to print an image
    introStory() # start the intro

main() # this is the first thing that happens