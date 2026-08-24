from termcolor import cprint
from treasure_island import TreasureIsland

def main():
    welcome_message = """
        Welcome to Treasure Island.
    Your mission is to find the treasure.
    """
    cprint(welcome_message,"light_blue")
    
    treasure_island = TreasureIsland()
    treasure_island.game()
    


if __name__ == "__main__":
    main()
