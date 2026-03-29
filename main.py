from player import Player
from data.ascii import ascii
from utils import sprint, cls
import json
from config import SAVE_PATH

def mainmenu():
    while True:
        sprint(ascii["title-screen"])
        sprint("1. New game")
        sprint("2. Load game")
        sprint("3. Exit game")
        choice = input().lower().strip()
        match choice:
            case "1" | "one":
                while True:
                    cls()
                    sprint("Are you sure you want to start a new game?")
                    sprint("This will empty your current save file. Y/N")
                    yn = input().lower().strip()
                    if yn in ["y", "yes"]:
                        save_string = {
                                "player": {
                                    "first_name": "",
                                    "last_name": "",
                                    "stats": {
                                        "courage": 0,
                                        "diligence": 0,
                                        "understanding": 0,
                                        "expression": 0,
                                        "knowledge": 0
                                    }
                                }
                            }
                        with open(SAVE_PATH, "w") as f:
                            json.dump(save_string, f, indent=4)
                        from game import intro
                        player = intro()
                        return player
                    elif yn in ["n", "no"]:
                        cls()
                        break
                    else:
                        print("Invalid option")
            case "2" | "two":
                from game import loadgame
                loadgame()
                break
            case "3" | "three":
                sprint("Exiting game...")
                exit()
            case _:
                print("Invalid option")


if __name__ == "__main__":
    player = mainmenu()
    from game import opening_cutscene
    if player.current_day == 1 and player.current_time == "morning":
        opening_cutscene(player)