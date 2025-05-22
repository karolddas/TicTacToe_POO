class TicTacToe:
    def __init__(self):
        self.board = [i for i in range(1, 10)]
        self.used_numbers = []
        self.win_combos = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],   # filas
            [1, 4, 7], [2, 5, 8], [3, 6, 9],   # columnas
            [1, 5, 9], [3, 5, 7]               # diagonales
        ]
        self.times = 0
        self.game_over = False

    def print_board(self):
        for i in range(0, 9, 3):
            print(self.board[i], self.board[i + 1], self.board[i + 2])

    def make_move(self, player, symbol):
        while True:
            try:
                number = int(input(f"{player} choose the number to place your symbol {symbol}: "))
                if number < 1 or number > 9 or number in self.used_numbers:
                    raise ValueError
                self.used_numbers.append(number)
                self.board[number - 1] = symbol
                break
            except ValueError:
                print("ERROR: Invalid or already used number. Try again with another number between 1 and 9.")

    def check_winner(self, symbol):
        for combo in self.win_combos:
            if self.board[combo[0]-1] == self.board[combo[1]-1] == self.board[combo[2]-1] == symbol:
                self.print_board()
                print(f"\n🎉 We have a winner! {symbol} wins!")
                self.game_over = True
                return True
        return False

    def play(self):
        print("Welcome to the Tic Tac Toe Game!")
        print("Player 1: X   Player 2: O")
        print("To win, align 3 of your symbols in any direction. Good luck!\n")
        self.print_board()

        while self.times < 9 and not self.game_over:
            self.make_move("Player 1", "X")
            self.print_board()
            self.times += 1
            if self.check_winner("X") or self.times == 9:
                break

            self.make_move("Player 2", "O")
            self.print_board()
            self.times += 1
            if self.check_winner("O") or self.times == 9:
                break

        if not self.game_over:
            print("\n🤝 It's a draw! Nobody wins.")

game = TicTacToe()
game.play()