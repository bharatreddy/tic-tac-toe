class TicTacToe(object):
    """
    A class for playing TicTacToe using 
    the Minimax algorithm.
    """
    def __init__(self):
        """
            set up the board. We'll use an array of length 9 (3x3)
            to represent the board. The layout is shown below
            0 | 1 | 2
            3 | 4 | 5
            6 | 7 | 8
            Also we'll use 'X', 'O' to represent the players
            empty slots will be represented using #.
        """
        self.board = [ '#' for i in range(9) ]#''.join( [ '#' for i in range(9) ] )

    def check_winner(self):
        """
            Function to check if there is winner in the board.
            Check the comments in the __init__ function for 
            a layout/description of the board.
            Check the rows for winners.
        """
        for i in range(3):
            if ( (self.board[i*3] == self.board[i*3+1]) and \
                (self.board[i*3] ==  self.board[i*3+2]) and \
                self.board[i*3] != '#' ): 
                return True
        # Check the columns for winners.
        for i in range(3):
           if ( (self.board[i] == self.board[i+3]) and \
                (self.board[i] ==  self.board[i+6]) and \
                self.board[i] != '#' ):
                return True
        # Check the diagonal elements
        # There are two possibilities elements 0, 4 and 8 or 2, 4 and 6.
        if ( self.board[0] == self.board[4] and \
            self.board[4] == self.board[8] and self.board[4] != '#' ):
            return  True
        if ( self.board[2] == self.board[4] and \
            self.board[4] == self.board[6] and self.board[4] != '#' ):
            return  True
        return False

    def get_winner(self):
        """
            Function to check and see who won the game.
        """
        if not self.check_winner():
            print "No Winner found"
            return None
        for i in range(3):
            if ( (self.board[i*3] == self.board[i*3+1]) and \
                (self.board[i*3] ==  self.board[i*3+2]) and \
                self.board[i*3] != '#' ):
                return self.board[i*3]
        # Check the columns for winners.
        for i in range(3):
           if ( (self.board[i] == self.board[i+3]) and \
                (self.board[i] ==  self.board[i+6]) and \
                self.board[i] != '#' ):
                return self.board[i]
        # Check the diagonal elements
        # There are two possibilities elements 0, 4 and 8 or 2, 4 and 6.
        if ( self.board[0] == self.board[4] and \
            self.board[4] == self.board[8] and self.board[4] != '#' ):
            return  self.board[4]
        if ( self.board[2] == self.board[4] and \
            self.board[4] == self.board[6] and self.board[4] != '#' ):
            return  self.board[4]
        return None

    def check_draw(self):
        """
            Function to check if the game ended in a draw.
        """
        if '#' in self.board:
            return False
        if self.check_winner():
            return False
        return True

    def get_next_move(self,currPlayer):
        """
            Function to calculate the next move
            using minimax algorithm. 
            Note : This is a recursive algo and a knowledge of
                the minimax algorithm is required to understand this.
            Input(s) : currPlayer - current player ('X' or 'O')
            Output(s) : (score, nextPos)
                         (1) score --> +10 if 'X' is winning, 
                           0 if draw and -10 if 'O' is winning
                         (2) nextPos --> Position for next move.
        """
        # Verify the inputs before we begin
        assert( currPlayer == 'X' or currPlayer == 'O' )            
        # If this is the first step return the center position by
        # default, otherwise the calculation takes a lot of time.
        if len( set( self.board ) ) == 1:
            return (0,4)
        # set the next player
        if currPlayer == 'X':
            nextPlayer = 'O'
        else:
            nextPlayer = 'X'
        # check for a winner in the current step
        if self.check_winner():
            if currPlayer == 'X':
                return (-10,-1)
            else:
                return (10,-1)
        # Check for a draw in the current step
        if self.check_draw():
            return (0,-1)
        # have a list to keep track of the results.
        resList = []
        # store the location of empty spots in the board
        emptySpots = []
        for ix,brd in enumerate( self.board ):
            if brd == '#':
                emptySpots.append( ix )
        # Now here is the main minimax part.
        for es in emptySpots:
            self.board[es] = currPlayer
            # Recurse and get a final state for the current move
            tmpScore, tmpMove = self.get_next_move( nextPlayer )
            resList.append( tmpScore )
            self.board[es] = '#'
        # Return the score and move depending on the currPlayer
        if currPlayer == 'X':
            maxScore = max( resList )
            return ( maxScore, emptySpots[ resList.index( maxScore ) ] )
        else:
            minScore = min( resList )
            return ( minScore, emptySpots[ resList.index( minScore ) ] )


    def get_next_move_dumb(self,currPlayer):
        """
            Function to calculate the next move using 
            minimax algorithm. However, we make the  algo
            a little dumb by making some moves random. We
            start in a simple way by making 50 percent
            of the moves random.
            Note : This is a recursive algo and a knowledge of
                the minimax algorithm is required to understand this.
            Input(s) : currPlayer - current player ('X' or 'O')
            Output(s) : (score, nextPos)
                         (1) score --> +10 if 'X' is winning, 
                           0 if draw and -10 if 'O' is winning
                         (2) nextPos --> Position for next move.
        """
        # get a random number
        import random
        currRandom = random.uniform( 0., 1. )
        # Verify the inputs before we begin
        assert( currPlayer == 'X' or currPlayer == 'O' )            
        # If this is the first step return the center position by
        # default, otherwise the calculation takes a lot of time.
        if len( set( self.board ) ) == 1:
            return (0,4)
        # set the next player
        if currPlayer == 'X':
            nextPlayer = 'O'
        else:
            nextPlayer = 'X'
        # check for a winner in the current step
        if self.check_winner():
            if currPlayer == 'X':
                return (-10,-1)
            else:
                return (10,-1)
        # Check for a draw in the current step
        if self.check_draw():
            return (0,-1)
        # have a list to keep track of the results.
        resList = []
        # store the location of empty spots in the board
        emptySpots = []
        for ix,brd in enumerate( self.board ):
            if brd == '#':
                emptySpots.append( ix )
        # if the random number is less than .5
        # we use minimax algo else we generate 
        # a random move.
        if currRandom <= 0.5: 
            # Now here is the main minimax part.
            for es in emptySpots:
                self.board[es] = currPlayer
                # Recurse and get a final state for the current move
                tmpScore, tmpMove = self.get_next_move( nextPlayer )
                resList.append( tmpScore )
                self.board[es] = '#'
            # Return the score and move depending on the currPlayer
            if currPlayer == 'X':
                maxScore = max( resList )
                return ( maxScore, emptySpots[ resList.index( maxScore ) ] )
            else:
                minScore = min( resList )
                return ( minScore, emptySpots[ resList.index( minScore ) ] )
        else:
            # return a random empty spot
            return ( 0, emptySpots[random.randint(0,len(emptySpots)-1)] )