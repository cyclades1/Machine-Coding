

def test_position(Board):
	pos = 2
	print("at snake or ladder ",Board.check_snake_ladder(pos))
	print("at snake ",Board.check_snake(pos))
	print("at ladder ",Board.check_ladder(pos))

def test_updation(Board):
	while Board.iswinner():
		Board.update_round()
	print(Board.getwinner())