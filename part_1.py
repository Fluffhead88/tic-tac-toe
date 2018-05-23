

class Board:
    def __init__(self):
        self.space = [" "," "," "," "," "," "," "," "," "," "]

    def draw(self):
        print (self.space[1], " |", self.space[2], "|", self.space[3])
        print ("---+---+---")
        print (self.space[4], " |", self.space[4], "|", self.space[4])
        print ("---+---+---")
        print (self.space[7], " |", self.space[8], "|", self.space[9])

    def free_space(self):
        if self.space == " ":
            return True

    def move(self):
        print("Choose a place between 1-9 > ")
        place = int(input())
        self.space.append(place)
        return place
    
    def win(self):
        possible_wins = ([1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7])

"""class Player:
    def __init__(self):

            place = int(input("Pick a spot on the board between 1-9 > "))
            self.space.append(place)
        return place"""






"""def make_move(self):
    player = input(int())
    if self.space = " "
        self.space.append(player)"""






#x_move = int(input("Please choose a space number. > "))


board = Board()
board.draw()
board.move()
