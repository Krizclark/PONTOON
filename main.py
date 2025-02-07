from app import *
from player import *
from logic import *

player = Player(None)
running = False

if __name__ == "__main__":
    if running == True:
        Logic.req_game(player)
    else:
        App()