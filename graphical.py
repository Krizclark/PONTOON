from logic import *

class Card:
    def __init__(self,hand):
        self.hand = hand
        self.face = ""
        self.n = [i[1] for i in self.hand] #Numbers are seperated into number only list
        self.s = [i[0] for i in self.hand] #Symbols  "   "     "   ""  symbol "  " "  "
        n = self.n
        s = self.s
        N = ' '.join(str(e) for e in n) #List in joined and still n
        S = ' '.join(str(e) for e in s) # ""  "" "    "
        card_quantity = len(self.hand)
        Card.get_print(self,N,S,card_quantity)
    
    def get_print(self,N,S,card_quantity): 
        x = -2
        i = card_quantity
        self.print = ""
        while i != 0:
            x += 2
            a = S[x]
            b = N[x]
            self.face = f'''
                    .---------.
                    | {b}       |
                    |         |
                    |    {a}    |
                    |         |
                    |       {b} |
                    '---------'
                    '''
            i -= 1
            self.print += self.face
        else:
            self.illustrate()

    def illustrate(self):
        pass

hand = ["♥T","♣4","♣7"]
Card(hand)


class savedprotocol():
    #spacer = "" * 5
    #for a, b, c in zip(a.splitlines(), b.splitlines(), c.splitlines()):
    #   print(f'{a}{spacer}{b}{spacer}{c}')
    #for d, e, in zip(d.splitlines(),e.splitlines()):
    #    print(f'{d}{spacer}{e}')
    #print(pack.double())
    pass
