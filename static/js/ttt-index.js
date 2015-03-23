// Initialize some Global Variables
var gameGrid = [[0,0,0],[0,0,0],[0,0,0]];
var highPriWin = [[0,"X","X"],["X",0,"X"],["X","X",0]];
var highPriBlock = [[0,"O","O"],["O",0,"O"],["O","O",0]];
var gameState = 0;
var gameAttempts = 0;
var drawGames = -1;
var youWon = -1;
var iWon = -1;

var xImg = "static/imgs/cross-sm.png";
var oImg = "static/imgs/circle-tick-sm.png";
var blankImg = "static/imgs/blank-dark.png";

//returns the x Index of the gameGrid 
function xIndex(squareDiv) {
    var x = squareDiv.split("_");
    var i = parseInt(x[1]);
    return i;
}

//returns the Y index of the gameGrid
function yIndex(squareDiv) {
    var x = squareDiv.split("_");
    var i = parseInt(x[2]);
    return i;
}

// Get the next move using the minimax algo from Python
function getNextMove(){
    // get the board as array of strings
    var boardArr = gameGrid[0].concat(gameGrid[1],gameGrid[2]);
    // Get difficulty level
    if (document.getElementById('easyLev').checked) {
          diffLevel = document.getElementById('easyLev').value;
    }else{
        diffLevel = document.getElementById('dfcltLev').value;
    }
    // Get the new position from python script
    $(function( data ) {
          $.getJSON("/next_move/"+boardArr.toString()+"/"+diffLevel, {}, function(data) {
              placeMnmxLoc(data.result);
          });
    });

}

// Place an 'X' in the location returned by minimax algo
function placeMnmxLoc(loc) {
    // check if there is a winner
    checkWinner();
    // get the x,y coords from loc
    var x = Math.floor(loc/3);
    var y = loc % 3;
    gameGrid[x][y] = "X";
    var divName = "square_"+x+"_"+y;
    console.log(divName);
    $("#"+divName).children("img").attr('src',xImg);
    document.getElementById(divName).classList.remove("blank");
    document.getElementById(divName).classList.add("X");
    // check if there is a winner
    checkWinner();
}


function checkWinner() {
    //check for draw
    var fullGridArr = gameGrid[0].concat(gameGrid[1],gameGrid[2]);

    if (fullGridArr.indexOf(0) == -1) {
        gameState = 1;
        $('#drawModal').modal('show');
    }
    //check for win
    //initialize diag counters 
    var diag1X = 0;
    var diag1O = 0;
    var diag2X = 0;
    var diag2O = 0;
    // row and column checks
    for (var i=0; i<3; i++){
        //counter initialize
        var rowX = 0;
        var rowO = 0;
        var colX = 0;       
        var colO = 0;       
        //check diagonals
        if (gameGrid[i][i] == "O") {
            diag1X++;           
        } else if (gameGrid[i][i] == "X") {
            diag1O++;
        }   if (gameGrid[i][(2-i)] == "O") {
            diag2X++;
        }   else if (gameGrid[i][(2-i)] == "X") {
            diag2O++;
        } if (i == 2) {                 
            if (diag1X == 3 || diag2X == 3) {
                gameState = 1;
                $('#winModal').modal('show');
            }
            else if (diag1O == 3 || diag2O == 3) {
                gameState = 1;
                $('#loseModal').modal('show');
            }
        }
        // count and check rows and columns for win
        for (var j=0; j<3; j++) {
            if (gameGrid[i][j] == "O") {
                rowX++;             
            }   else if (gameGrid[i][j] == "X") {
                rowO++;
            }   if (gameGrid[j][i] == "O") {
                colX++;             
            }   else if (gameGrid[j][i] == "X") {
                colO++;                     
            } if (j==2) {                   
                if (rowX == 3 || colX == 3) {
                    gameState = 1;
                    $('#winModal').modal('show');
                } else if (rowO == 3 || colO == 3) {
                    gameState = 1;
                    $('#loseModal').modal('show');
                }
            }
        }   
    }
}

//creates 3 rows of 3 divs, names and applies classes
function createGame() {
    for (var i=0; i<3; i++) {
        var rowDiv = document.createElement("div");
        rowDiv.classList.add("row");
        
        for (var j=0; j<3; j++) {
            var gridDiv = document.createElement("div");
            gridDiv.id = "square_" + i +"_"+ j;
            gridDiv.classList.add("col-lg-4");
            gridDiv.classList.add("col-sm-4");
            gridDiv.classList.add("col-4");
            gridDiv.classList.add("blank");
            $('<img/>').attr('src',blankImg).addClass('img-responsive').appendTo(gridDiv);
            rowDiv.appendChild(gridDiv);
        }
        
        document.getElementById("gamezone").appendChild(rowDiv);
        if (i<2) {
            $("<br>").appendTo(document.getElementById("gamezone"));
        }
    }
}

//resets gameGrid and gameState, clears gamezone, and calls createGame
function resetGame(){
    gameGrid = [[0,0,0],[0,0,0],[0,0,0]];
    gameState = 0;
    document.getElementById("gamezone").innerHTML = '';
    createGame();
}

// increments game attempt counter, resets if given "reset" as argument
function countrIncrmt(condition){
  if (condition == "reset"){
        gameAttempts = 1;
    }   else {
        gameAttempts++;
    }
    var counters = document.getElementsByClassName("counter")
    for (var i=0; i<counters.length; i++){
        var count = counters[i];
        count.innerHTML = gameAttempts;
    }
}

// increment drawn games counter, resets if given "reset" as argument
function drawIncrmt(condition){
  if (condition == "reset"){
        drawGames = 0;
    }   else {
        drawGames++;
    }
    var counters = document.getElementsByClassName("drawCounter")
    for (var i=0; i<counters.length; i++){
        var count = counters[i];
        count.innerHTML = drawGames;
    }
}

// increment you won counter, resets if given "reset" as argument
function youWonIncrmt(condition){
  if (condition == "reset"){
        youWon = 0;
    }   else {
        youWon++;
    }
    var counters = document.getElementsByClassName("meCounter")
    for (var i=0; i<counters.length; i++){
        var count = counters[i];
        count.innerHTML = youWon;
    }
}

// increment i won counter, resets if given "reset" as argument
function iWonIncrmt(condition){
  if (condition == "reset"){
        iWon = 0;
    }   else {
        iWon++;
    }
    var counters = document.getElementsByClassName("youCounter")
    for (var i=0; i<counters.length; i++){
        var count = counters[i];
        count.innerHTML = iWon;
    }
}

//jQuery to create game on page load and capture clicks
$(document).ready(function(){
    createGame();   
    countrIncrmt();
    drawIncrmt();
    iWonIncrmt();
    youWonIncrmt();

    $(document).on("mousedown", ".blank", function(){
        if ($(this).hasClass("blank")){
            if (gameState == 0){
                this.classList.remove("blank");
                this.classList.add("O");
                $(this).children("img").attr('src',oImg);
                gameGrid[xIndex(this.id)][yIndex(this.id)] = "O";
                checkWinner();
                if (gameState == 0) {
                    getNextMove();
                    checkWinner();
                }
            }
        }
    })
    $("#drawModal").on('hide.bs.modal', function(){
            countrIncrmt();
            drawIncrmt();
    });
    $("#winModal").on('hide.bs.modal', function(){
        countrIncrmt();
        iWonIncrmt();
    });
    $("#loseModal").on('hide.bs.modal', function(){
        countrIncrmt();
        youWonIncrmt();
    });

    $(".btn-reset").click(function(){
        resetGame();
    })

    $(".btn-reset-user").click(function(){
        countrIncrmt();
        resetGame();
    })
});