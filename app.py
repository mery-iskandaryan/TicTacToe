from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
 
import sys
from game import Game


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.game = Game()
        self.board = self.game.board
        self.current_player = 'X'
        self.setWindowTitle("Tic Tac Toe ")
        self.setContentsMargins(20, 20, 20, 20)

        main_layout = QVBoxLayout(self)
        grid_layout = QGridLayout()

        self.buttons = [['' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                button = QPushButton(self)
                button.setFixedSize(100, 100)
                button.clicked.connect(lambda _, row=i, col=j: self.on_button_click(row, col))
                self.buttons[i][j] = button
                grid_layout.addWidget(button, i, j)


        v_layout = QVBoxLayout()

        self.reset_button = QPushButton('Reset Game', self, clicked = self.reset_game)
        self.reset_button.setFixedSize(150, 30)
  
        self.exit_button = QPushButton('Exit', self, clicked = self.exit_game)
        self.exit_button.setFixedSize(150, 30)
   
        
        v_layout.addWidget(self.reset_button, alignment=Qt.AlignmentFlag.AlignCenter)
        v_layout.addWidget(self.exit_button, alignment=Qt.AlignmentFlag.AlignCenter)

        main_layout.addLayout(grid_layout)
        main_layout.addLayout(v_layout)



    def on_button_click(self, row, col):
        if self.board[row][col] == '':
            self.board[row][col] = self.current_player
            self.buttons[row][col].setText(self.current_player)

            if self.game.win_cases():
                QMessageBox.information(self, 'Game Over', f'Player {self.current_player} wins!')
                self.reset_game()
            elif all(self.board[i][j] != '' for i in range(3) for j in range(3)):
                QMessageBox.information(self, 'Game Over', 'It\'s a draw!')
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def reset_game(self):
        self.game = Game()
        self.board = self.game.board
        self.current_player = 'X'

        for i in range(len(self.buttons)):
            for j in range(len(self.buttons)):

                self.buttons[i][j].setText('')

    def exit_game(self):
        self.close()



App = QApplication(sys.argv) 
App.setStyleSheet("""
    QMainWindow{
            background-color: 'black';
    }
    QPushButton{
            font-size: 20px;

    }
    }


""")

window = Window()
window.show()
sys.exit(App.exec())
