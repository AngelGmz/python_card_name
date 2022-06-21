class Game():
    """
    Maneja Parametros del juego
    -Turnos
    -Niveles
    """
    def __init__(self, players, fases) -> None:
        self.dongeon_lv = 3
        self.players = players
        self.fases = fases
        self.fase = fases[0]
    
    def next_dungeon_lv(self):
        self.dongeon_lv += 1
    
    def reset_dungeon_lv(self):
        self.dungeon_lv = 1
    
    def set_players_turn_false(players):
        for player in players:
            player.turn = False
            
    
    def set_turn(self, player):
        self.reset_dungeon_lv()
        self.set_players_turn_false(self.players)
        player.turn = True
        
        
        