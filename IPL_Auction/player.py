
Status = ["Draft", "Sold", "Unsold"]
Player_dir = {}

class Player:
    

    def __init__(self, name, base_price) -> None:
        self.name = name
        self.base_price = base_price
        self.status = 0
        self.bids = {}
        self.team = None
        self.high_bid = base_price-1
        self.win_price = None
        Player_dir[self.name]=self

    def __str__(self) -> str:
        return self.name
    
    def get_overview(self) -> str:
        return "name: {player_name}, status : {status}, team: {team}, price: {price}".format(
            player_name=self.name,
            status = Status[self.status],
            team= self.team if self.team else "N/A",
            price= self.win_price if self.win_price else "N/A"
            
        )
    def get_name(self):
        return self.name

    def check_bid(self, bid):
        return bid.price> self.high_bid

    def add_bid(self, bid):
        if self.status!=0:
            return False
        if self.check_bid(bid):
            self.high_bid = bid.price
            self.bids[bid.price]= bid
            return True
        else:
            return False

    def get_highest_bidder(self):
        if self.high_bid<self.base_price:
            return None
        else:
            return self.bids[self.high_bid]

    def update_team(self, bid):
        self.team = bid.team
        self.win_price = bid.price
        self.status=1
    
    def unsold(self):
        self.status = -1

    def check_status(self):
        return Status[self.status]

    def update_status(self):
        winner = self.get_highest_bidder()
        if winner:
            self.update_team(winner)
        else:
            self.unsold()
    def get_bids(self):
        bids = [self.bids[price] for price in self.bids]
        return bids




