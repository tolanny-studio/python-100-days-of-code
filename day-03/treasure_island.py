from termcolor import cprint


class TreasureIsland:

    def __init__(self):
        self.is_game_over = False
        self.option = ""

    def game_over(self):
        cprint("\nGame Over ⛔\n", "light_red")
        self.is_game_over = True

    def check_game_over(self, *options):
        if self.option in options:
            self.game_over()
        else:
            self.is_game_over = False

    def first_stage(self):
        while True:
            self.option = input("\nGo left or right? ").lower()

            if self.option not in ("r", "right", "l", "left"):
                cprint("Enter a valid option of left or right", "light_red")
                continue

            self.check_game_over("r", "right")
            break

    def second_stage(self):
        while True:
            self.option = input("\nDo you want to swim or wait? ").lower()

            if self.option not in ("s", "swim", "wait", "w"):
                cprint("Enter a valid option of swim or wait", "light_red")
                continue

            self.check_game_over("s", "swim")

            break

    def third_stage(self):
        while True:
            self.option = input("\nWhich door blue,red or yellow ? ").lower()

            if self.option not in ("r", "red", "blue", "b", "y", "yellow"):
                cprint("Enter a valid option of blue,re or yellow", "light_red")
                continue

            self.check_game_over("r", "red", "b", "blue")

            break

    def game(self):
        while not self.is_game_over:
            self.first_stage()

            if self.is_game_over:
                break

            self.second_stage()

            if self.is_game_over:
                break

            self.third_stage()

            if self.is_game_over:
                break

            cprint("\nYou win! 🌟🌟🌟🌟\n", "light_green")
