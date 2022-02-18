
Team_dir = {}

class Team:

    def __init__(self, name, wallet) -> None:
        self.name = name
        self.wallet = wallet
        self.bids = []
        self.players = []
        Team_dir[self.name] = self
    
    def __str__(self) -> str:
        return self.name

    def get_overview(self) -> str:
        return "name: {name}, players = {players}, wallet : {wallet}".format(
            name=self.name,
            players = self.players,
            wallet = self.wallet
            
        )

    def check_wallet(self, bid):
        return bid.price<=self.wallet

    def add_bid(self, bid):
        if self.check_wallet(bid):
            self.bids.append(bid)
            return True
        else:
            return False
    
    def add_player(self, bid):
        player = str(bid.player)
        price = bid.price
        self.players.append(player)
        self.wallet -= price

    def get_bids(self):
        return self.bids
    


