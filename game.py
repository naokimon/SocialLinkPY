from player import Player
from utils import cls, sprint, charprint, ask_confirmed_input, dialogueOption, displayStatusDay1, helpCommand, npcprint, saveGame, idprint
from data.dialogue import introDialogue, openingCutsceneDialogue, centralsdsouthintro
from data.locations import location
from main import SAVE_PATH
import json


def intro():
    cls()
    charprint("The Velvet Room", location["velvet_room"]["description"])
    for speaker, line in introDialogue[:5]:
        charprint(speaker, line, pause=True)
    charprint("igor", '"Now then... Why dont you introduce yourself...?"', pause=False)

    firstname = ask_confirmed_input("Enter your first name: ")
    lastname = ask_confirmed_input("Enter your last name: ")

    player = Player(first_name=firstname, last_name=lastname, current_location="velvet_room")

    for speaker, line in introDialogue[5:]:
        charprint(speaker, line, pause=True)

    cls()
    saveGame(player)
    return player


def opening_cutscene(player):
    player.current_location = "yasoinaba_station"
    player.current_time = "Afternoon"
    for speaker, line in introDialogue[23:]:
        charprint(speaker, line, pause=True)
    for speaker, line in openingCutsceneDialogue[:15]:
        charprint(speaker, line, pause=True)
    charprint("unfriendlylookinggirl", ('''"You dropped this."\n''' + '''She kneels down and grabs the note. She hands it to you.'''), pause=False)
    chosen = dialogueOption('"Thank you."', '''"It's not mine."''')
    while True:
        if chosen in ["thank you", "1"]:
            charprint("unfriendlylookinggirl", ('''"Whatever. All I did was pick it up."\n''' + '''> It's the note you made for yourself with Dojima's address...'''), pause=True)
            break
        elif chosen in ["it's not mine", "2"]:
            charprint("unfriendlylookinggirl", ('''"Well, take it anyway. I don't care."\n''' + '''> It's the note you made for yourself with Dojima's address...'''), pause=True)
            break
        else:
            print("Invalid option")

    for speaker, line in openingCutsceneDialogue[16:17]:
        charprint(speaker, line, pause=True)

    charprint("shopping-district", "> Inaba, Central shopping district, Gas station...", pause=True)

    for speaker, line in openingCutsceneDialogue[18:37]:
        charprint(speaker, line, pause=True)
    charprint("dojima", "What's wrong? You okay?", pause=True)
    chosen = dialogueOption('''"I'm just tired."''', '''"It's nothing."''', '''"I just felt lightheaded."''').lower().strip()
    while True:
        if chosen in ["just tired", "i just felt lightheaded", "1", "3"]:
            charprint("dojima", '''"That's understandable. It must have been a long trip for you."''')
        else:
            print("Invalid option")
            break

    for speaker, line in openingCutsceneDialogue[38:41]:
        charprint(speaker, line, pause=True)

    return player

def firstday(player):
    player.current_location = "central_sd_south_intro"
    current = location[player.current_location]
    displayStatusDay1(player, player.current_location, player.current_time)
    while True:
        choice = input("> ").strip().lower()
        match choice:
            case commandlist if commandlist in ["help"]:
                helpCommand()
            case action if action in ["action", "actions"]:
                for i, action in enumerate(current["actions"], start=1):
                    print(f"{i}. {action}")
            case shops if shops in ["shop", "shops"]:
                for i, shops in enumerate(current["shops"], start=1):
                    print(f"{i}. {shops.title()}")
                print("Type in the shop name to enter and check it out!")
            case clear if clear in ["cls", "clear"]:
                cls()
                displayStatusDay1(player, player.current_location, player.current_time)
            case shop if shop in current["shops"]:
                shop_info = current["shops"][shop]
                print(f'{shop.title()}: {shop_info["description"]}')
            case dojima if dojima in ["dojima", "talk to dojima"]:
                cls()
                charprint("dojima", "How're you feeling? Ready to get back in the car?", pause=False)
                ready = False
                while True:
                    chosen = dialogueOption('''"I'm ready."''', '''"Not yet..."''').lower().strip()
                    if chosen in ["i'm ready", "i'm ready.", "1"]:
                        ready = True
                        charprint("dojima", '''"All right, let's hit the road then."\n
                                                All of you make your way back into the car to head back to Dojima's residence.''')
                        break
                    elif chosen in ["not yet...", "not yet", "2"]:
                        charprint("dojima", "I see. Well, I'll be waiting here.", pause=True)
                        charprint("dojima", "You should take a walk around here. Hopefully it'll make you feel better.")
                        break
                if ready:
                    break
                else:
                    cls()
                    firstday(player)
            case bus if bus in ["wait at bus stop", "bus stop"]:
                sprint(current["buildings"]["bus_stop"]["description"])
            case lazystudent if lazystudent in ["talk to lazy student", "lazy student"]:
                for speaker, line in centralsdsouthintro[:3]:
                    npcprint(speaker, line, pause=True)
                cls()
                displayStatusDay1(player, player.current_location, player.current_time)
            case unfriendlygirl if unfriendlygirl in ["talk to unfriendly looking girl", "unfriendly looking girl"]:
                for speaker, line in centralsdsouthintro[3:4]:
                    charprint(speaker, line, pause=False)
                while True:
                    chosen = dialogueOption('''"I met you just now."''', '''"What were you doing at the station?"''', '''"It's just your imagination."''')
                    if chosen in ["i met you just now", "1", "i met you just now."]:
                        for speaker, line in centralsdsouthintro[4:7]:
                            charprint(speaker, line, pause=True)
                        cls()
                        displayStatusDay1(player, player.current_location, player.current_time)
                        break
                    elif chosen in ["what were you doing at the station", "what were you doing at the station?", "2"]:
                        for speaker, line in centralsdsouthintro[8:12]:
                            charprint(speaker, line, pause=True)
                        cls()
                        displayStatusDay1(player, player.current_location, player.current_time)
                        break
                    elif chosen in ["it's just your imagination", "it's just your imagination.", "3"]:
                        for speaker, line in centralsdsouthintro[7:8]:
                            charprint(speaker, line, pause=True)
                        cls()
                        displayStatusDay1(player, player.current_location, player.current_time)
                        break
            case nanako if nanako in ["nanako", "talk to nanako"]:
                for speaker, line in centralsdsouthintro[12:16]:
                    charprint(speaker, line, pause=True)
                cls()
                displayStatusDay1(player, player.current_location, player.current_time)
            case butterfly if butterfly in ["butterfly", "touch the butterfly"]:
                saveGame(player)
            case _:
                print("Invalid option")

    npcprint("naokimon", "Hey, thank you for playing this small little sneak peak/demo of social link! Make sure to star the project and follow me for more updates! If you find any bugs make sure to DM me about it on discord @naokimon", pause=True)



def loadgame():
    with open(SAVE_PATH, "r") as f:
        data = json.load(f)
    player = Player.from_save(data["player"])
    if player.current_day == 1 and player.current_location == "velvet_room":
        opening_cutscene(player)
    elif player.current_day == 1 and player.current_location in ["central_sd_south_intro", "dojimas_residence"]:
        firstday(player)


if __name__ == "__main__":
    debug_player = Player(
        first_name="Debug",
        last_name="Player",
        current_day=1,
        current_time="Afternoon",
        current_location="velvet_room"
    )
    loadgame()

