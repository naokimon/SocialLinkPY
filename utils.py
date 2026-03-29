import sys, time, os
from data.ascii import ascii
from data.locations import location
from data.dialogue import commandlist
import json
from config import SAVE_PATH
import textwrap

def sprint(text, delay=0.005, width=100):
    wrapped = textwrap.fill(text, width)
    for char in wrapped:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def charprint(character, dialogue, pause=True):
    cls()
    print(ascii[character])
    sprint(dialogue, delay=0.05)
    if pause:
        input()

def npcprint(npc, dialogue, pause=True):
    cls()
    print(f"{npc}:")
    sprint(dialogue, delay=0.05)
    if pause:
        input()

def playerprint(prevcharacter, dialogue, pause=True):
    cls()
    print(ascii[prevcharacter])
    sprint(dialogue, delay=0.05)
    if pause:
        input()

def idprint(dialogue, pause=True):
    cls()
    sprint(dialogue, delay=0.05)
    if pause:
        input()

def ask_confirmed_input(prompt, max_len=8):
    while True:
        value = input(prompt)
        if len(value) > max_len:
            sprint(f"Character limit is {max_len}.")
            continue
        while True:
            sprint("Are you sure? Y/N")
            yn = input().lower().strip()
            if yn in ["y", "yes"]:
                return value
            elif yn in ["n", "no"]:
                break
            else:
                sprint("Invalid option.")

def show_location(shownlocation):
    return location[shownlocation]["name"]

def show_description(showdescription):
    return location[showdescription]["description"]

def show_time(player, showtime):
    return player.current_time

def dialogueOption(*options):
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    chosen = input().lower().strip()
    return chosen

def displayStatusDay1(player, plocation, current_time):
    print("Player Status:")
    print("+----------------------------------------------------------------------------+")
    print(f"Name: {player.full_name}")
    print(f"Location: {show_location(plocation)}")
    print(f"Description: {show_description(plocation)}")
    print(f"Time: {show_time(player, showtime=current_time)}")
    print(f"Level: {player.level}")
    print("Type actions to list all actions.")
    print("Need help? Type help!")
    print("+----------------------------------------------------------------------------+")

def helpCommand():
    for i, command in enumerate(commandlist, start=1):
        print(f"{i}. {command} - {commandlist[command]}")

def saveGame(player):
    while True:
        save = ask_confirmed_input("Would you like to save thus far? Y/N: ")
        if save in ["y", "yes"]:
            with open(SAVE_PATH, "w") as f:
                json.dump(player.to_save(), f, indent=4)
            sprint("Game saved succesfully.", delay=0.05)
            input()
            break
        elif save in ["n", "no"]:
            sprint("Game was not saved.")
            input()
            break
        else:
            print("Invalid option.")