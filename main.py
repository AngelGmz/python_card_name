from tkinter import W
from turtle import update
from ursina import *



class Inventory(Entity):
    def __init__(self,position, **kwargs ):
        super().__init__(
            parent = camera.ui,
            model = Quad(radius=.015),
            texture = 'cube',
            texture_scale = (7,1),
            scale = (.7, .1),
            origin = (-.5, .5),
            position = position,
            color = color.color(0,0,.1,.9),
            w=7,
            h=1,
            items_list = []
        )

        for key, value in kwargs.items():
            setattr(self, key, value)


    def find_free_spot(self):
        for y in range(self.h):
            for x in range(self.w):
                grid_positions = [(int(e.x*self.texture_scale[0]), int(e.y*self.texture_scale[1])) for e in self.children]
                print("grid pos:",grid_positions)

                if not (x,-y) in grid_positions:
                    print('found free spot:', x, y)
                    return x, y


    def append(self, item, x=0, y=0):
        print('add item:', item)
        white_dice = ['Guerrero', 'Ladrón', 'Mago', 'Clerigo', 'Campeón', 'Pergamino']
        black_dice = ['Goblin', 'Cofre', 'Golem', 'Esqueleto', 'Dragon', 'Posion']

        if len(self.children) >= self.w*self.h:
            print('inventory full')
            error_message = Text('<red>Inventory is full!', origin=(0,-1.5), x=-.5, scale=2)
            destroy(error_message, delay=1)
            return

        x, y = self.find_free_spot()

        icon = Draggable(
            parent = self,
            model = 'cube',
            color = color.tint(color.lime, -.5),
            scale_x = 1/self.texture_scale[0],
            scale_y = 1/self.texture_scale[1],
            origin = (-.5,.5),
            x = x * 1/self.texture_scale[0],
            y = -y * 1/self.texture_scale[1],
            z = -.5,
            highlight_color = self.color.tint(.2),
            
            )
        name = item.replace('_', ' ').title()

        if name == white_dice[0] or name ==  black_dice[0]:
            icon.color = color.tint(color.red, -.5)
            icon.text = 'W'
        if name == white_dice[1] or name ==  black_dice[1]:
            icon.color = color.green
        if name == white_dice[2] or name ==  black_dice[2]:
            icon.color = color.violet
        if name == white_dice[3] or name ==  black_dice[3]:
            icon.color = color.white
        if name == white_dice[4] or name ==  black_dice[4]:
            icon.color = color.yellow
        if name == white_dice[5] or name ==  black_dice[5]:
            icon.color = color.brown
       
        # if random.random() < .25:
        #     icon.color = color.gold
        #     name = '<orange>Rare ' + name

        icon.tooltip = Tooltip(name)
        icon.tooltip.background.color = color.color(0,0,0,.8)


        def drag():
            icon.org_pos = (icon.x, icon.y)
            icon.z -= .01   # ensure the dragged item overlaps the rest

        def drop():
            icon.x = int((icon.x + (icon.scale_x/2)) * self.w) / self.w
            icon.y = int((icon.y - (icon.scale_y/2)) * self.h) / self.h
            icon.z += .01

            # if outside, return to original position
            if icon.x < 0 or icon.x >= 1 or icon.y > 0 or icon.y <= -1:
                icon.position = (icon.org_pos)
                return

            # if the spot is taken, swap positions
            for c in self.children:
                if c == icon:
                    continue

                if c.x == icon.x and c.y == icon.y:
                    print('swap positions')
                    c.position = icon.org_pos

        icon.drag = drag
        icon.drop = drop
        self.items_list.append(icon)



if __name__ == '__main__':
    '''
    Config 
    '''
    

    app = Ursina()

    dungeon_lv = 1
    inventory = Inventory((-.3,.4))
    dungeon = Inventory((-.3,-.2))

    white_dice = ['Guerrero', 'Ladrón', 'Mago', 'Clerigo', 'Campeón', 'Pergamino']
    black_dice = ['Goblin', 'Cofre', 'Golem', 'Esqueleto', 'Dragon', 'Posion']

    def add_item():
        inventory.append(random.choice(white_dice))
    
    def remove_all_items():
        global dungeon
        print(dungeon.items_list)
        count = 0
        for enemy in dungeon.items_list: 
            count += 1
            
            destroy(enemy)
            print("count: ", count)
        dungeon.items_list = []
    def add_item_dungeon():
       
        global dungeon_lv
        
        remove_all_items()    
        for i in range(dungeon_lv):
            dungeon.append(random.choice(black_dice))
        
        dungeon_lv += 1
        print("dungleon lv: ",dungeon_lv)

    for i in range(7):
        add_item()


    add_item_button = Button(
        scale = (.1,.1),
        x = -.5,
        color = color.lime.tint(-.25),
        text = '+',
        tooltip = Tooltip('Explorar Mazmorra'),
        on_click = add_item_dungeon,

        )
    remove_all = Button(
        scale = (.1,.1),
        x = -.8,
        color = color.lime.tint(-.25),
        text = '- all',
        tooltip = Tooltip('Remover todos'),
        on_click = remove_all_items,

        )

    bg = Entity(parent=camera.ui, model='quad', texture='shore', scale_x=camera.aspect_ratio, z=1)
    Cursor(texture='cursor', scale=.1)
    mouse.visible = False
    window.exit_button.visible = True
    window.fps_counter.enabled = False

    def update():
        pass
        #print(mouse.x, mouse.y) 

    app.run()