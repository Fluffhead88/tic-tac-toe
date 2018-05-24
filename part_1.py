

"""class TicTac:

    def __init__(self):
        self.mark = None

    def filled(self):
        self.mark = 1

    def empty(self):
        self.mark = 0

    def __repr__(self):
        if self.mark == 1:
            return "X"
        else:
            return " " """

class Board:
    def __init__(self, size = 3):
        self.board = []

        for _ in range(3):
            self.board.append(["_"] * 3)

    def print_board(self):
        for row in self.board:
            print (row)


    def x_player_turn(self):
        mark = "X"
        mark = input("Please choose a place: ")
        position = (index(mark))
        if self.board[] == "_":
            self.board.append(position)
        else:
            print("invalid move")
        print (self.board)

    def O_player_turn(self):
        mark = "O"
        mark = input("Please choose a place: ")
        position = (index(mark))
        if self.board[] == "_":
            self.board.append(position)
        else:
            print("invalid move")
        print (self.board)




    def x_win(self):
        if "X" in ([0,0] and [0,1] and [0,2]:
        if "X" in ([1,0] and [1,1] and [1,2]:
        if "X" in ([2,0] and [2,1] and [2,2]:
        if "X" in ([0,0] and [1,0] and [2,0]:
        if "X" in ([1,0] and [1,1] and [2,1]:
        if "X" in ([2,0] and [2,1] and [2,2]:
            print ("X wins")

    def y_win(self):
        if "O" in ([0,0] and [0,1] and [0,2]:
        if "O" in ([1,0] and [1,1] and [1,2]:
        if "O" in ([2,0] and [2,1] and [2,2]:
        if "O" in ([0,0] and [1,0] and [2,0]:
        if "O" in ([1,0] and [1,1] and [2,1]:
        if "O" in ([2,0] and [2,1] and [2,2]:
            print ("O wins")






x = Board()
print(x.print_board()
