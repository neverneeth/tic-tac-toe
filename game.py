import random

class GameBoard():
    def __init__(self):
        self.board = [[i + j * 3 + 1 for i in range(3)] for j in range(3)]
        self.turn = 1
        self.shape = {1: 'O', 2: 'X'}
        self.count = 0
        self.mode = None

    def print_board(self):
        print("---------------")
        for i in range(3):
            for j in range(3):
                print(f"| {self.board[i][j]} |", end="")
            print("\n---------------")

    def update_board(self, pos):
        if pos < 1 or pos > 9:
            print("Out of range. Please choose 1 to 9")
            raise ValueError
        rows = (pos - 1) // 3
        cols = (pos - 1) % 3
        if not str(self.board[rows][cols]).isnumeric():
            print("Position already filled. Choose another")
            raise ValueError
        self.board[rows][cols] = self.shape[self.turn]
        self.count += 1
        self.turn = 2 if self.turn == 1 else 1


def save_game(game):
    with open("game_state.txt", "w") as f:
        for row in game.board:
            f.write(",".join(map(str, row)) + "\n")
        f.write(f"Player Turn: {game.turn}\n")
        f.write(f"Filled Squares: {game.count}\n")
        f.write(f"Mode: {game.mode}\n")
    print("Game progress saved!")


def load_game():
    try:
        with open("game_state.txt", "r") as f:
            lines = f.readlines()
            game = GameBoard()
            for i in range(3):
                game.board[i] = [int(x) if x.isnumeric() else x for x in lines[i].strip().split(",")]
            game.turn = int(lines[3].split(":")[1].strip())
            game.count = int(lines[4].split(":")[1].strip())
            game.mode = lines[5].split(":")[1].strip()
        print("Game progress loaded!")
        print(game.mode)
        return game
    except FileNotFoundError:
        print("No saved game found.")
        return GameBoard()
    except Exception as e:
        print(f"An error occurred while loading the game: {e}")
        return GameBoard()



def twop_game_loop(game):
    while True:
        try:
            game.mode = '2pe'
            if game.count == 9:
                game.print_board()
                print("Game Drawn")
                break
            game.print_board()
            n = input("Enter a position (1-9) or 'S' to save: ").strip()
            if n.upper() == 'S':
                save_game(game)
                break
            n = int(n)
            game.update_board(n)
            if win_checker(game):
                game.print_board()
                print("Winner is Player ", (2 if game.turn == 1 else 1))
                break
        except ValueError:
            print("Invalid move. Try again.")
        except Exception:
            print("An error occurred. Try again.")


def onep_easy_game_loop(game):
    while True:
        try:
            game.mode = "1pe"
            if game.count == 9:
                game.print_board()
                print("Game Drawn")
                break
            game.print_board()
            if game.turn == 1:
                n = input("Enter a position (1-9) or 'S' to save: ").strip()
                if n.upper() == 'S':
                    save_game(game)
                    break
                n = int(n)
            else:
                print("Computer is Playing...")
                empty_positions = [i + 1 for i in range(9) if str(game.board[i // 3][i % 3]).isnumeric()]
                n = random.choice(empty_positions)
            game.update_board(n)
            if win_checker(game):
                game.print_board()
                print("Winner is", ('Computer' if game.turn == 1 else 'Player 1'))
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


def opening_screen():
    print(r"""
 _________  ________  ______           _________  ________  ______           _________  ______  ______      
/________/\/_______/\/_____/\         /________/\/_______/\/_____/\         /________/\/_____/\/_____/\     
\__.::.__\/\__.::._\/\:::__\/   ______\__.::.__\/\::: _  \ \:::__\/   ______\__.::.__\/\:::_ \ \::::_\/_    
   \::\ \     \::\ \  \:\ \  __/______/\ \::\ \   \::(_)  \ \:\ \  __/______/\ \::\ \   \:\ \ \ \:\/___/\   
    \::\ \    _\::\ \__\:\ \/_/\__::::\/  \::\ \   \:: __  \ \:\ \/_/\__::::\/  \::\ \   \:\ \ \ \::___\/_  
     \::\ \  /__\::\__/\\:\_\ \ \          \::\ \   \:.\ \  \ \:\_\ \ \          \::\ \   \:\_\ \ \:\____/\ 
      \__\/  \________\/ \_____\/           \__\/    \__\/\__\/\_____\/           \__\/    \_____\/\_____\/ 
                                    WELCOME TO TIC-TAC-TOE
    """)


def main():
    while True:
        opening_screen()
        print("1. Start New Game")
        print("2. Load Game")
        print("3. Read Instructions")
        print("4. Exit")
        try:
            ch = int(input("Enter your choice: "))
            if ch == 1:
                mode = int(input("Choose Game Mode:\n1. Single Player\n2. Two Player\nEnter your choice: "))
                s = GameBoard()
                if mode == 1:
                    onep_easy_game_loop(s)
                elif mode == 2:
                    twop_game_loop(s)
                else:
                    print("Invalid mode. Returning to main menu.")
            elif ch == 2:
                s = load_game()
                if s.mode == '1pe':
                    onep_easy_game_loop(s)
                elif s.mode=='2pe':
                    twop_game_loop(s)
            elif ch == 3:
                print("""
Instructions:
- Enter 1-9 to select where you want to drop your mark.
- A row, column, or diagonal of the same mark wins.
- Player 1 uses 'O' and Player 2 (or Computer) uses 'X'.
""")
            elif ch == 4:
                print("Thank you for playing! Goodbye.")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()
