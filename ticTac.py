from flask import Flask, render_template, request, jsonify
import json
app = Flask(__name__)

@app.route("/")
def starter():
    return render_template('ttt-index.html')

@app.route("/next_move/<board>/<level>")
def next_move(board=["#", "#", "#", "#", "#", "#", "#", "#", "#"], \
    level="difficult"):
    # given the current board retreive the next move.
    # import the library
    import gamePerfect
    # what we get in the board is a string
    # convert it into a list as required 
    # by the python code.
    board = board.split(",")
    # Also get the level.
    level = level
    # Now in our javascript code
    # the blank spaces are represented
    # by zero ('0') and in python by '#'
    # replace the zeros.
    for i,b in enumerate(board):
        if b == '0':
            board[i] = "#"
    gmObj = gamePerfect.TicTacToe()
    # set the board
    gmObj.board = board
    # return computer's step based on
    # the difficulty level chosen
    if level == "difficult":
        step = gmObj.get_next_move('X')
    else:
        step = gmObj.get_next_move_dumb('X')
    return jsonify(result=step[1])

if __name__ == "__main__":
    app.debug=True
    app.run()