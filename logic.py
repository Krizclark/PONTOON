from player import *

class Logic:
    def req_name(player):
        name = input("Please enter name to play: ")
        player.add_name(name)
        Logic.req_bid(player)
    
    def req_bid(player):
        if not player.name == None:
            bid = input("How much would you like to deposit for ante? ")
            player.bid = bid
        else:
            Logic.req_name()  


