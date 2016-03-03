BSTARTROW = 1
WSTARTROW = 3
WHITE = 'w'
BLACK = 'b'
EMPTY = '-'
WIDTH = 3
HEIGHT = 6

        
class pos:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return "("+str(self.x)+","+str(self.y)+")"

class Pawn:
    def __init__(self,x,y,color):
        self.pos = pos(x,y)
        self.color = color
    def __repr__(self):
        return str(self.pos)+str(self.color)
    def isWhite(self):
        return self.color==WHITE
    def move(self,pos):
        self.pos = pos
        
#INCOMPLETE FUNCTIONS
"""
WINFOR
OPENMOVES
SUCCESSORS

"""
class board:
    # Represent the gamestate pawned
    #  Minimax assumes objects that respond to the following methods:
    #     __str__(): return a unique string describing the state of the game (for use in hash table)
    #     isTerminal(): checks if the game is at a terminal state
    #     successors(): returns a list of all legal game states that extend this one by one move
    #                   in this version, the list consists of a move,state pair
    #     isMinNode(): returns True if the node represents a state in which Min is to move
    #     isMaxNode(): returns True if the node represents a state in which Max is to move
    def __init__(self,state,player=WHITE):
        """
        Create a new object
        :param state: a description of the board for the current state
        :param player: whose turn it isto play in the current state
        :return:
        """
        if(state==None):
            self.gameState = dict()
            for x in range(0,WIDTH):
                for y in range(0,HEIGHT):
                    self.gameState[x,y] = EMPTY
            for x in range(0,WIDTH):
                self.setNode(x,BSTARTROW,BLACK)#Blacks starting row
                self.setNode(x,WSTARTROW,WHITE)#Whites starting row
                #whites.append(Board.pawn(Board.pos(x,WSTARTROW),WHITE))
                #blacks.append(Board.pawn(Board.pos(x,BSTARTROW),BLACK))
        else:
            self.gameState = state
        
        self.whoseTurn = player
        self.cachedWin = False  # set to True in winFor() if
        self.cachedWinner = None

    
    def __repr__(self):
        """
        Used for debugging and displaying in user friendly manner.
        :return: User friendly string of the current board state.
        """
        s = ""
        for y in range(0,HEIGHT):
            temp=""
            for x in range(0,WIDTH):
                temp = temp+ str(self.gameState[x,y])
            s += temp+"\n"
        return s

    def __str__(self):
        """
        Translate the board description into a string.  Used for a hash table.
        :return: A string that describes the board in the current state.
        """
        s=""
        for x in range(0,WIDTH):
            for y in range(0,HEIGHT):
                s+=self.gameState[x,y]
        return s

    def isMinNode(self):
        return self.whoseTurn==BLACK
        
    def isMaxNode(self):
        return self.whoseTurn==WHITE
   
        
        
    def winFor(self,player):
        """
        Check if it's a win for player.
        :param player: either BLACK or WHITE
        :return: True if player has a pawn on its end row
        """
        if(self.cachedWin == False):
            won = False;
            if(player==WHITE):
                for x in range(0,WIDTH):
                    if(self.gameState[x,0]==WHITE):
                        won = True
                
            elif(player==BLACK):
                for x in range(0,WIDTH):
                    if(self.gameState[x,HEIGHT-1]==BLACK):
                        won = True
            #IF there are no available moves for both players
                #check who has the most pawns
            if(won):
                self.cachedWin = True
                self.cachedWinner = player
                return true
            else:
                return false
        else:
            return player == self.cachedWinner
        
    #Used to decide who to win for
    def utility(self):
        """
        :return: 1 if win for WHITE, -1 for win for BLACK, 0 for draw
        """
        if(self.winFor(WHITE)):
            return 1
        elif(self.winFor(BLACK)):
            return -1
        else:
            return 0
    
    def togglePlayer(self,p):
        """
        :param p: either 'b' or 'w'
        :return: other players symbol
        else false
        """
        if(p==WHITE):
            return BLACK
        else:
            return WHITE
    
    def intPlayer(self,p):
        """ *** needed for move ***
        :param p:  a game state node with stored game state
        :return: a list of move,state pairs that are the next possible states
        """
        if(p==WHITE):
            return -1
        else:
            return 1
            
    def openMoves(self):
        """
        
        """
        for x in range(0,WIDTH):
            for y in range(0,HEIGHT):
                if(hasTurnPawn(x,y)):
                    x = x
    
    
    
    def hasTurnPawn(self,x,y):
        """
        :param x: x coordinate on board
        :param y: y coordinate on board
        :return: true if the location given has a color equal to whoseTurn it is
        else false
        """
        return self.gameState[x,y]==whoseTurn
        
    
    
    
    
    #MOVEMENTS
    #Moves forward relative to player
    #Returns a gameState with the change
    def move(self,p,intMove):
        """
        Create a new board state with the given move
        :param p: The pawn,of type pawn, to move
        :param move: What type of move it was
                     0: move forward relative to player
                     -1: attack left relative to player
                     1: attack right relative to player
        :return: a pawn,move pair, gs the state is a copy of the current state with the additional move included
                 a pawn contains the position it was at and its color
                 move is an int with the type of move it did
        """
        gs = self.gameState.copy()
        if(intMove==0):#
            gs[p.pos.x,p.pos.y+self.intPlayer(p.color)] = p.color
        elif(intMove==-1):
            gs[p.pos.x+self.intPlayer(p.color),p.pos.y+self.intPlayer(p.color)] = p.color
        elif(intMove== 1):
            gs[p.pos.x-self.intPlayer(p.color),p.pos.y+self.intPlayer(p.color)] = p.color

        gs[p.pos.x,p.pos.y] = '-'
        return (p,intMove),gs






