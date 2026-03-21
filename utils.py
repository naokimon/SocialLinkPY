import sys, time, os
from ascii import ascii

def sprint(text, delay=0.005):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def dprint(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def charprint(character, dialogue, pause=True):
    cls()
    print(ascii[character])
    dprint(dialogue)
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
