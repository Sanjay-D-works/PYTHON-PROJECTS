class TicTacToc:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #we will use a single list to rep 3*3 board
        self.current_winner = None #keep track of winner!

    def print_board(self):
        #This  is just getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' * '| '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' * '| '.join(row) + ' |')


    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_
       

def play(game, x_player, o_player , print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X' #strating letter
    # iterate while the game still has empty square 
    while game.empty_squares():
        pass
