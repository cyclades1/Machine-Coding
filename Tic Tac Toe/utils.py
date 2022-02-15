N = 3

class Board:
    def __init__(self, user1, user2) -> None:
        self.board = [['-']*N for i in range(N)]
        self.chance = 0
        self.users = [user1[1], user2[1]]
        self.userbymark = {user1[1]:user1[0],user2[1]:user2[0]}
        self.winner = None
        self.status = "Running"
        self.turn = 0

    def check_row(self, x, y):
        cur= self.board[x][y]
        i, j = x,y
        cnt = 0
        while self.board[i][j]==cur:
            j=(j+1)%N
            cnt+=1
            if cnt ==N:
                return True
        return False
    
    def check_col(self, x, y):
        cur= self.board[x][y]
        i, j = x,y
        cnt = 0
        while self.board[i][j]==cur:
            i=(i+1)%N
            cnt+=1
            if cnt ==N:
                return True
        return False

    def check_digonal(self, x, y):
        cur= self.board[x][y]
        i, j = x,y
        cnt = 0
        while self.board[i][j]==cur:
            i=(i+1)%N
            j=(j+1)%N
            cnt+=1
            if cnt ==N:
                return True
        i, j = x,y
        cnt = 0
        while self.board[i][j]==cur:
            i=(i-1)%N
            j=(j-1)%N
            cnt+=1
            if cnt ==N:
                return True
        return False

    def update_status(self, x, y):
        fl = self.check_col(x,y) or self.check_row(x,y) or self.check_digonal(x,y) 
        if fl:
            self.winner = self.board[x][y]
            self.status =  self.get_winner() + " won the Game."
        if self.turn ==9:
            self.status = "Game over"

    def move(self, x, y):
        if x>N or x<1 or y<1 or y>N or self.board[x-1][y-1]!='-':
            return False
        self.board[x-1][y-1]=self.users[self.chance]
        self.chance ^= 1
        self.turn+=1
        self.update_status(x-1, y-1)
        return True
        
    def get_status(self):
        return self.status

    def get_winner(self):
        if not self.winner:
            return "No Winner"
        return self.userbymark[self.winner]
    
    def get_board(self):
        return self.board

    def __str__(self) -> str:
        return str(self.board)