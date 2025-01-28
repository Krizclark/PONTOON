from player import *
from deck import *
import time

class Logic:
    def req_name(player):
        name = input("Please enter name to play: ")
        player.add_name(name)
        Logic.req_game(player)
    
    def req_game(player):
        print("1.Pontoon")
        print("2.Poker")
        print("3.Solataire")
        if not player.name == None:
            game = input("Which game would you like to play!? ")
            if game.isdigit():
                if not game == "1":
                    print("Sorry, in development!")
                    Logic.req_game(player)
                else:
                    print(f"OK {player.name} you currently have {player.funds}")
                    Logic.req_bid(player)
            else:
                print("Please enter a number from the list!")
                Logic.req_game(player)

    def req_bid(player):
        if not player.name == None:
            bid = input("How much would you like to deposit for ante? £")
            player.bid = int(bid)
            Logic.play(player)
        else:
            Logic.req_name()  

    def play(player):
        print(f"{player.name} has deposited £{player.bid} in Pontoon!")
        player.funds -= player.bid
        player.bid = 0
        print(f"You have £{player.funds} remaining")
        time.sleep(1)
        print("Dealer gives you....")
        time.sleep(3)
        print(f"{deck.double()}   score: {deck.score()}")
        