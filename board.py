class Board:
    def __init__(self):
        self.grid = [" " for _ in range(9)]

    def display(self):
        for i in range(3):
            print(f" {self.grid[i * 3]} | {self.grid[i * 3 + 1]} | {self.grid[i * 3 + 2]} ")
            if i < 2:
                print("---|---|---")

    def update(self, position, symbol):
        if self.grid[position] == " ":
            self.grid[position] = symbol
            return True
        return False

    def is_full(self):
        if " " not in self.grid:
            return True
        return False

    def check_winner(self, symbol):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
            [0, 4, 8], [2, 4, 6]  # diagonal
        ]
        for combination in win_combinations:
            if all(self.grid[i] == symbol for i in combination):
                return True
        return False
