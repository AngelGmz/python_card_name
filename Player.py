class Player(): 

    def __init__(self) -> None:
        self.dices = []
        self.points = 0
        self.inventory = []


    def show_dices(self):
        for dice in self.dices:
            dice.get_role()
    
    def append_random_dice(self, Dice):
        self.dices.append(Dice)
