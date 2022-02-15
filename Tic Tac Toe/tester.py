from utils import Board


def test_update(game, pos):
    x, y = pos
    fl = game.move(x, y)
    if not fl:
        print('Invalid Move')

def test_winner(game):
    print(game.get_winner(), " won the Game.")