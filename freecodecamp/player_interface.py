from abc import ABC, abstractmethod
import random
class Player(ABC):
    def __init__(self)->None:
        self.moves = []
        self.position = (0,0)
        self.path = [self.position]
    
    #building the make move parent class

    def make_move(self)->tuple:
        move = random.choice(self.moves)
        self.position = (self.position[0]+move[0], self.position[1]+move[1])
        self.path.append(self.position)
        return self.position
    
    @abstractmethod
    def level_up(self):
        pass

#Define Moves of the pawn
class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves=[(0,1),(0,-1),(-1,0),(1,0)]
    def level_up(self):
        self.moves +=((1,1),(1,-1),(-1,1),(-1,-1))

p=Pawn()
p.make_move()


    