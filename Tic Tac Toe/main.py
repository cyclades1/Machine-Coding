from utils import Board
from tester import  test_update,test_winner

getnum = lambda: int(input())
getnums = lambda : map(int, input().split())

def print_board(game):
    board = game.get_board()
    for i in board:
        for c in i:
            print(c, end= " ")
        print()

def main():
    mark, name = list(input().split())
    user1 = (name ,mark) 
    mark, name = list(input().split())
    user2 = (name, mark) 
    game = Board(user1, user2)
    move = input()
    print_board(game)
    while move!="exit" and game.get_status()=="Running":
        x, y = list(map(int, move.split()))
        fl = game.move(x, y)
        if fl :
            print_board(game)
        else:
            print("Invalid Move")
        move = input()
    if game.get_status()!="Running":
        print(game.get_status())


if __name__=="__main__":
    main()