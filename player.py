

class Player:
    def __init__(self, name: str, shape: str)-> None:
        self.name = name
        self.shape = shape

    # def make_move(self, x: int, y: int, board):
    #     if board[x][y] is None:
    #         board[x][y] = self.shape