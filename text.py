import time
import random
import sys

def mainmenu():
    print('''
 a88888b. dP     dP   888888ba  dP .d88888b  d888888P 8888ba.88ba   .d888888  .d88888b      a88888b. dP     dP   .d888888   .88888.  .d88888b  
d8'   `88 88     88   88    `8b 88 88.    "'    88    88  `8b  `8b d8'    88  88.    "'    d8'   `88 88     88  d8'    88  d8'   `8b 88.    "' 
88        88aaaaa88a a88aaaa8P' 88 `Y88888b.    88    88   88   88 88aaaaa88a `Y88888b.    88        88aaaaa88a 88aaaaa88a 88     88 `Y88888b. 
88        88     88   88   `8b. 88       `8b    88    88   88   88 88     88        `8b    88        88     88  88     88  88     88       `8b 
Y8.   .88 88     88   88     88 88 d8'   .8P    88    88   88   88 88     88  d8'   .8P    Y8.   .88 88     88  88     88  Y8.   .8P d8'   .8P 
 Y88888P' dP     dP   dP     dP dP  Y88888P     dP    dP   dP   dP 88     88   Y88888P      Y88888P' dP     dP  88     88   `8888P'   Y88888P  
ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo                                                                                                                                                                                                                                              
''')

def choice1():
    print('''Here are your options:
1) Climb down the chute
2) Remake the present
3) Ignore it''')

def youlost():
    print('''
dP    dP  .88888.  dP     dP    dP         .88888.  .d88888b  d888888P 
Y8.  .8P d8'   `8b 88     88    88        d8'   `8b 88.    "'    88    
 Y8aa8P  88     88 88     88    88        88     88 `Y88888b.    88    
   88    88     88 88     88    88        88     88       `8b    88    
   88    Y8.   .8P Y8.   .8P    88        Y8.   .8P d8'   .8P    88    
   dP     `8888P'  `Y88888P'    88888888P  `8888P'   Y88888P     dP    
ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo                                                                       
''')

def choice2():
    print('''Choose the present that you think is the correct present.
1) Present 1
2) Present 2
3) Present 3''')

def choice3():
    print('''Here are your options:
1) Climb back up the chute
2) Run around the incinerator
3) Sit there and relax''')

def choice4():
    print('''Here are your options:
1) Try and jump onto the sleigh
2) Throw the present onto the sleigh''')

def youwon():
    print('''
dP    dP  .88888.  dP     dP    dP   dP   dP  .88888.  888888ba  dP 
Y8.  .8P d8'   `8b 88     88    88   88   88 d8'   `8b 88    `8b 88 
 Y8aa8P  88     88 88     88    88  .8P  .8P 88     88 88     88 88 
   88    88     88 88     88    88  d8'  d8' 88     88 88     88 dP 
   88    Y8.   .8P Y8.   .8P    88.d8P8.d8P  Y8.   .8P 88     88    
   dP     `8888P'  `Y88888P'    8888' Y88'    `8888P'  dP     dP oo 
oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo                                                                    
''')