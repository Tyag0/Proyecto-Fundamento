import time
from random import randint

#Se define las características de los jugadores
class jugador():
    def __init__(self, nombre, ficha):
        self.nombre = nombre
        self.ficha = ficha

    def turno(self):
        global table

        row = input(f"{self.nombre}, indica un número de columna o pulsa [S] para tentar a la suerte: ")
        if row=="S":
            row = randint(1,7)
            print(f"mmm...suerte con eso, se eligió aleatoriamente la columna {row} para tu ficha")
        else:
            row = int(row)
        
        for i in range(7):
            index = 7-i
            if table[index][row] == ".":
                table[index][row] = self.ficha
                break
        
        return tablero()

#Función que dibuja el tablero
def tablero():
    for i in range(9):
        for j in range(9):
            if j==8:
                print(table[i][j])
            else:
                print(table[i][j], end="")


play = True
try:
    while play:
        #Se define la forma estándar del tablero
        table = [["|","1","2","3","4","5","6","7","|"],
        ["+","-","-","-","-","-","-","-","+"],
        ["|",".",".",".",".",".",".",".","|"],
        ["|",".",".",".",".",".",".",".","|"],
        ["|",".",".",".",".",".",".",".","|"],
        ["|",".",".",".",".",".",".",".","|"],
        ["|",".",".",".",".",".",".",".","|"],
        ["|",".",".",".",".",".",".",".","|"],
        ["+","-","-","-","-","-","-","-","+"]]


        #INICIO DE PARTIDA#
        print(4*"*","CUATRO SEGUIDAS",4*"*")
        for i in range(1,3,1):
            nombre = input(f"Por favor indique nombre de participante #{i}: ")
            if i==1:
                ficha = input(f"{nombre}, por favor indica con qué ficha deseas jugar [X] o [O]: ")
                jugador1 = jugador(nombre, ficha)
            else:
                if ficha=="X" or ficha=="x":
                    ficha = "O"
                else:
                    ficha = "X"
                print(f"{nombre}, te toca jugar con la siguiente ficha: {ficha}")
                jugador2 = jugador(nombre, ficha)
        jugadores = [jugador1, jugador2]
        
        #SELECCION DE QUIEN EMPIEZA
        print("")
        inicia = randint(0,1)
        time.sleep(1)
        print("Lanzando una moneda al aire para determinar quién inicia la partida...")
        time.sleep(3)
        if inicia == 0:
            print(f"La partida la inicia {jugador1.nombre}")
        else:
            print(f"La partida la inicia {jugador2.nombre}")
        
        #TABLERO INICIAL 
        Win = False
        time.sleep(2)
        tablero()
        #Primera ronda de juego
        if inicia==0:
            jugador1.turno()
            jugador2.turno()
        elif inicia==1:
            jugador2.turno()

        #Ciclo para los turnos
        while not Win:
            for i in jugadores:
                i.turno()
                if table[2].count(".") == 0:
                  Win = True
                  break
        #Pregunta para volver a jugar
        continua = input("¿Desean volver a jugar? [Si] / [No]:")
        if continua == "No" or continua == "no":
            print("¡Gracias por jugar!")
            play = False
except:
    pass #En proceso...
