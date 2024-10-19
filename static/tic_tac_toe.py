import tkinter as tk
from tkinter import messagebox

# Función para verificar si alguien ha ganado
def check_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Filas
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columnas
                      (0, 4, 8), (2, 4, 6)]  # Diagonales
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == player:
            return True
    return False

# Función para verificar si hay un empate
def check_draw(board):
    return all(cell != "" for cell in board)

# Algoritmo Minimax para la IA
def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 1  # IA gana
    elif check_winner(board, "X"):
        return -1  # Jugador gana
    elif check_draw(board):
        return 0  # Empate

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == "":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = ""
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == "":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = ""
                best_score = min(score, best_score)
        return best_score

# Función para que la IA haga su movimiento
def ia_move():
    best_score = -float('inf')
    best_move = 0
    for i in range(9):
        if board[i] == "":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = ""
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = "O"
    buttons[best_move].config(text="O")
    if check_winner(board, "O"):
        messagebox.showinfo("Fin del juego", "¡La IA ha ganado!")
        reset_game()
    elif check_draw(board):
        messagebox.showinfo("Fin del juego", "¡Es un empate!")
        reset_game()

# Función para manejar el clic del jugador
def player_move(index):
    if board[index] == "" and not check_winner(board, "O"):
        board[index] = "X"
        buttons[index].config(text="X")
        if check_winner(board, "X"):
            messagebox.showinfo("Fin del juego", "¡Has ganado!")
            reset_game()
        elif check_draw(board):
            messagebox.showinfo("Fin del juego", "¡Es un empate!")
            reset_game()
        else:
            ia_move()

# Función para reiniciar el juego
def reset_game():
    global board
    board = [""] * 9
    for button in buttons:
        button.config(text="")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Tic-Tac-Toe con IA (Minimax)")

board = [""] * 9
buttons = []

# Crear los botones de la cuadrícula del tablero
for i in range(9):
    button = tk.Button(root, text="", font=("Arial", 40), width=5, height=2,
                       command=lambda i=i: player_move(i))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Iniciar el bucle principal de Tkinter
root.mainloop()
