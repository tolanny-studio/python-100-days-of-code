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
                cprint("Enter a valid option of blue,red or yellow", "light_red")
                continue

            self.check_game_over("r", "red", "b", "blue")

            break

    def game(self):
        while True:
            stages = [self.first_stage, self.second_stage, self.third_stage]
            for stage in stages:
                stage()
                if self.is_game_over:
                    break
            if not self.is_game_over:
                cprint("\nYou win! 🌟🌟🌟🌟\n", "light_green")

            replay = input("Do you want to replay ? Yes/No ").lower()
            if replay not in ("yes", "y"):
                break