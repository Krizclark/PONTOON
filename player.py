class Player:
    def __init__(self,name : str,funds : int =100, bid : int = None):
        self.name = name
        self.funds = funds
        self.bid = bid

    def add_name(self,name):
        if name:
            self.name = name.capitalize()

    def give(self,recipient,ante):
        if self.funds >= ante:
            recipient.funds += ante
            self.funds -= ante


