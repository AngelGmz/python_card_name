import random
import collections

class Carta:
  def __init__(self, numero, figura) -> None:
    self.numero = int(numero)
    self.figura = figura
    
  def imprimir_carta(self):
    if self.numero == 11:
      print(f"J de {self.figura}")
    elif self.numero == 12:
      print(f"Q de {self.figura}")
    elif self.numero == 13:
      print(f"K de {self.figura}")
    else:
      print(f"{self.numero} de {self.figura}")
    
  def __eq__(self, object) -> bool:
    return self.figura == object.figura and self.numero == object.numero
    

class Mazo:
  def __init__(self, figuras) -> None:
    self.cartas = []
    self.figuras = figuras
    self.llenar_mazo()
  
  def llenar_mazo(self):
    
    for figura in self.figuras:
      for i in range(1,14):
        self.cartas.append( Carta(i, figura) )
    self.barajear_cartas()
  
  def imprimir_mazo(self):
    print("::Mazo::")
    for carta in self.cartas:
      carta.imprimir_carta()
  
  def reparitr_carta(self):
    return self.cartas.pop()
  
  def barajear_cartas(self):
    random.shuffle(self.cartas)

        
class Jugador():
  def __init__(self, nombre) -> None:
    self.nombre = nombre
    self.turno = False
    self.mano = []
  
  def imprimir_mano(self):
    print("Mano de ",self.nombre)
    for m in self.mano:
      m.imprimir_carta()
  
  def imprimir_nombre(self):
    print("Jugador: ", self.nombre)
  
  def robar_carta(self, mazo):
    self.mano.append( mazo.reparitr_carta() )
    
    
class Juego():
  def __init__(self, fases, mazo) -> None:
    self.fases = fases
    self.fase_actual = 0
    self.jugadores = []
    self.mazo = mazo
  
  def repartir_cartas(self):
      for j in self.jugadores:
        while len( j.mano ) < 5:
          j.robar_carta(self.mazo)
  
  def iniciar_juego(self):
      self.fase_actual = 0
      self.definir_cola_de_turnos()
      self.repartir_cartas()
  
  def imprimir_fase_actual(self):
      print( self.fases[self.fase_actual])
  
  def siguiente_fase(self):
    self.fase_actual += 1
  
  def agreagar_jugador(self, jugadores):
    self.jugadores = jugadores
  
  def definir_cola_de_turnos(self):
    random.shuffle(self.jugadores)
    print(":: Orden de Turnos ::")
    for jugador in self.jugadores:
      print(jugador.nombre)
    
  def evaluar_mano(self, mano ):
    valores = [0]*14
    
    for carta in mano:
      valores[carta.numero] += 1
      
    print(valores)
    if self.es_par(valores) > 0:
      print(f"Hay {self.es_par(valores)} pares")

    if self.es_color(mano):
      print("Es color")

    

  def es_par(self,valores):
    pares = 0
    for i in range(len(valores)):
      if valores[i] == 2:
        pares += 1
    return pares

  def es_color(self, mano):
    carta_anterior = mano[0].figura
    color = True
    for carta in mano:
      if carta_anterior == carta.figura:
        carta_anterior = carta.figura
      else:
        color = False
    return color
    
    
figuras = ["Corazones" , "Picas", "Diamantes", "Treboles"]  
fases = [ "Repartir", "Cambiar", "Repartir", "Evaluar" ] 
mazo = Mazo(figuras)
ranking = { 1: 'Escalera Imperial' }

mena = Jugador("Mena")
lalo = Jugador("Lalo")
juego = Juego(fases, mazo)
juego.agreagar_jugador([mena,lalo])
juego.iniciar_juego()

mena.imprimir_mano()
lalo.imprimir_mano()

print(ranking[1])

juego.evaluar_mano(lalo.mano)









