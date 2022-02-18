from player import Player, Player_dir
from team import Team, Team_dir
from bid import Bid

class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return(self.msg)
# raise(MyError("message"))

def create_player(name, price):
    if price<0:
        print("negative number can not be base price")
        return
    test_player = Player(name, price)

def create_team(name, wallet):
    test_team = Team(name,wallet)

def create_bid(team, player, price):
    try:
        bid = Bid(team, player, price)
        if Team_dir[team].check_wallet(bid) and Player_dir[player].check_bid(bid):
            Team_dir[team].add_bid(bid)
            Player_dir[player].add_bid(bid)
        else:
            print("Invalid Bid")
    except Exception as e:
        print("player or team does not exits")

def auction_start(player):
    try:
        if Player_dir[player].check_status()!= "Draft":
            print("Action for {player} has been done".format(player=player))
            return None
        return player
    except Exception as e:
        print("player does not exist")
        return None

def auction_end(player):
    winner = Player_dir[player].get_highest_bidder()
    if winner:
        Player_dir[player].update_team(winner)
        Team_dir[winner.team].add_player(winner)
        print(player, "sold to ",winner.team)
    else:
        Player_dir[player].unsold()
        print("Unsold")

def getplayerbids(player):
    try:
        bids = Player_dir[player].get_bids()
        for bid in bids:
            print(bid.team, bid.price)
    except Exception as e:
        print("Player does not exits")

def getteambids(team):
    try:
        bids = Team_dir[team].get_bids()
        for bid in bids:
            print(bid.player, bid.price)
    except Exception as e:
        print("Team does not exits")


