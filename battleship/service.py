from abc import ABC, abstractmethod
from model import Game, GameStatus, Ships
import random
import time

class FireStrategy():
    @abstractmethod
    def getFireCordinates(self, n):
        pass

class RandomFireStrategy(FireStrategy):

    def getFireCordinates(self, n):
        return [random.randrange(n), random.randrange(n)]
    

class GameService:
    def __init__(self, n, player = 2, fireStrategy:FireStrategy= RandomFireStrategy()):
        self.fireStrategy = fireStrategy
        self.game = Game(n, player)
        
    def addShip(self, x, y, s, owner):
        ship = Ships(x,y,s)
        ship.setOwner(owner)
        try:
            self.game.addShips(ship)
        except Exception as e:
            print(e)


    

    def startGame(self):
        try:
            self.game.start()
        except Exception as e:
            print(e)
        turn = 0
        while self.game.status == GameStatus.Running:
            x, y = self.fireStrategy.getFireCordinates(self.game.Battlefield.size)
            player = turn%self.game.playerCnt+1
            try:
                print("player {} is firing at {},{}".format(player, x,y))
                self.game.fireAt(x,y,player)
            except Exception as e:
                print(e)
            turn +=1
            time.sleep(1)
        else:
            if self.game.status == GameStatus.Ended:
                print("winner: player{}".format(self.game.getWinner()))
            else:
                print("error starting game")
