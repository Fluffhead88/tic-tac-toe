

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

    def printboard(self):
        for row in self.board:
            print (row)


    """def player_turn(self):
        turn = input()
        x[]



    def win(self):
        if "X" in (row[0] and row[1] and row[2]:
            print "X win's" """



#player_turn()
x = Board()
print(x.printboard())
