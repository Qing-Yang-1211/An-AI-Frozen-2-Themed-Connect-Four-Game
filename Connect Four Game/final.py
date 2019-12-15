import random

# helper functions for winsFor()
def inarow_Neast(ch, r_start, c_start, A, N):
    """
    Starting from (row, col) of (r_start, c_start)
    within the 2d list-of-lists A (array),
    returns True if there are N ch's in a row
    heading east and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nsouth(ch, r_start, c_start, A, N):
    """
    Starting from (row, col) of (r_start, c_start)
    within the 2d list-of-lists A (array),
    returns True if there are N ch's in a row
    heading south and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start + (N-1) > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start+i][c_start] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nnortheast(ch, r_start, c_start, A, N):
    """
    Starting from (row, col) of (r_start, c_start)
    within the 2d list-of-lists A (array),
    returns True if there are N ch's in a row
    heading northeast and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start - (N-1) < 0 or r_start > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start-i][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nsoutheast(ch, r_start, c_start, A, N):
    """
    Starting from (row, col) of (r_start, c_start)
    within the 2d list-of-lists A (array),
    returns True if there are N ch's in a row
    heading southeast and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start + (N-1) > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start+i][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True





class Board:
    """
    A data type representing a Connect-4 board
    with an arbitrary number of rows and columns.
    """

    def __init__(self, width, height):
        """
        Construct objects of type Board, 
        with the given width and height.
        """
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]
        self.checker = "X"

        # We do not need to return anything from a constructor!

    def __repr__(self):
        """
        This method returns a string representation
        for an object of type Board.
        """
        s = ''                          # the string to return
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += '-' * (self.width * 2) + '-\n'   # bottom of the board
        for col in range(self.width):   # column no. labels
            s += ' ' + str(col % 10)

        return s       # the board is complete, return it

    def setBoard(self, moveString):
        """Accepts a string of columns and places
           alternating checkers in those columns,
           starting with 'X'.

           For example, call b.setBoard('012345')
           to see 'X's and 'O's alternate on the
           bottom row, or b.setBoard('000000') to
           see them alternate in the left column.

           moveString must be a string of one-digit integers.
        """
        nextChecker = 'X'   # start by playing 'X'
        for colChar in moveString:
            col = int(colChar)
            if 0 <= col <= self.width:
                self.addMove(col, nextChecker)
            if nextChecker == 'X':
                nextChecker = 'O'
            else:
                nextChecker = 'X'

    def addMove(self, col, ox):
        """
        This method takes two arguments: the first, col, 
        represents the index of the column to which the checker will be added. 
        The second argument, ox, will be a 1-character string representing 
        the checker to add to the board. 
        That is, ox should either be 'X' or 'O'.
        """
        H = self.height
        for row in range(0, H):
            # until the slot is not empty, add ox above it
            if self.data[row][col] != " ":
                self.data[row-1][col] = ox
                return
        
        # add to the bottom row if the column is empty
        self.data[H-1][col] = ox
    
    def clear(self):
        """
        should clear the board that calls it.
        """
        self.data = [[' ']*self.width for row in range(self.height)]

    def allowsMove(self, c):
        """
        This method should return True if the calling object (of type Board) 
        does allow a move into column c. 
        It returns False if column c is not a legal column number for the calling object. 
        It also returns False if column c is full. 
        Thus, this method should check to be sure that 
        c is within the range from 0 to the last column and make sure that there is still room left in the column!
        """
        W = self.width
        D = self.data

        # check if out-of-bound
        if c<0 or c>=W:
            return False
        # check if the column is full
        elif D[0][c] != " ":
            return False
        else:
            return True

    def isFull(self):
        """
        This method should return True if the calling object (of type Board) is completely full of checkers. 
        It should return False otherwise.
        """
        # check if the whole board is full
        for r in self.data :
            for c in r :
                if c == ' ' :
                    return False
        return True

    def delMove(self, c):
        """
        This method should do the opposite of addMove. 
        It should remove the top checker from the column c. 
        If the column is empty, then delMove should do nothing. 
        """
        H = self.height
        for row in range(0, H):
            # look for the first non-empty row
            if self.data[row][c] != " ":
                self.data[row][c] = " "
                return
        # it's empty, just return
        return
    
    def winsFor(self, ox):
        """
        This method's argument ox is a 1-character checker: either 'X' or 'O'. 
        It should return True if there are four checkers of type ox in a row on the board. 
        It should return False othwerwise. 
        Important Note: you need to check whether the player has won horizontally, vertically, or diagonally (and there are two different directions for a diagonal win).
        """
        for i in range(self.height) :
            for j in range(self.width) :
                if inarow_Neast(ox, i, j, self.data, 4) \
                    or inarow_Nsouth(ox, i, j, self.data, 4) \
                    or inarow_Nnortheast(ox, i, j, self.data, 4) \
                    or inarow_Nsoutheast(ox, i, j, self.data, 4):
                    return True
        return False

    def gameOver(self):
            """Returns True if the game is over."""
            if self.isFull() or self.winsFor('X') or self.winsFor('O'):
                return True
            return False

    def colsToWin(self, ox):
        """
        This method should be within the Board class and should take one argument, ox, 
        which will be either the string 'X' or the string 'O' (the two possible checkers in the game).
        Then, the colsToWin method should return the list of columns where ox can move in the next turn 
        in order to win and finish the game. The columns should be in numeric order (if there are more than one). 
        Also, colsToWin should not look ahead more than one turn. 
        """
        possibleCols = []
        W = self.width
        for col in range(0, W):
            if self.allowsMove(col):
                self.addMove(col, ox)
                if self.winsFor(ox) == True:
                    possibleCols += [col]
                self.delMove(col)

        return possibleCols


    def aiMove(self, ox):
        """
        The aiMove method should also be within the Board class and should accept a single argument, ox, which will be either the string 'X' or the string 'O' (the two possible checkers in the game).
        Then, aiMove should return a single integer, which must be a legal column in which to make a move. AND
        If there is a way for ox to win, then aiMove MUST return that move (that column number). It must win when it can. There may be more than one way to win: in this case, any one of those winning column moves may be returned.
        If there is NO way for ox to win, but there IS a way for ox to block the opponent's four-in-a-row, then aiMove MUST return a move that blocks its opponent's four-in-a-row. Again, it should not look more than one move ahead for its opponent. If there are no wins, but multiple ways to block the opponent, then aiMove should return any one of those ways to block the opponent. (Even though the opponent might win in a different way.)
        If there is NO way for ox to win NOR a way for ox to block the opponent from winning, then aiMove should return a move of your (the programmer's) choice—but it must be a legal move. We won't call aiMove when the board is full.
        """
        colsX = self.colsToWin("X")
        colsO = self.colsToWin("O")
        
        if ox == "X":
            
            if colsX == []:
                if colsO != []:
                    return random.choice(colsO)
                else:
                    if self.allowsMove(3):    
                      return 3
                    elif self.allowsMove(2):
                        return 2
                    elif self.allowsMove(4):
                        return 4
                    elif self.allowsMove(1):
                        return 1
                    elif self.allowsMove(5):
                        return 5
                    elif self.allowsMove(0):
                        return 0
                    elif self.allowsMove(6):
                        return 6
            else:
                return random.choice(colsX)
        
        elif ox == "O":
            
            if colsO == []:
                if colsX != []:
                    return random.choice(colsX)
                else:
                    if self.allowsMove(3):    
                      return 3
                    elif self.allowsMove(2):
                        return 2
                    elif self.allowsMove(4):
                        return 4
                    elif self.allowsMove(1):
                        return 1
                    elif self.allowsMove(5):
                        return 5
                    elif self.allowsMove(0):
                        return 0
                    elif self.allowsMove(6):
                        return 6
            else:
                return random.choice(colsO)


    def hostGame(self):
        """
        This method brings everything together into the familiar game. 
        It should host a game of Connect Four, using the methods listed above to do so. 
        In particular, it should alternate turns between 'X' (who will always go first) 
        and 'O' (who will always go second). It should ask the user (with the input function) 
        to select a column number for each move. 
        """
        print ("Welcome to Connect Four!")
        print (self)
        user = input("Choose your weapon: (X or O):")
        if user == "X":
            aiPlayer = "O"
        elif user == "O":
            aiPlayer = "X"
        
        while True:
            users_col = int(input(user + ": Choose a column: "))
            while not self.allowsMove(users_col):
                users_col = int(input(user + ": Choose a column: "))
            self.addMove(users_col, user)
            print(self)

            if self.winsFor(user):
                print("You win--Congratulations!")
                break
            if self.isFull():
                print("It's a tie. Better luck next time!")
                break
            

            ai_col = self.aiMove(aiPlayer)
            while not self.allowsMove(ai_col):
                ai_col = self.aiMove(aiPlayer)
            self.addMove(ai_col, aiPlayer)
            print(self)

            if self.winsFor("O"):
                print("I win--HAHAHAHA!")
                break
            if self.isFull():
                print("It's a tie. Better luck next time!")
                break


    def playGame(self, px, po, ss = False):
        """
        playGame does just that: it calls the nextMove method for two objects of type Player in order to play a game. 
        Those objects are named px and po.
        you should test your Connect Four-playing code in playing games against itself and against a person. 
        That is, if px or po is the string 'human' instead of an object of type Player, 
        then playGame pauses and ask the user to input the next column to move for that player, with error checking just as in hostGame.
        """
        if px=='human' or po=='human':
            s = "Welcome to Connect 4 - Frozen 2!" + "\n"
            s += "Get on a cozy couch and pour youself a cup of hot chocolate." + "\n"
            s += "Watch/Rewatch Frozen 2 while enjoying this game!" + "\n"
            s += "Elsa and Anna find their parents' wrecked ship and a map with a route to Ahtohallan, a mythical river told by their mother to hold all the answers to the past." + "\n"
            s += "Every time Elsa, Anna, and Olaf sing the Ahtohallan song 'All is Found'and call 'Ahtohallan', they will be granted magic power by the nature!" + "\n"
            s += "However, 'Ahtohallan' can only be called once per game. If called twice, you will risk missing a chance to place your checker!" + "\n"
            s += "Now, enter the magic world!"
            print(s)

        # ask player(s) to choose character(s)
        if px=='human':
            choice=input("Player for X please choose your character from:\nelsa, anna, olaf\n")
            if choice.lower()=='elsa':
                checkerx = Elsa('X')
            elif choice.lower()=='anna':
                checkerx = Anna('X')
            elif choice.lower()=='olaf':
                checkerx = Olaf('X')
            elif choice.lower()=='grutor':
                checkerx = Grutor('X')
                print("Just call 'Ahtohallan' whenever grutor wants to win the game!")

        if po=='human':
            choice=input("Player for O please choose your character from:\nelsa, anna, olaf\n")
            if choice.lower()=='elsa':
                checkero = Elsa('O')
            elif choice.lower()=='anna':
                checkero = Anna('O')
            elif choice.lower()=='olaf':
                checkero = Olaf('O')
            elif choice.lower()=='grutor':
                checkero = Grutor('O')
                print("Just call 'Ahtohallan' whenever grutor wants to win the game!")

        nextPlayerToMove = px

        while True:

            # print the current board
            print(self)

            # choose the next move
            if nextPlayerToMove == 'human':
                col = -1
                while not self.allowsMove(col):
                    col = input('Next col for ' + self.checker + ': ')
                    if col=='Ahtohallan':
                        break
                    else:
                        col=int(col)
            else: # it's a computer player
                if ss:
                    scores = nextPlayerToMove.scoresFor(self)
                    print((self.checker + "'s"), 'Scores: ', [int(sc) for sc in scores])
                    print()
                    col = nextPlayerToMove.tiebreakMove(scores)
                else:
                    col = nextPlayerToMove.nextMove(self)

            # add the checker to the board
            flag = False
            while flag == False:
                if col == 'Ahtohallan':
                    if self.checker == 'X':
                        flag = checkerx.Ahtohallan(self)
                    else:
                        flag = checkero.Ahtohallan(self)
                else:
                    self.addMove(col, self.checker)
                    flag = True

            # check if game is over
            if self.winsFor(self.checker):
                print(self)
                print('\n' + self.checker + ' wins! \n\n')
                break
            if self.isFull():
                print(self)
                print('\nThe game is a draw.\n\n')
                break

            # swap players
            if self.checker == 'X':
                self.checker = 'O'
                nextPlayerToMove = po
            else:
                self.checker = 'X'
                nextPlayerToMove = px

        print('Come back 4 more and Merry Christmas!')


class Grutor:
    """ No doubt for grutors' super power cos we LOVE our life-saviors!!! """
    def __init__(self, ox):
        self.ox = ox
        self.Ahto = True

    def __repr__(self):
        s = "Grutor now holds the checker" + self.ox + "\n"
        return s
    
    def Ahtohallan(self, b):
        """ Just call 'Ahtohallan' when grutor wants to win the game! """
        if self.Ahto:
            s = "No doubt for grutors' super power cos we LOVE our life-saviors!!!"
            print(s)
            b.data[5][0] = self.ox
            b.data[5][1] = self.ox
            b.data[5][2] = self.ox
            b.data[5][3] = self.ox
            return True

class Elsa:
    """ Ready to meet our Frozen Queen? """
    def __init__(self, ox):
        self.ox = ox
        self.Ahto = True
    
    def __repr__(self):
        s = "Elsa now holds the checker" + self.ox + "\n"
        s += "Ready to meet our Frozen Queen?" + "\n\n"
        return s
    
    def Ahtohallan(self, b):
        """ When Elsa sings the Ahtohallan song 'All is Found' """
        if self.Ahto:
            s = "Your opponent is frozen by Elsa's power! Poor guy. ;)" + "\n"
            s += "Elsa: Don't even try to move. I can see your eyes rolling." + "\n"
            s += "[pretend to be angry but actually cute.emoji]" + "\n"
            s += "Now, my Majesty, you can replace any one of your opponent's checkers on the board with yours!" + "\n"
            s += "Elsa singing to the opponent: Let it go -- Let it go ~~~"
            print(s)
            delCheckerRow = int(input("Enter the row of the checker that you want to replace: from top(0) to bottom(5)"))
            delCheckerCol = int(input("Enter the column of the checker that you want to replace: from left(0) to right(6)"))
            b.data[delCheckerRow][delCheckerCol] = self.ox 
            print(b)
            print("And make your move, my Majesty!")
            col = int(input("Choose a column:"))
            b.addMove(col, self.ox)
            self.Ahto = False
            return True
        else:
            print("The magic river Ahtohallan can only be reached once per game!")
        

class Anna:
    """ Beware of our naughty gril ;) """
    def __init__(self, ox):
        self.ox = ox
        self.Ahto = True
    
    def __repr__(self):
        s = "Anna now holds the checker" + self.ox + "\n"
        s += "Beware of our naughty gril ;)" + "\n\n"
        return s
    
    def Ahtohallan(self, b):
        """ When Anna sings the Ahtohallan song 'All is Found' """
        if self.Ahto:
            print("It seems that our naughty girl has messed up the checkers in a column...but which column is it? ;)")
            clearCol = int(input("Enter the column that you would like to clear: (0-6)"))
            for col in range(0, 7):
                if col == clearCol:
                    for row in range(0, 6):
                        b.data[row][col] = " "
            self.Ahto = False
            return True
        else:
            print("The magic river Ahtohallan can only be reached once per game!")


class Olaf:
    """ Do you want to build a snowman~~~~ """
    def __init__(self, ox):
        self.ox = ox
        self.Ahto = True
    
    def __repr__(self):
        s = "Olaf now holds the checker" + self.ox + "\n"
        s += "Do you want to build a snowman~~~~" + "\n\n"
        return s
    
    def Ahtohallan(self, b):
        """ When Olaf sings the Ahtohallan song 'All is Found' """
        if self.Ahto:
            s = "Do you want to build a snowman~~~~" + "\n"
            s += "Olaf: Do you know that water has memory?" + "\n"
            s += "It not only brings back memories from Elsa's parents," + "\n"
            s += "but also flashes back the board to what I have remembered - the empty game board!" + "\n"
            s += "SURPRISE"
            print(s)
            b.clear()
            self.Ahto = False
            return True
        else:
            print("The magic river Ahtohallan can only be reached once per game!")

            
class Player:
    """An AI player for Connect Four."""

    def __init__(self, ox, tbt, ply):
        """Construct a player for a given checker, tie-breaking type,
           and ply."""
        self.ox = ox
        self.tbt = tbt
        self.ply = ply

    def __repr__(self):
        """Create a string represenation of the player."""
        s = "Player for " + self.ox + "\n"
        s += "  with tiebreak type: " + self.tbt + "\n"
        s += "  and ply == " + str(self.ply) + "\n\n"
        return s
    
    def oppCh(self):
        """
        This method should return the other kind of checker 
        or playing piece, i.e., the piece being played by 
        self's opponent. In particular, if self is playing 'X', 
        this method returns 'O' and vice-versa.
        """
        if self.ox == "X":
            return "O"
        if self.ox == "O":
            return "X"

    def scoreBoard(self, b):
        """
        This method should return a single float value r
        epresenting the score of the input b, which you 
        may assume will be an object of type Board. 
        This should return 100.0 if the board b is a win for self. 
        It should return 50.0 if it is neither a win nor a loss for self, 
        and it should return 0.0 if it is a loss for self (i.e., the opponent has won).
        """
        # if self wins, the score for self is 100
        if b.winsFor(self.ox):
            return 100.0
         # if self's opponent wins, the score for self is 0
        elif b.winsFor(self.oppCh()):
            return 0.0
        # if self does not win or lose, the score for self is 50
        else:
            return 50.0

    def scoresFor(self, b):
        """
        Its job is to return a list of scores, with the cth score representing the "goodness" of the input board 
        after the player moves to column c. And, "goodness" is measured by what happens in the game after self.ply moves.
        """
        # fisrt set all columns to have a score 50
        scores = [50]*b.width
        
        # iterate through the score list
        for c in range(b.width):
            # if column c is full
            if b.allowsMove(c) == False:
                scores[c] = -1.0
            # if self has won
            elif b.winsFor(self.ox) == True:
                scores[c] == 100
            # if self has lost
            elif b.winsFor(self.oppCh()) == True:
                scores[c] == 0
            # if no move is made
            elif self.ply == 0:
                scores[c] = 50
            # the game isn't over, the code should make a move into the column that is under consideration
            elif self.ply > 0:
                b.addMove(c, self.ox)
                if b.gameOver() == True:
                    scores[c] = 100
                else:
                    # establish the opponent object for testing
                    opponent = Player(self.oppCh(),self.tbt, self.ply-1)
                    # find opponent's max score
                    opponentMax = max(opponent.scoresFor(b))
                    # find self's corresonding score
                    scores[c] = 100 - opponentMax
                
                b.delMove(c)
        return scores

    def tiebreakMove(self, scores):
        """
        This method takes in scores, which will be a nonempty list of floating-point numbers. 
        If there is only one highest score in that scores list, this method should return its COLUMN number. 
        Note that the column number is the same as the index into the list scores. 
        If there is more than one highest score because of a tie, this method should return 
        the COLUMN number of the highest score appropriate to the player's tiebreaking type.
        Thus, if the tiebreaking type is 'LEFT', then tiebreakMove should return 
        the column of the leftmost highest score (not the score itself).
        And if the tiebreaking type is 'RANDOM', then tiebreakMove should return 
        the column of the a randomly-chosen highest score (yet again, not the score itself).
        """
        # keep a list of the column numbers for the max scores
        listOfMaxScore = []
        # find the max score value in scoures
        maxScore = max(scores)
        # iterate through scores, add the column number if equals max score
        for i in range(len(scores)):
            if scores[i] == maxScore:
                listOfMaxScore += [i]
        
        # break ties by choosing the left-most column no. with max score
        if self.tbt == "LEFT":
            return listOfMaxScore[0]
        # break ties by choosing the right-most column no. with max score
        elif self.tbt == "RIGHT":
            return listOfMaxScore[-1]
        # break ties by choosing randomly a column no. with max score
        elif self.tbt == "RANDOM":
            return random.choice(listOfMaxScore)

    def nextMove(self, b):
        """
        This method accepts b, an object of type Board, and returns an integer—namely, 
        the column number that the calling object (of class Player) chooses to move to. 
        This is the primary interface to Player, but it is really just a "wrapper" for 
        the heavy lifting done by the other methods, particularly scoresFor. 
        Thus, nextMove should use scoresFor and tiebreakMove to return its move.
        """
        scores = self.scoresFor(b)
        return self.tiebreakMove(scores)






















