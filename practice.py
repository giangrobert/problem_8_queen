import random

# inicializamos el tablero
tablero = []
n = 8
for _ in range(n):
    fila = [" "] * n
    tablero.append(fila)


def tablero_view():
    for tabler in tablero:
        print(tabler)


# agregamos las posiciones de los ataques de la reina
def ataque_cruz(x, y):
    # ataque en la misma fila
    for i in range(n):
        if i != y:
            tablero[x][i] = "X"  # ataque en la misma fila

    # ataque en la misma columna
    for i in range(n):
        if i != x:
            tablero[i][y] = "X"  # ataque en la misma columna


def ataques_diagonales(x, y):
    for fila in range(n):
        for columna in range(n):
            if fila == x and columna == y:
                tablero[fila][columna] = "Q"
            elif fila + columna == x + y:
                tablero[fila][columna] = "X"
            elif fila - columna == x - y:
                tablero[fila][columna] = "X"


# colocamos todos los ataques en el tablero


def ataques(x, y):
    ataque_cruz(x, y)
    ataques_diagonales(x, y)


reinas = 0
posiciones = []

# en esta lista se guardan las listas de las posiciones de las reinas


def poner_posiciones():
    global reinas
    for _ in range(500):
        # agregamos una posocion aleatoria de la reina x e y
        position_x = random.randint(0, 7)  # fila
        position_y = random.randint(0, 7)  # columnas

        if tablero[position_x][position_y] == " ":  # si la posicion esta vacia
            tablero[position_x][position_y] = "Q"
            ataques(position_x, position_y)
            reinas += 1
            posiciones.append([position_x, position_y])


poner_posiciones()
print(reinas)

while reinas != 8:
    tablero = [[" "] * n for _ in range(n)]
    posiciones = []
    poner_posiciones()
    reinas = len(posiciones)
    if reinas == 8:
        for fila in tablero:
            print(fila)
        print("Se ha colocado 8 reinas correctamente.")

tablero_view()


# visualizamos el tablero en un ventana con tkinter
import tkinter as tk

ventana = tk.Tk()
ventana.title("8 Reinas")

# dibujamos el tablero
for i in range(8):
    for j in range(8):
        color = "black" if (i + j) % 2 == 0 else "white"
        casilla = tk.Label(ventana, bg=color, width=14, height=7)
        casilla.grid(row=i, column=j)


imagen = tk.PhotoImage(file="reina2.png")
imagen = imagen.subsample(8, 8)
# colocar la imagen de la lista de posiciones que se guardo
for posicion in posiciones:
    reyna_colocada = tk.Label(ventana, image=imagen)
    reyna_colocada.grid(row=posicion[0], column=posicion[1])


# colocando u cuadro  de detalles al lado de la tabla, donde vemos en que posiciones se colocaron las y reinas y el nombre del autor "Gian Grobert Mamani Mamani"
frame = tk.Frame(ventana)
frame.grid(row=0, column=8, rowspan=8)
# colocndo los detalles de las posiciones de la reinas
for i in range(8):
    tk.Label(frame, text=f"Reina {i+1} en la posicion: {posiciones[i]}").grid(
        row=i, column=0
    )


frame2 = tk.Frame(ventana)
frame2.grid(row=0, column=8, columnspan=8)
# agregando la foto del autor
imagen_autor = tk.PhotoImage(file="foto.png")
imagen_autor = imagen_autor.subsample(15, 15)
tk.Label(frame2, image=imagen_autor).grid(row=9, column=0)

# colocando el nombre del autor
tk.Label(frame2, text=" Autor:  Gian Grobert Mamani Mamani").grid(row=8, column=0)


ventana.mainloop()
