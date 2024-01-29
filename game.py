from board import Board


class Game:
    def __init__(self):
        self.board = Board().board
        self.players = []

    def win_cases(self) -> bool:
        for row in self.board:
            if all([row[0] == row[j] and row[j] != '' for j in range(len(row))]):
                return True
        for col in range(len(self.board)):
            item = self.board[0][col]
            if item != '' and all(self.board[row][col] == item for row in range(len(self.board))):
                return True
        if self.board[0][0] != '' and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return True
        elif self.board[-3][-1] != '' and self.board[-3][-1] == self.board[-2][-2] == self.board[-1][-3]:
            return True
        return False
    
