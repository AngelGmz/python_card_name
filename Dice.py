from ursina import *

class Dice(Entity):
    
    def __init__(self, x, y, dice_type ) -> None:
        super().__init__(
            parent = camera.ui, 
            model='cube', 
            color=color.orange, 
            origin = (0,0) , 
            scale = (.1,.1,.1), 
            position=Vec2(x,y), 
            texture='box'
        )
        self.dice_type = dice_type
        self.role = self.random_role()
    
    def random_role(self):
        return random.choice(self.dice_type)

    def get_role(self):
        print("Rol: ", self.role)