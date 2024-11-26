from service import GameService

if __name__=="__main__":

    gameService = GameService(6)
    # print(gameService.game.Battlefield)
    gameService.addShip(0,0,2,1)
    gameService.addShip(2,2,3,2)
    for row in gameService.game.Battlefield.field:
        print(row)
    gameService.startGame()
    