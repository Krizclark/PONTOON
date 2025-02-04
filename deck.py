import random


cards = ["H2","D2","C2","S2",
         "H3","D3","C3","S3",
         "H4","D4","C4","S4",
         "H5","D5","C5","S5",
         "H6","D6","C6","S6",
         "H7","D7","C7","S7",
         "H8","D8","C8","S8",
         "H9","D9","C9","S9",
         "Ht","Dt","Ct","St",
         "Hj","Dj","Cj","Sj",
         "Hq","Dq","Cq","Sq",
         "Hk","Dk","Ck","Sk",
         "Ha","Da","Ca","Sa"]

class Deck:
    def __init__(self):
        self.cards = cards
        self.hand = []
        self.score_result = 0
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
        letter_sum = 0
        for char in letter_list:
            integer_sum= sum(integer_list)
            ace = False
            if char.isalpha():
                if char == "a":
                    letter_sum += 1
                    ace = True
                else:
                    letter_sum += 10
        sub_total = letter_sum + integer_sum
        
        if ace == True:
            if (sub_total + 10) <= 21:
                self.score_result = sub_total + 10
            else:
                self.score_result = sub_total
        else:
            self.score_result = sub_total
        return self.score_result

deck = Deck()