from termcolor import cprint

class TreasureIsland:

    def __init__(self):
        self.is_game_over = False

    def game_over(self):
        cprint("\nGame Over ⛔\n", "light_red")

    def game(self):
        option = ""
        while True:
            option = input("\nGo left or right ? ").lower()
            if option in ("r", "right"):
                self.game_over()
                break
            else:
                option = input("\nDo you want to swim or wait ? ").lower()
                if option in ("swim", "s"):
                    self.game_over()
                    break
                else:
                    option = input("\nWhich door blue,red or yellow ? ").lower()
                    if option in ("red", "r", "blue", "b"):
                        self.game_over()
                        break
                    else:
                        cprint("\nYou win! 🌟🌟🌟🌟\n","light_green")
