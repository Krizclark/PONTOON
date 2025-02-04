from logic import *

class Card:
    def __init__(self,card_number,card_suit):
        self = self
        self.card_number = card_number
        self.card_suit = card_suit

    def ilustrate(self,card_number,card_suit):
        n = card_suit
        a = card_number
        if n:
            if a: 
                return  f'''\
                        .-------.
                        |{a }      |
                        |       |
                        |   {n }   |
                        |       |
                        |      {a}|
                        '-------'
                        '''
                




#spacer = ' ' * 5
#for a, b in zip(a.splitlines(), b.splitlines()):
#    print(f'{a}{spacer}{b}')
#print(pack.double())
