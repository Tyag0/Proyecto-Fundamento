import time
from random import randint


class jugador():
    def __init__(self, nombre, ficha):
        self.nombre = nombre
        self.ficha = ficha

def tablero():
  print("")
  print("|1|2|3|4|5|6|7|")
  print("+","+","+","+","+","+","+","+",sep="-")
  print("|","|", "|", "|", "|","|","|","|")
  print("+","+","+","+","+","+","+","+",sep="-")
  print("|","|", "|", "|", "|","|","|","|")
  print("+","+","+","+","+","+","+","+",sep="-")
  print("|","|", "|", "|", "|","|","|","|")
  print("+","+","+","+","+","+","+","+",sep="-")
  print("|","|", "|", "|", "|","|","|","|")
  print("+","+","+","+","+","+","+","+",sep="-")
  print("|","|", "|", "|", "|","|","|","|")
  print("+","+","+","+","+","+","+","+",sep="-")
  print("|","|", "|", "|", "|","|","|","|")
  print("+","+","+","+","+","+","+","+",sep="-")
  print("")
    #En proceso...

def turno(jugador):
    row = input(f"{jugador.nombre}, indica un número de columna o pulsa [S] para tentar a la suerte: ")
    if row=="S":
        row = randint(1,7)
        print(f"mmm...suerte con eso, se eligió aleatoriamente la columna {row} para tu ficha")
    else:
        row = int(row)
    #En proceso...

play = True
try:
    while play:

        #INICIO DE PARTIDA#
        print(4*"*","CUATRO SEGUIDAS",4*"*")
        for i in range(1,3):
            nombre = input(f"Por favor indique nombre de participante #{i}: ")
            if i==1:
                ficha = input(f"{nombre}, por favor indica con qué ficha deseas jugar [X] o [O]: ")
                jugador1 = jugador(nombre, ficha)
            else:
                if ficha=="X":
                    ficha = "O"
                else:
                    ficha = "X"
                print(f"{nombre}, te toca jugar con la siguiente ficha: {ficha}")
                jugador2 = jugador(nombre, ficha)
        jugadores = [jugador1, jugador2] #En proceso
        
        #SELECCION DE QUIEN EMPIEZA
        print("")
        inicia = randint(0,1)
        time.sleep(3)
        print("Lanzando una moneda al aire para determinar quién inicia la partida...")
        time.sleep(5)
        if inicia == 0:
            print(f"La partida la inicia {jugador1.nombre}")
        else:
            print(f"La partida la inicia {jugador2.nombre}")
        
        #TABLERO INICIAL
        Win = False
        tablero()
        while not Win:
            if inicia==0:
                turno(jugador1)
            elif inicia==1:
                turno(jugador2)
            for i in jugadores:
                turno(i) #En proceso...
            Win = True #En proceso...

        continua = input("¿Desean volver a jugar? [Si] / [No]:")
        if continua == "No":
            play = False
except:
    pass #En proceso...
