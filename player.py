from board import Board


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board: Board):
        while True:
            try:
                position = int(input(f"{self.name}: choose number 1-9 where you want to put '{self.symbol}' in: "))
                if position > 9 or position < 1:
                    raise ValueError
                if board.update(position - 1, self.symbol):
                    break
                else:
                    print("This position is already taken. Try again.")
            except ValueError:
                print("You have to type one of the numbers from 1 to 9.")
