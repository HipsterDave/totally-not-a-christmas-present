import random
import os
import time
import text
import game
import sys

typingspeed = 100

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

def clear():
	os.system("cls")

def mainmenu():
	clear()
	text.mainmenu()
	typing("Would you like to PLAY, or QUIT?\n")
	ooh = ""
	while ooh not in ["play", "quit"]:
		ooh = input("> ")
	if ooh == "play":
		clear()
		game.playgame()
	elif ooh == "quit":
		clear()
		typing("Goodbye!")

def mainmenu_teleport():
	typing("Please press enter to continue.\n")
	input("> ")
	mainmenu()