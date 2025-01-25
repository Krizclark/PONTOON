class Player:
    def __init__(self,name,funds =100,bid=None):
        self.name = name
        self.funds = funds
        self.bid = bid

    def give(self,recipient,ante):
        if self.funds >= ante:
            recipient.funds += ante
            self.funds -= ante


player = Player(None)
dealer = Player("Dealer",1000)

