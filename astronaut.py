#!/usr/bin/env python3

import time
from led_manager import Led_Manager
from colors import *


def parse_text(text):
    # Keep going if no command is entered
    if(len(text) == 0):
        return False, False    
    
    # Set the command and color text if valid
    command = text[0].lower()    
    if(len(text) == 1):
        color = False
    elif(len(text) == 2):
        color = parse_color(text[1].lower())

    return command, color


def parse_color(text):
    color = False
    if(text == "blue"):
        color = B
    elif(text == "red"):
        color = R
    elif(text == "green"):
        color = G
    elif(text == "yellow"):
        color = Y
    elif(text == "maroon"):
        color = M
    return color    


def help():
    print(
        """
        Commands: 
            exit - leaves the program
            help - prints this help text
            
            blinking_eyes(color) - creates blinking eyes animates
            heart_eyes(color) - creates hearts for eyes that swell
            angry_eyes(color) - shows open eyes that become angry/frustrated
            excited_eyes(color) - show excited eyes that close with excitement
            
            *(color) tag indicates that colors can be passed in and changed
        
        Colors: List of supported colors
            white
            blue
            red
            green
            yellow
            maroon
        """
    )


def main():    
    led_manager = Led_Manager()
    
    exit = False

    while(exit != True):
        text = raw_input("#>").split()
        
        command, color = parse_text(text)
        # No command was typed so keep displaying prompt
        if(command == False):
            continue
            
        # Figure out what command was sent from cli
        if(command == "exit"):
            exit = True
        elif(command == "help"):
            help()
        elif(command == "blinking_eyes"):
            if(color == False):
                led_manager.blinking_eyes()
            else:
                led_manager.blinking_eyes(color)
        elif(command == "heart_eyes"):
            if(color == False):
                led_manager.heart_eyes()
            else:
                led_manager.heart_eyes(color)
        elif(command == "angry_eyes"):
            if(color == False):
                led_manager.angry_eyes()
            else:
                led_manager.angry_eyes(color)  
        elif(command == "excited_eyes"):
            if(color == False):
                led_manager.excited_eyes()
            else:
                led_manager.excited_eyes(color)             
        else:
            print("Not valid command.")
            

if __name__ == '__main__':
    main()
    
    
    
