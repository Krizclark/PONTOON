import random

cards = ["H2","D2","C2","S2",
         "H3","D3","C3","S3",
         "H4","D4","C4","S4",
         "H5","D5","C5","S5",
         "H6","D6","C6","S6",
         "H7","D7","C7","S7",
         "H8","D8","C8","S8",
         "H9","D9","C9","S9",
         "H10","D10","C10","S10",
         "Hj","Dj","Cj","Sj",
         "Hq","Dq","Cq","Sq",
         "Hk","Dk","Ck","Sk",
         "Ha","Da","Ca","Sa"]

class Deck:
    def __init__(self):
        self.cards = cards
        self.hand = []
        random.shuffle(cards)

    def single(self):
        card = cards.pop(0)
        self.hand.append(card)
        random.shuffle(cards)
        return self.hand
    
    def double(self):
        first  = cards.pop(0)
        second = cards.pop(1)
        self.hand.append(first)
        self.hand.append(second)
        random.shuffle(cards)
        return self.hand
    
    def score(self):
        list = [x[-1] for x in self.hand]
        letter_list = [''.join(filter(lambda ch: not ch.isdigit(), i)) for i in list]
        integer_list= [int(i) for i in list if i.isdigit()]


deck = Deck()
deck.double()
deck.single()
print(deck.score())