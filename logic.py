from player import *
from deck import *
import time

class Logic:
    def welcome(player):
        print("Welome to Lose your cash Casino!")
        time.sleep(1)
        Logic.req_name(player)

    def req_name(player):
        name = input("Please enter name to play: ")
        player.add_name(name)
        time.sleep(1)
        Logic.req_game(player)
    
    def req_game(player):
        if not player.name == None:
            print("1.Pontoon")
            print("2.Poker")
            print("3.Solataire")
            game = input(f"OK {player.name} Which game would you like to play!? ")
            if game.isdigit():
                if not game == "1":
                    print("Sorry, in development!")
                    Logic.req_game(player)
                else:
                    time.sleep(1)
                    print(f"OK {player.name} you currently have £{player.funds}")
                    Logic.req_bid(player)
            else:
                print("Please enter a number from the list!")
                Logic.req_game(player)



    def req_bid(player):
        if not player.name == None:
            time.sleep(1)
            bid = input("How much would you like to deposit for ante? £")
            player.bid = int(bid)
            Logic.bid(player)
        else:
            Logic.req_name()  

    def bid(player):
        time.sleep(1)
        print(f"OK {player.name} you have deposited £{player.bid} to the dealer!")
        player.funds -= player.bid
        player.bid = 0
        print(f"You now have £{player.funds} remaining... Good Luck!")
        time.sleep(2)
        Logic.play(player)

    def play(player):
        print("....")
        time.sleep(1)    
        print(f"{deck.double()}   score: {deck.score()}")
        time.sleep(2)
        Logic.loop(player)
        
    def loop(player):  
        step = input("Would you like to (s)Stick, (t)Twist or (h)Hold!?...")  
        if step.isalpha():    
            if step.lower() == "s":
                print("s")
            elif step.lower() == "t":
                time.sleep(1)
                print(f"{deck.single()}   score: {deck.score()}")
                time.sleep(2)
                Logic.loop(player)
            elif step.lower() == "h":
                score = int(deck.score())
                Logic.hold(player,score)
            elif step.lower() == "e":
                Logic.req_bid()
            else:
                print("Please pick either (s)tick, t(wist) or (h)old")
        else:
            print("Please pick either (s)tick, t(wist) or (h)old")

    def hold(player,score):
        time.sleep(1)
        if score > 21:
            print("Oh sorry you bust")
            time.sleep(1)
            print(f"Unlucky {player.name}, another hand!?...")
            deck.hand = []
            time.sleep(1)
            Logic.req_bid(player)
        else:
            time.sleep(2)
            print("Dealers hand......")


    
