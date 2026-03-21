from dialogue import introDialogue
from player import Player
from utils import cls, sprint, charprint, dprint, ask_confirmed_input
from ascii import ascii
from dialogue import introDialogue, roomDescriptions

def intro():
    cls()
    charprint("The Velvet Room", roomDescriptions["The Velvet Room"])
    for line in introDialogue["igor"][:3]:
        charprint("igor", line, pause=True)
    charprint("igor", '"Now then... Why dont you introduce yourself...?"', pause=False)

    firstName = ask_confirmed_input("Enter your first name: ")
    lastName = ask_confirmed_input("Enter your last name: ")

    player = Player(first_name=firstName, last_name=lastName)

    for line in introDialogue["igor"][5:19]:
        charprint("igor", line, pause=True)
    for line in introDialogue["margaret"]:
        charprint("margaret", line, pause=True)
    for line in introDialogue["igor"][20:]:
        charprint("igor", line, pause=True)
    return player

intro()