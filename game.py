from dialogue import introDialogue
from player import Player
from utils import cls, sprint, charprint, dprint, ask_confirmed_input, show_location, dialogueOption
from ascii import ascii
from dialogue import introDialogue, roomDescriptions, getPlayerDialogue, openingCutsceneDialogue
from main import SAVE_PATH
import json


def intro():
    cls()
    charprint("The Velvet Room", roomDescriptions["The Velvet Room"])
    for speaker, line in introDialogue[:5]:
        charprint(speaker, line, pause=True)
    charprint("igor", '"Now then... Why dont you introduce yourself...?"', pause=False)

    firstName = ask_confirmed_input("Enter your first name: ")
    lastName = ask_confirmed_input("Enter your last name: ")

    player = Player(first_name=firstName, last_name=lastName)

    for speaker, line in introDialogue[5:]:
        charprint(speaker, line, pause=True)

    cls()
    save = ask_confirmed_input("Would you like to save thus far? Y/N: ")
    if save in["y", "yes"]:
        with open(SAVE_PATH, "w") as f:
            json.dump(player.to_save(), f, indent=4)
    for line in introDialogue["train"]:
        charprint("train", line, pause=True)
    return player


def opening_cutscene(player):

    for speaker, line in openingCutsceneDialogue[:15]:
        charprint(speaker, line, pause=True)
    charprint("mariewohat", ('''"You dropped this."\n''' + '''She kneels down and grabs the note. She hands it to you.'''), pause=False)
    chosen = dialogueOption('"Thank you."', '''"It's not mine."''')
    while True:
        if chosen in ["thank you", "1"]:
            charprint("mariewohat", ('''"Whatever. All I did was pick it up."\n''' + '''> It's the note you made for yourself with Dojima's address...'''), pause=True)
            break
        elif chosen in ["it's not mine", "2"]:
            charprint("mariewohat", ('''"Well, take it anyway. I don't care."\n''' + '''> It's the note you made for yourself with Dojima's address...'''), pause=True)
            break
        else:
            print("Invalid option")

    for speaker, line in openingCutsceneDialogue[16:17]:
        charprint(speaker, line, pause=True)

    charprint("shopping-district", "> Inaba, Central shopping district, Gas station...", pause=True)

    for speaker, line in openingCutsceneDialogue[18:37]:
        charprint(speaker, line, pause=True)
    charprint("dojima", "What's wrong? You okay?", pause=True)
    chosen = dialogueOption('''"I'm just tired."''', '''"It's nothing."''', '''"I just felt lightheaded."''')
    while True:
        if chosen in ["just tired", "i just felt lightheaded", "1", "3"]:
            charprint("dojima", '''"That's understandable. It must have been a long trip for you."''')
        else:
            print("Invalid option")
            break

    for speaker, line in openingCutsceneDialogue[37:41]:
        charprint(speaker, line, pause=True)
    return player