import numpy as np

#We nee dto make a class for the baord
#0 unoccupied
#1 X
#-1 O
class tictactoe:
    def __init__(self):
        self.board = np.zeros((3,3), dtype=int)
        self.current_player = 1 
        #if current player = 1: X, current player = -1, O, player = 0, empty square

    def display_board(self):
        symbols = {1: "X", -1: "O", 0: " "}

        for row in self.board:
            print(" | ".join(symbols[int(cell)] for cell in row))
            print("---------")

    def reset_board(self):
        self.board = np.zeros((3,3), dtype=int)
        self.current_player = 1
        return self.board

    def get_valid_moves(self):
        valid_moves = [] #makes sure the ai has a list of options it can choose from

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i,j] == 0:
                    valid_moves.append((i,j))

        return valid_moves

    def play_move(self, row, col):
        moves = self.get_valid_moves()
        if self.is_game_over():
            return False
        if (row, col) in moves:
            self.board[row,col] = self.current_player
        else:
            return False
        if not self.is_game_over():
            self.current_player *= -1

        return True


    def check_winner(self): #return true is sm1 won
        board = self.board
        #winner = self.current_player
        #check rows
        for i in range(3):
            if (board[i, 0] == board[i, 1] == board[i, 2]) and (board[i, 0] != 0):
                return board[i,0]

        #check columns
        for i in range(3):
            if (board[0,i] == board[1, i] == board[2, i]) and (board[0,i] != 0):
                return board[0,i]

        #check diagonals
        if (board[0,0] == board[1,1] == board[2,2]) and (board[0,0] != 0):
            return board[0,0]

        if (board[0,2] == board[1,1] == board[2,0]) and (board[0,2] != 0):
            return board[0,2]

        return None #if no one wins

    def is_draw(self): #return true if a draw
        valid_moves = self.get_valid_moves()

        if len(valid_moves) == 0 and (self.check_winner() == None):
            return True

        return False #so if it isnt a draw false is returned
        

    def is_game_over(self):
        winner = self.check_winner()
        draw = self.is_draw()
        if winner or draw:
            return True
        return False

x_win = 0
o_win = 0
draw = 0
#agent
import random
def random_agent(game):
    valid_moves = game.get_valid_moves()

    return random.choice(valid_moves)

for _ in range(1000):
    game = tictactoe()

    #implement two agents playing against eachother

    while not game.is_game_over():
        #print(f"It's {game.current_player}'s turn")
        row, col = random_agent(game)
        game.play_move(row, col)
            
    game.display_board()

    if game.check_winner() == 1:
        x_win += 1
    elif game.check_winner() == -1:
        o_win += 1
    else:
        draw += 1

    if game.check_winner() is not None:
        print(f"Player {game.check_winner()} wins")
    else:
        print("It's a draw")

print(x_win, o_win, draw)
print(f"X win rate: {x_win / 1000 * 100:.1f}%")
print(f"O win rate: {o_win / 1000 * 100:.1f}%")
print(f"Draw rate: {draw / 1000 * 100:.1f}%")
