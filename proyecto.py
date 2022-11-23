import time
from random import randint

#Se define las características de los jugadores
class jugador():
    def __init__(self, nombre, ficha):
        self.nombre = nombre
        self.ficha = ficha

    def turno(self):
        global table
        global Win
        #Se consigue y define entrada del usuario
        try:
            row = input(f"{self.nombre}, indica un número de columna o pulsa [S] para tentar a la suerte: ")
            if row=="S" or row=='s':
                row = randint(1,7)
                print(f"mmm...suerte con eso, se eligió aleatoriamente la columna {row} para tu ficha")
            else:
                row = int(row)
                if row<1 or row>7:
                    raise ValueError
            for i in range(7):
                index = 7-i
                if table[index][row] == ".":
                    table[index][row] = self.ficha
                    break
        except:
            print('Upss.. opción inválida revisa la entrada')
            return self.turno()

        #Verificación de 4 en línea : Vertical, horizontal y diagonal
        if index<=4:
            for i in range(3):
                if table[index][row] != table[index+i+1][row]:
                    Win = False
                    break
                else:
                    Win = True
        #------------------------------------------------------
        for i in range(1,5):
            if not Win:
                for j in range(1,4):
                    if table[index][i] != table[index][i+j] and table[index][i] != '.':
                        Win = False
                        break
                    elif table[index][i] != '.':
                        Win = True
            else:
                break
        #------------------------------------------------------
        D1 = False
        D2 = False
        for i in range(4):
            for k in range(4): 
                if not Win:
                    for j in range(1,4):
                        if table[7-i][k+1] != table[(7-i)-j][(k+1)+j] and table[7-i][k+1] != '.':
                            D1 = False
                            break
                        elif table[7-i][k+1] != '.':
                            D1 = True
                    for j in range(1,4):
                        if table[7-i][k+4] != table[(7-i)-j][(k+4)-j] and table[7-i][k+4] != '.':
                            D2 = False
                            break
                        elif table[7-i][k+4] != '.':
                            D2 = True
                    if D1 or D2:
                        Win = True
                else:
                    break

        return Win, tablero()

#Función que dibuja el tablero
def tablero():
    for i in range(9):
        for j in range(9):
            if j==8:
                print(table[i][j])
            else:
                print(table[i][j], end="")

#INICIO DE PARTIDA#
print(4*"*","CUATRO SEGUIDAS",4*"*")
for i in range(1,3):
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

play = True

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
        
        #SELECCION DE QUIEN EMPIEZA
    print("")
    inicia = randint(0,1)
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
            if Win:
                break
            if table[2].count(".") == 0:
                Win = True
                break
        #Pregunta para volver a jugar
    print(f'{i.nombre} ha ganado la partida!!')
    continua = input("¿Desean volver a jugar? [Si] / [No]:")
    if continua == "No" or continua == "no":
        print("¡Gracias por jugar!")
        play = False
