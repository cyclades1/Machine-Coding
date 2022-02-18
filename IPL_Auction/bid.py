class Bid:

    def __init__(self, team, player, price) -> None:
        self.team = team
        self.player = player
        self.price = price
    
    def __str__(self) -> str:
        return "team: {team}, player = {player}, price : {price}".format(
            team=self.team,
            player = self.player,
            price = self.price
            
        )