from logic import *



class Card:
    def __init__(self,hand):
        self.card_a : str = "default"
        self.card_b : str = "default"
        self.card_c : str = "default"
        self.card_d : str = "default"
        self.card_e : str = "default"
        self.hand = hand
        self.face : str = ""
        self.n = [i[1] for i in self.hand] #Numbers are seperated into number only list
        self.s = [i[0] for i in self.hand] #Symbols  "   "     "   ""  symbol "  " "  "
        n = self.n
        s = self.s
        N = ' '.join(str(e) for e in n) #List in joined and still n
        S = ' '.join(str(e) for e in s) # ""  "" "    "
        card_quantity = len(self.hand)
        Card.get_print(self,N,S,card_quantity)
    
    def get_print(self,N,S,card_quantity) -> "str": 
        n = 0
        x = -2
        i = card_quantity
        self.print = ""
        while i != 0:
            x += 2
            a = S[x]
            b = N[x]
            self.face = f'''
        .-------.
        | {b}     |
        |       |
        |  {a}    |
        |       |
        |     {b} |
        '-------'
        '''
            i -= 1
            while n < 1:
                if self.card_a == "default":
                    self.card_a = self.face
                    self.face == ""
                elif self.card_b == "default":
                    self.card_b = self.face
                    self.face == ""
                elif self.card_c == "default":
                    self.card_c = self.face
                    self.face == ""
                elif self.card_d == "default":
                    self.card_d = self.face
                    self.face == ""
                elif self.card_e == "default":
                    self.card_e = self.face
                    self.face == ""
                n += 1
            n = 0                  
        self.illustrate()

    def illustrate(self):
        a = self.card_a
        b = self.card_b
        c = self.card_c
        d = self.card_d
        e = self.card_e
        if e == "default":
            if d == "default":
                if c == "default":
                    if b == "default":
                        if self.card_a == "default":
                            print(a)
                    else:
                        for a, b in zip(a.splitlines(), b.splitlines()):
                            print(f'{a}{b}')
                else:
                    for a, b, c in zip(a.splitlines(), b.splitlines(), c.splitlines()):
                        print(f'{a}{b}{c}')
            else:
                for a, b, c, d in zip(a.splitlines(), b.splitlines(), c.splitlines(), d.splitlines()):
                    print(f'{a}{b}{c}{d}')
        else:
            for a, b, c, d, e in zip(a.splitlines(), b.splitlines(), c.splitlines(), d.splitlines(), e.splitlines()):
                print(f'{a}{b}{c}{d}{e}')
