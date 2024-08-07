from player import Player
from board import Board
from random import randint


class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player("Player 1", "X"), Player("Player 2", "O")]
        self.current_player = self.players[randint(0, 1)]

    def switch_player(self):
        self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]

    def check_game_over(self):
        if self.board.check_winner(self.current_player.symbol):
            print(f'{self.current_player.name} ({self.current_player.symbol}) won!')
            return True
        elif self.board.is_full():
            print(f"It's a draw!")
            return True
        return False

    def play(self):
        self.board.display()
        running = True
        while running:
            self.current_player.make_move(self.board)
            self.board.display()
            if self.check_game_over():
                user_answer = input("Do you want to play again? (Y/N): ")
                if user_answer.upper() == 'Y':
                    self.reset()
                    running = False
                    self.play()
                else:
                    running = False
            else:
                self.switch_player()

    def reset(self):
        self.board.grid = [" " for _ in range(9)]
        self.current_player = self.players[randint(0, 1)]
