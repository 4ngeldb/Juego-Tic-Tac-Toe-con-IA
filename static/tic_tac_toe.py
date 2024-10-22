import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("TIC TAC TOE")
        self.root.configure(bg='lightgreen')
        
        # Variables de juego
        self.jugador_actual = "X"
        self.tablero = [None] * 9
        self.puntaje_jugador1 = 0
        self.puntaje_jugador2 = 0
        
        # Diseño de la interfaz
        self.crear_widgets()

    def crear_widgets(self):
        # Título
        self.titulo_label = tk.Label(self.root, text="TIC - TAC - TOE", font='Arial 24 bold', bg='lightgreen', fg='blue')
        self.titulo_label.pack(pady=10)

        # Tablero
        self.botones = []
        marco = tk.Frame(self.root)
        marco.pack()

        for i in range(9):
            boton = tk.Button(marco, text='', font='Arial 20 bold', width=5, height=2,
                              bg='yellow', command=lambda i=i: self.manejar_click(i))
            boton.grid(row=i // 3, column=i % 3)
            self.botones.append(boton)

        # Estado
        self.estado_label = tk.Label(self.root, text=f"Jugador activo: {self.jugador_actual}", font='Arial 15', bg='lightgreen')
        self.estado_label.pack(pady=10)

        # Puntajes
        self.puntaje_label = tk.Label(self.root, text=f"Puntaje:\nJugador1 (X): {self.puntaje_jugador1}\nJugador2 (O): {self.puntaje_jugador2}", font='Arial 15', bg='lightgreen')
        self.puntaje_label.pack(pady=10)

        # Botón de reinicio
        self.boton_reiniciar = tk.Button(self.root, text="REINICIAR JUEGO", font='Arial 15', command=self.reiniciar_juego, bg='orange')
        self.boton_reiniciar.pack(pady=10)

    def manejar_click(self, i):
        if self.tablero[i] is None and not self.calcular_ganador():
            self.tablero[i] = self.jugador_actual
            self.botones[i].config(text=self.jugador_actual, bg='lightblue')
            ganador = self.calcular_ganador()
            if ganador:
                self.actualizar_puntaje(ganador)
                self.mostrar_ganador(ganador)
            else:
                self.jugador_actual = "O"
                self.estado_label.config(text='Jugador activo: O (IA)')
                self.movimiento_ia()

    def movimiento_ia(self):
        mejor_movimiento = self.minimax(self.tablero, "O")["index"]
        self.tablero[mejor_movimiento] = "O"
        self.botones[mejor_movimiento].config(text="O", bg='lightblue')
        ganador = self.calcular_ganador()
        if ganador:
            self.actualizar_puntaje(ganador)
            self.mostrar_ganador(ganador)
        else:
            self.jugador_actual = "X"
            self.estado_label.config(text='Jugador activo: X')

    def minimax(self, tablero, jugador):
        ganador = self.calcular_ganador()
        if ganador:
            return {"score": 1 if ganador == "O" else -1 if ganador == "X" else 0}

        movimientos = []
        for i in range(9):
            if tablero[i] is None:
                tablero[i] = jugador
                resultado = self.minimax(tablero, "X" if jugador == "O" else "O")
                movimientos.append({"index": i, "score": resultado["score"]})
                tablero[i] = None

        mejor_movimiento = None
        if jugador == "O":
            mejor_puntaje = float("-inf")
            for movimiento in movimientos:
                if movimiento["score"] > mejor_puntaje:
                    mejor_puntaje = movimiento["score"]
                    mejor_movimiento = movimiento
        else:
            mejor_puntaje = float("inf")
            for movimiento in movimientos:
                if movimiento["score"] < mejor_puntaje:
                    mejor_puntaje = movimiento["score"]
                    mejor_movimiento = movimiento

        return mejor_movimiento if mejor_movimiento is not None else {"index": -1, "score": 0}

    def calcular_ganador(self):
        lineas = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]
        for linea in lineas:
            a, b, c = linea
            if self.tablero[a] and self.tablero[a] == self.tablero[b] == self.tablero[c]:
                return self.tablero[a]
        # Verificar empate
        if all(x is not None for x in self.tablero):
            return "Empate"
        return None

    def mostrar_ganador(self, ganador):
        if ganador == "X":
            messagebox.showinfo("Fin del Juego", "¡Jugador X gana!")
        elif ganador == "O":
            messagebox.showinfo("Fin del Juego", "¡Jugador O gana!")
        else:
            messagebox.showinfo("Fin del Juego", "¡Es un empate!")

        self.reiniciar_juego()

    def actualizar_puntaje(self, ganador):
        if ganador == "X":
            self.puntaje_jugador1 += 1
        elif ganador == "O":
            self.puntaje_jugador2 += 1

        self.puntaje_label.config(text=f"Puntaje:\nJugador1 (X): {self.puntaje_jugador1}\nJugador2 (O): {self.puntaje_jugador2}")

    def reiniciar_juego(self):
        self.jugador_actual = "X"
        self.tablero = [None] * 9
        for boton in self.botones:
            boton.config(text='', bg='yellow')
        self.estado_label.config(text="Jugador activo: X")

if __name__ == "__main__":
    root = tk.Tk()
    juego = TicTacToe(root)
    root.mainloop()
