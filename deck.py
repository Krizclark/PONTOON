import random

cards = ["♥2","♦2","♣2","♠2",
         "♥3","♦3","♣3","♠3",
         "♥4","♦4","♣4","♠4",
         "♥5","♦5","♣5","♠5",
         "♥6","♦6","♣6","♠6",
         "♥7","♦7","♣7","♠7",
         "♥8","♦8","♣8","♠8",
         "♥9","♦9","♣9","♠9",
         "♥T","♦T","♣T","♠T",
         "♥J","♦J","♣J","♠J",
         "♥Q","♦Q","♣Q","♠Q",
         "♥K","♦K","♣K","♠K",
         "♥A","♦A","♣A","♠A"]

class Deck:
    def __init__(self):
        self.cards = cards
        self.hand = []
        self.score_result = 0
        random.shuffle(cards)

    def single(self) -> "list":
        card = cards.pop(0)
        self.hand.append(card)
        random.shuffle(cards)
        return self.hand
    
    def double(self) -> "list":
        first  = cards.pop(0)
        second = cards.pop(1)
        self.hand.append(first)
        self.hand.append(second)
        random.shuffle(cards)
        return self.hand

    def score(self) -> "int":
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

