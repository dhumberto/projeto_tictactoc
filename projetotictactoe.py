import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class TicTacToeApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        game_layout = GridLayout(cols=3, spacing=10, size_hint=(None, None), width=300, height=300)

        self.board = [['', '', ''],
                      ['', '', ''],
                      ['', '', '']]

        self.buttons = []
        for row in range(3):
            row_buttons = []
            for col in range(3):
                button = Button(font_size=40, size_hint=(None, None), width=100, height=100)
                button.bind(on_press=self.on_button_press)
                game_layout.add_widget(button)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

        self.message_label = Label(text='', font_size=30)

        restart_button = Button(text='Reiniciar partida', size_hint=(None, None), width=200, height=50)
        restart_button.bind(on_press=self.restart_game)

        layout.add_widget(game_layout)
        layout.add_widget(self.message_label)
        layout.add_widget(restart_button)

        return layout

    def on_button_press(self, instance):
        row, col = self.get_button_coordinates(instance)

        if self.board[row][col] == '':
            if self.turn == 'X':
                self.board[row][col] = 'X'
                instance.text = 'X'
                self.turn = 'O'
            else:
                self.board[row][col] = 'O'
                instance.text = 'O'
                self.turn = 'X'

            if self.check_winner('X'):
                self.display_winner('X')
            elif self.check_winner('O'):
                self.display_winner('O')
            elif self.check_draw():
                self.display_draw()

    def get_button_coordinates(self, button):
        for row in range(3):
            for col in range(3):
                if self.buttons[row][col] == button:
                    return row, col

    def check_winner(self, player):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        return False

    def check_draw(self):
        for row in self.board:
            if '' in row:
                return False
        return True

    def display_winner(self, player):
        self.message_label.text = f'{player} venceu!'
        self.disable_buttons()

    def display_draw(self):
        self.message_label.text = 'Empate!'
        self.disable_buttons()

    def disable_buttons(self):
        for row in self.buttons:
            for button in row:
                button.disabled = True

    def restart_game(self, instance):
        self.clear_board()
        self.enable_buttons()
        self.message_label.text = ''
        self.turn = 'X'

    def clear_board(self):
        self.board = [['', '', ''],
                      ['', '', ''],
                      ['', '', '']]
        for row in self.buttons:
            for button in row:
                button.text = ''

    def enable_buttons(self):
        for row in self.buttons:
            for button in row:
                button.disabled = False

    def on_start(self):
        self.turn = 'X'

if __name__ == '__main__':
    TicTacToeApp().run()
