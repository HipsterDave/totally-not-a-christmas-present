import functions
import text
import sys
import time
import random
import os

typingspeed = 100

def clear():
	os.system("cls")

def typing(text):
	for letter in text:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(random.random()*10/typingspeed)

def settype(text, typing_speed):
	for letter in text:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(random.random()*10/typing_speed)

def playgame():
    typing("It is Christmas Eve, and you are an elf.\n")
    typing("This year, you get to make the LAST PRESENT.\n")
    typing("Santa's sleigh is about to take off! Just then, you finished making the LAST PRESENT.\n")
    typing("You run towards the sleigh with the LAST PRESENT.\n")
    typing("But then...\n")
    typing("You trip and drop the present into a random present chute.\n")
    typing("What is a present chute? A present chute is where the elves put the presents to do different things. It can range from wrapping to incinerating.\n")
    typing("The LAST PRESENT fell in the incinerating chute. :(\n")
    typing("Well... You need to retrive it!\n")
    text.choice1()
    choice1 = ""
    while choice1 not in ["1", "2", "3"]:
        choice1 = input("> ")
    if choice1 == "1":
        clear()
        typing("You attempt to climb down the chute.\n")
        typing("As you climb down, you see the present!\n")
        typing("All of the presents are on a conveyer belt.\n")
        typing("The only problem is... there are 2 other presents that look exactly like the LAST PRESENT!\n")
        text.choice2()
        choice2 = ""
        present_list = ["1", "2", "3"]
        randompresent = random.choice(present_list)
        while choice2 not in ["1", "2", "3"]:
            choice2 = input("> ")
        if choice2 == randompresent:
            clear()
            typing("Hooray! You found the correct present!\n")
            typing("YOU OBTAINED THE LAST PRESENT!\n")
            typing("Now... How do we get back up on the top floor?\n")
            text.choice3()
            choice3 = ""
            while choice3 not in ["1", "2", "3"]:
                choice3 = input("> ")
            if choice3 == "1":
                clear()
                typing("You attempt to climb back up the chute.\n")
                typing("Hmm... The chute is too slippery to climb up...\n")
                typing("As you try to climb up the chute, Santa leaves.\n")
                text.youlost()
                functions.mainmenu_teleport()
            elif choice3 == "2":
                clear()
                typing("You attempt to run around the incinerator.\n")
                typing("As you look around the back, you find a door!\n")
                typing("You walk through the door, and you find a staircase.\n")
                typing("As you are walking up the staircase, you come across a security guard.\n")
                typing("Security Guard - HEY! YOU'RE NOT SUPPOSED TO BE HERE!!!\n")
                typing("You tell the guard what happened.\n")
                typing("Security Guard - I see what happened. You'd better run! Santa is about to leave!\n")
                typing("As you run towards the sleigh, it starts to lift off.\n")
                text.choice4()
                choice4 = ""
                while choice4 not in ["1", "2"]:
                    choice4 = input("> ")
                if choice4 == "1":
                    clear()
                    typing("You attempt to jump into the sleigh.\n")
                    sleigh_jump_choices = ["make", "no make"]
                    sleigh_jump = random.choice(sleigh_jump_choices)
                    if sleigh_jump == "make":
                        typing("You made it onto the sleigh!\n")
                        typing("Yay! You deliver the present successfully!\n")
                        text.youwon()
                        typing("Merry Christmas!\n")
                        functions.mainmenu_teleport()
                    elif sleigh_jump == "no make":
                        typing("Sadly, you do not make it onto the sleigh...\n")
                        text.youlost()
                        functions.mainmenu_teleport()
                elif choice4 == "2":
                    clear()
                    typing("You attempt to throw the present on the sleigh.\n")
                    throw_choices = ["make", "no make"]
                    throw = random.choice(throw_choices)
                    if throw == "make":
                        typing("You made it onto the sleigh!\n")
                        typing("Yay! You deliver the present successfully!\n")
                        text.youwon()
                        typing("Merry Christmas!\n")
                        functions.mainmenu_teleport()
                    elif throw == "no make":
                        typing("Sadly, you miss the sleigh...\n")
                        text.youlost()
                        functions.mainmenu_teleport()
            elif choice3 == "3":
                clear()
                typing("You sit there and relax.\n")
                typing("Seriously... Why would you do that??!!?!?!\n")
                text.youlost()
                functions.mainmenu_teleport()
        else:
            clear()
            typing("Sigh... You picked up the wrong present. When you realize this, the LAST PRESENT already fell into the incinerator.")
            text.youlost()
            functions.mainmenu_teleport()
    elif choice1 == "2":
        clear()
        typing("You attempt to rebuild the present.\n")
        typing("You try your hardest, but it takes too long.\n")
        text.youlost()
        functions.mainmenu_teleport()
    elif choice1 == "3":
        clear()
        typing("You ignore it.\n")
        typing("How could you ignore it? IT IS THE LAST PRESENT!!!!!!!!!!\n")
        text.youlost()
        functions.mainmenu_teleport()