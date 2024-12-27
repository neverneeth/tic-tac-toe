import random

class GameBoard():

    def __init__(self):
        self.board= [[i+j*3+1 for i in range(3)]for j in range(3)]
        self.turn = 1
        self.shape = {1: 'O', 2: 'X'}
        self.count = 0

    def print_board(self):
        print("---------------")
        for i in range(3):
            for j in range(3):
                print(f"| {self.board[i][j]} |", end="")
            print("\n---------------")

    def update_board(self, pos):
        if pos<1 or pos>9:
            print("Out of range. Please choose 1 to 9")
            raise ValueError
        rows = (pos-1)//3
        cols = (pos-1)%3
        if not str(self.board[rows][cols]).isnumeric():
            print("Position already filled. Choose another")
            raise ValueError
        self.board[rows][cols] = self.shape[self.turn]
        self.count+=1
        self.turn = 2 if self.turn == 1 else 1

def twop_game_loop(game):
    while True:
        try:
            if game.count == 9:
                game.print_board()
                print("Game Drawn")
                break
            game.print_board()
            n = int(input("Enter a position (1-9): "))
            game.update_board(n)
            if win_checker(game):
                game.print_board()
                print("Winner is Player ", (2 if game.turn ==1 else 1))
                break
        except ValueError:
            print("Invalid move. Try again.")
        except Exception:
            print("An error occurred. Try again.")
    
def onep_easy_game_loop(game):
    while True:
        try:
            if game.count == 9:
                game.print_board()
                print("Game Drawn")
                break
            game.print_board()
            if game.turn==1:
                print("Player Turn: ")
                n = int(input("Enter a position (1-9): "))
            else:
                print("Computer is Playing...")
                empty_positions = [i+1 for i in range(9) if str(game.board[i//3][i%3]).isnumeric()]
                n = random.choice(empty_positions)
            game.update_board(n)
            if win_checker(game):
                game.print_board()
                print("Winner is ", ('Computer' if game.turn ==1 else 'Player 1'))
                break
        except ValueError:
            print("Invalid move. Try again.")
        except Exception:
            print("An error occurred. Try again.")

def win_checker(game):
    state = game.board
    for row in state:
        if row[0] == row[1] == row[2]:
            return True
    
    for col in range(3):
        if state[0][col] == state[1][col] == state[2][col]:
            return True
    
    if state[0][0] == state[1][1] == state[2][2]:
        return True
    
    if state[0][2] == state[1][1] == state[2][0]:
        return True

    return False

def main():
    s = GameBoard()
    onep_easy_game_loop(s)

if __name__ == "__main__":
    main()