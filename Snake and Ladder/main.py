from utils import Board

from tester import test_position, test_updation

getnum = lambda :int(input())
getnums = lambda : map(int, input().split())

def main():
	snakes = getnum()
	snake_list = []
	for _ in range(snakes):
		snake_list.append(list(getnums()))
	ladder = getnum()
	ladder_list = []
	for _ in range(ladder):
		ladder_list.append(list(getnums()))
	user = getnum()
	user_list = []
	for _ in range(user):
		user_list.append(input())

	board = Board(snake_list, ladder_list, user_list)
	while board.iswinner():
		board.update_round()
	print(board.getwinner(), "wins the game.")

if __name__=="__main__":
	main()