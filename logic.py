from player import *
from deck import *
import time
from graphical import *
bl = ".............................."

class Logic:

    def welcome(player):
        print("Welome to Lose your cash Casino!")
        time.sleep(1)
        print(bl)
        Logic.req_name(player)

    def req_name(player):
        time.sleep(1)
        name = input("Please enter name to play: ")
        player.add_name(name)
        time.sleep(1)
        print(bl)
        time.sleep(1)
        print(f"OK {player.name} Which game would you like to play!? ")
        time.sleep(1)
        print("      __________________")
        Logic.req_game(player)
    
    def req_game(player):
        if not player.name == None:
            print("     |                  |")
            print("     |    1.Pontoon     |")
            print("     |    2.Poker       |")
            print("     |    3.Solataire   |")
            print("     |__________________|")
            game = input((""))
            print(bl)
            if game.isdigit():
                if not game == "1":
                    print("Sorry, in development!")
                    Logic.req_game(player)
                else:
                    time.sleep(1)
                    print(f"OK {player.name} you currently have £{player.funds}")
                    print(bl)
                    Logic.req_bid(player)
            else:
                print("Please enter a number from the list!")
                Logic.req_game(player)



    def req_bid(player):
        if not player.name == None:
            deck = Deck()
            time.sleep(1)
            if not player.funds == 0:
                bid = input("How much would you like to deposit for ante? £")
                if player.funds >= int(bid):    
                    player.bid = int(bid)
                    Logic.bid(player,deck)
                    return player.bid
                else:
                    print(f"Unfortunately you only have £{player.funds}")
                    Logic.req_bid(player)
            else:
                print("Looks like you lost your cash")
                time.sleep(1)
                print(".........")
                time.sleep(1)
                print("GAME OVER")
                time.sleep(1)
                print(".........")
        else:
            Logic.req_name()  

    def bid(player,deck):
        time.sleep(1)
        print(f"OK {player.name} you have deposited £{player.bid} to the dealer!")
        player.funds -= player.bid
        print(f"You now have £{player.funds} remaining... Good Luck!")
        time.sleep(2)
        Logic.play(player,deck)

    def play(player,deck):
        deck.double()
        print("....")
        time.sleep(1)    
        print(f"{deck.hand}   score: {deck.score()}")
        time.sleep(2)
        Logic.loop(player,deck)
        
    def loop(player,deck):  
        step = input("Would you like to (s)Stick or (t)Twist!?...")  
        if step.isalpha():    
            if step.lower() == "t":
                time.sleep(1)
                deck.single()
                print(f"{deck.hand}   score: {deck.score()}")
                time.sleep(2)
                Logic.loop(player,deck)
            elif step.lower() == "s":
                score = int(deck.score())
                Logic.hold(player,score,deck)
            elif step.lower() == "e":
                Logic.req_bid(player)
            else:
                print("Please pick either (s)tick or t(wist)")
        else:
            print("Please pick either (s)tick or t(wist)")

    def hold(player,score,deck):
        time.sleep(1)
        if score > 21:
            print("Oh sorry you bust")
            time.sleep(1)
            print(f"Unlucky {player.name}, another hand!?...")
            deck.hand = []
            time.sleep(1)
            Logic.req_bid(player)
        else:
            if len(deck.hand) >= 5:
                print("Five Card Trick.....Nicely Played!!")
                reward = 2*player.bid
                player.funds += reward
                player.bid = 0
                print(f"player funds = {player.funds} as reward was {reward}")
                Logic.req_bid(player)
            else:
                time.sleep(2)
                print("Dealers hand......")
                Logic.dealershand(player,score,deck)
    
    def dealershand(player,score,deck):
        dealer = Player(None,funds = 1000)
        dealers_deck = Deck()
        print(f"Your current score to be beaten {score}")
        time.sleep(1)    
        print(f"{dealers_deck.double()}   score: {dealers_deck.score()}")
        while True:
            time.sleep(1)
            print("....")
            if dealers_deck.score() <= 15:
                print("Dealer Twists.....")
                print(f"{dealers_deck.single()}   score: {dealers_deck.score()}")
            else:
                print("Dealer Sticks")
                time.sleep(2)
                break
        time.sleep(2)
        if dealers_deck.score() < score:
            if score <= 21:
                print(f"Your hand of {score} beats the house's hand of {dealers_deck.score()}")
                reward = 2*player.bid
                player.funds += reward
                player.bid = 0
                print(f"player funds = {player.funds} as reward was {reward}")
                time.sleep(2)
                print("Another hand?....")
                deck.hand = []
                deck.score = 0
                dealers_deck.hand = []
                dealers_deck.score = 0
                Logic.req_bid(player)
        else:
            if dealers_deck.score() > 21:    
                deck.hand = []
                deck.score = 0
                dealers_deck.hand = []
                dealers_deck.score = 0
                print("Dealers bust!...You win!")
                reward = 2*player.bid
                player.funds += reward
                player.bid = 0
                print(f"player funds = {player.funds} as reward was {reward}")
                Logic.req_bid(player)
            else:
                time.sleep(2)
                print("House wins....Unlucky!")
                deck.hand = []
                deck.score = 0
                dealers_deck.hand = []
                dealers_deck.score = 0
                print(f"player funds = {player.funds}")
                Logic.req_bid(player)
    
