from enum import Enum
from typing import Dict


class BattleField:
    def __init__(self, n):
        self.field = [[0]*n for _ in range(n)]
        self.size = n
        

    def markCondinate(self, x, y, s, val):
        for i in range(x, x+s):
            for j in range(y, y+s):
                self.field[i][j]=val
        

    def __str__(self):
        return str(self.__dict__)


class ShipState(Enum):
    Active = "active"
    Destroyed = "destroyed"

class Ships:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.status = ShipState.Active
        self.owner = None

    def setOwner(self, owner):
        self.owner = owner

    def destroy(self):
        self.status = ShipState.Destroyed
    def __str__(self):
        return str(self.__dict__)

class GameStatus(Enum):
    Created = "created"
    Running = "running"
    Ended = "ended"

class ShipValidator:
    def validate(game:'Game', ship:Ships):
        if ship.owner>game.playerCnt or ship.owner>game.playerCnt<=0:
            raise Exception("invalid player")
        if game.status != GameStatus.Created:
            raise Exception("already running or ended game")
        if ship.x +ship.size >= game.Battlefield.size or ship.x +ship.size >= game.Battlefield.size:
            raise Exception("can not fit the ship")
        for i in range(ship.x, ship.x +ship.size):
            for j in range(ship.y, ship.y +ship.size):
                if game.Battlefield.field[i][j]!=0:
                    raise Exception("already an ship assinged to {} {}".format(i, j))
        
class Game:
    def __init__(self, n, player):
        if player<2:
            raise Exception("atleast 2 player required")
        self.Battlefield = BattleField(n)
        self.ships :Dict[Ships]= dict()
        self.playerCnt = player
        self.status = GameStatus.Created
        self.winner = None


    def __str__(self):
        return str(self.__dict__)
    

    
    def addShips(self, ship: Ships):
        ShipValidator.validate(self, ship)
        if ship.owner in self.ships:
            self.ships[ship.owner].append(ship)
        else:
            self.ships[ship.owner] = [ship]
        self.Battlefield.markCondinate(ship.x, ship.y, ship.size, ship.owner)

    def start(self):
        prvs = -1
        cnt = 0
        for owner in self.ships:
            if prvs ==-1:
                prvs = len(self.ships[owner])
               
            else:
                if prvs != len(self.ships[owner]):
                    raise Exception("not equal number of ships")
            cnt += 1
        if prvs ==0:
            raise Exception("no ships")
        if cnt != self.playerCnt:
            raise Exception("no ships for some player")
        self.status = GameStatus.Running

    def __updateWinner(self, winner):
        self.winner= winner

    def __calculateWinner(self):
        remaining = []
        for player in self.ships:
            if len(self.ships[player])!=0:
                remaining.append(player)
        if len(remaining)==1:
            return remaining[0]
        else:
            return None
        
    def __isGameEnded(self, ind, player):
        if ind == len(self.ships[player]):
            winner = self.__calculateWinner()
            if winner:
                self.__updateWinner(winner)
                self.status = GameStatus.Ended
                print("game ended..")
                return True
        return False

    def getWinner(self):
        return self.winner
    


    def fireAt(self, x, y, player):
        if self.Battlefield.field[x][y]==-1:
            raise Exception("already bombed location")
        if player == self.Battlefield.field[x][y]:
            raise Exception("blowing own ship")
        if 0 == self.Battlefield.field[x][y]:
            print("nothing happend")
        else:
            player = self.Battlefield.field[x][y]
            ind = -1
            for i in range(len(self.ships[player])):
                ship = self.ships[player][i]
                if ship.x <= x<ship.x+ship.size and ship.y <= y<ship.y+ship.size and ship.status == ShipState.Active:
                    ship.status = ShipState.Destroyed
                    print("ship destroyed at {}, {} of size {}, owner: {}".format(ship.x, ship.y, ship.size, player))
                    ind = i
                    break
            last= self.ships[player].pop()
            if self.__isGameEnded(ind, player):
                return 
            if ind ==-1:
                raise Exception("already blown ship for player {}".format(player))
            
            self.ships[player][ind]=last


        self.Battlefield.field[x][y]=-1
        


