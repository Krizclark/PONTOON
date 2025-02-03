from logic import *
from deck import *

pack = Deck()

class Card:
    def __init__(self,A=None,N=None):
        self = self
        self.a = A
        self.n = N

    def draw_card(self):
        n = self.n
        a = self.a
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

                #print(f" _________ ")
                #print(f"|{self.n}       {self.n}|")
                #print("|         |")
                #print(f"|    {self.a}    |")
                #print(f"|         |")
                #print(f"|{self.n}_______{self.n}|")
                

#spacer = ' ' * 5
#for a, b in zip(a.splitlines(), b.splitlines()):
#    print(f'{a}{spacer}{b}')

print(pack.double())
