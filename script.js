const boardElement = document.getElementById('board');
let board = ["", "", "", "", "", "", "", "", ""];
let currentPlayer = "X";

// Crear el tablero HTML
for (let i = 0; i < 9; i++) {
    const cell = document.createElement('div');
    cell.classList.add('cell');
    cell.addEventListener('click', () => playerMove(i), { once: true });
    boardElement.appendChild(cell);
}

function playerMove(index) {
    if (board[index] === "") {
        board[index] = "X";
        updateBoard();
        if (checkWinner("X")) {
            alert("¡Has ganado!");
            resetGame();
        } else if (isDraw()) {
            alert("¡Es un empate!");
            resetGame();
        } else {
            aiMove();
        }
    }
}

function aiMove() {
    const bestMove = minimax(board, true).index;
    board[bestMove] = "O";
    updateBoard();
    if (checkWinner("O")) {
        alert("¡La IA ha ganado!");
        resetGame();
    } else if (isDraw()) {
        alert("¡Es un empate!");
        resetGame();
    }
}

function minimax(newBoard, isMaximizing) {
    // Implementar lógica Minimax aquí
    return { index: newBoard.findIndex(cell => cell === "") };
}

function checkWinner(player) {
    const winPatterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ];
    return winPatterns.some(pattern => 
        pattern.every(index => board[index] === player)
    );
}

function isDraw() {
    return board.every(cell => cell !== "");
}

function resetGame() {
    board.fill("");
    document.querySelectorAll('.cell').forEach(cell => cell.textContent = "");
}

function updateBoard() {
    const cells = document.querySelectorAll('.cell');
    board.forEach((mark, index) => {
        cells[index].textContent = mark;
    });
}
