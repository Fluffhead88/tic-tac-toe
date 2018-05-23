#def CheckPosition(x):
#    if(board[x] == ' '):
#        return True
#    else:
#        return False

class Board:
    def __init__(self):
        self.space = [" "," "," "," "," "," "," "," "," "," "]

    def draw(self):
        print (self.space[1], " |", self.space[2], "|", self.space[3])
        print ("---+---+---")
        print (self.space[4], " |", self.space[4], "|", self.space[4])
        print ("---+---+---")
        print (self.space[7], " |", self.space[8], "|", self.space[9])



class Player:
    def __init__(self):
        self.xplayer = "X"
        self.oplayer = "O"

        for char in Board():
            if char == " "
                return True
            else:
                False
        while True:
            
        place = int(input("Pick a spot on the board between 1-9 > "))
        self.space.append(place)


    """def make_move(self):
        player = input(int())
        if self.space = " "
            self.space.append(player)"""






#x_move = int(input("Please choose a space number. > "))



board = Board()
board.draw()
