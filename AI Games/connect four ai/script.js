
const ROWS = 6;
const COLS = 7;
let board = []; 
let currentPlayer = "red"; 
let gameOver = false;
let userScore = 0;
let aiScore = 0;


const boardEl = document.getElementById("board");
const statusEl = document.getElementById("status");
const userScoreEl = document.getElementById("userScore");
const aiScoreEl = document.getElementById("aiScore");


function initBoard() {
  board = [];
  boardEl.innerHTML = ""; 

  for (let r = 0; r < ROWS; r++) {
    board[r] = [];
    for (let c = 0; c < COLS; c++) {
      const cell = document.createElement("div");
      cell.classList.add("cell");
      cell.dataset.row = r;
      cell.dataset.col = c;
      boardEl.appendChild(cell);
      board[r][c] = null; 
    }
  }
}


function restartGame() {
  gameOver = false;
  currentPlayer = "red";
  statusEl.textContent = "Your Turn (🔴)";
  initBoard();
}


boardEl.addEventListener("click", (e) => {
  if (gameOver || currentPlayer !== "red") return;
  const col = parseInt(e.target.dataset.col); 
  if (isNaN(col)) return;

  for (let row = ROWS - 1; row >= 0; row--) {
    if (board[row][col] === null) {
      board[row][col] = "red";
      const cell = getCell(row, col);
      cell.classList.add("red");

      if (checkWinner(row, col)) {
        statusEl.textContent = "You Win! 🎉";
        gameOver = true;
        userScore++;
        userScoreEl.textContent = userScore;
        return;
      }
      currentPlayer = "yellow";
      statusEl.textContent = "Computer's Turn (🟡)";
      setTimeout(computerMove, 500);
      break;
    }
  }
});


function getCell(row, col) {
  return document.querySelector(`.cell[data-row='${row}'][data-col='${col}']`);
}


function computerMove() {
  if (gameOver) return;

  const validCols = [];
  for (let c = 0; c < COLS; c++) {
    for (let r = ROWS - 1; r >= 0; r--) {
      if (board[r][c] === null) {
        validCols.push({ row: r, col: c });
        break;
      }
    }
  }

  if (validCols.length === 0) {
    statusEl.textContent = "It's a Tie!";
    gameOver = true;
    return;
  }

  const move = validCols[Math.floor(Math.random() * validCols.length)];
  board[move.row][move.col] = "yellow";
  const cell = getCell(move.row, move.col);
  cell.classList.add("yellow");

  if (checkWinner(move.row, move.col)) {
    statusEl.textContent = "Computer Wins! 😭";
    gameOver = true;
    aiScore++;
    aiScoreEl.textContent = aiScore;
  } else {
    currentPlayer = "red";
    statusEl.textContent = "Your Turn (🔴)";
  }
}


function checkWinner(r, c) {
  const directions = [ [1, 0], [0, 1], [1, 1], [1, -1] ]; 
  for (let [dr, dc] of directions) {
    let count = 1;
    count += countDirection(r, c, dr, dc);
    count += countDirection(r, c, -dr, -dc);
    if (count >= 4) return true;
  }
  return false;
}


function countDirection(r, c, dr, dc) {
  let count = 0;
  let color = board[r][c];

  for (let i = 1; i < 4; i++) {
    let nr = r + dr * i;
    let nc = c + dc * i;
    if (nr < 0 || nr >= ROWS || nc < 0 || nc >= COLS) break;
    if (board[nr][nc] === color) count++;
    else break;
  }

  return count;
}


initBoard();