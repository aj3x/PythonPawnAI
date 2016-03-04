#CONSTANTS
BSTARTROW = 1
WSTARTROW = 3
WHITE = 'w'
BLACK = 'b'
EMPTY = '-'
WIDTH = 3
HEIGHT = 6

        
class pos:
    # Represent the gameState for tic tac toe.
    #  Minimax assumes objects that respond to the following methods:
    #     __str__(): return a unique string describing the state of the game (for use in hash table)
    #     isTerminal(): checks if the game is at a terminal state
    #     successors(): returns a list of all legal game states that extend this one by one move
    #                   in this version, the list consists of a move,state pair
    #     isMinNode(): returns True if the node represents a state in which Min is to move
    #     isMaxNode(): returns True if the node represents a state in which Max is to move
    def __init__(self,x,y):
        """
        Create a new position.
        :param x: an x position.
        :param y: a y position.
        :return:
        """
        self.x = x
        self.y = y
    
    def __repr__(self):
        """
        Display position in user friendly manner.
        :return: User friendly representation.
        """
        return "("+str(self.x)+","+str(self.y)+")"
    
    def get(self):
        """
        Returns a tuple of position in (x,y) form.
        :return: Position in form of a tuple (x,y).
        """
        return (self.x,self.y);

class Pawn:
    def __init__(self,x,y,color):
        """
        
        """
        self.pos = pos(x,y)
        self.color = color
    
    
    def __repr__(self):
        """
        Displays a string in user friendly manner.
        :return: User friendly string representation.
        """
        return "("+str(self.pos)+","+str(self.color)+")"
        
        
    def isColor(self,color):
        """
        Compares color to pawn color, returns true if they are the same.
        :param color: Color either BLACK or WHITE to compare pawn to.
        :return: True if the pawn color and color are the same.
        """
        return self.color==color
    def move(self,x,y):
        """
        Sets the position of the pawn
        
        """
        self.pos.x = x
        self.pos.y = y
   


   
#INCOMPLETE FUNCTIONS
"""
WINFOR
OPENMOVES
SUCCESSORS

"""
class board:
    # Represent the gameState pawned
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
                self.gameState[x,BSTARTROW] = BLACK#Blacks starting row
                self.gameState[x,WSTARTROW] = WHITE#Whites starting row
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

    
    def getPawn(self,x,y):
        """
        Gives a pawn on the position x,y or returns empty if none exists
        :param x: x coordinate on board
        :param y: y coordinate on board
        :return: Pawn on the coordinate x,y or None if EMPTY
        """
        if(self.gameState[x,y]==EMPTY):
            return
        return Pawn(x,y,self.gameState[x,y])
    
    
    
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
            
    
    
    

    
    
    #MOVEMENTS
    def inBounds(self,pos):
        """
        Tells if a position is in the game bounds
        :param pos: position to be evauluated is tuple (x,y)
        :return: true if the position is within the bounds
                 false otherwise
        """
        return ((pos.x<WIDTH) & (pos.x>=0) & (pos.y<HEIGHT) & (pos.y>=0))
    
    def movePos(self,p,intMove):
        """
        Takes a pawn and returns it's relative move position
        :param p: A Pawn on the board
        :param intMove: The type of move wanted
                     0: move forward relative to player
                     -1: attack left relative to player
                     1: attack right relative to player
        :return: A tuple with (x,y) in for the desired move relative to the pawn's position
        """
        return pos(p.pos.x-(intMove*self.intPlayer(p.color)),p.pos.y+self.intPlayer(p.color))
    
    def legalMove(self,p,intMove):
        """
        Tells if a move is legal
        :param p: Pawn to be moved
        :param intMove: The type of move wanted
                     0: move forward relative to player
                     -1: attack left relative to player
                     1: attack right relative to player
        :return: True if the move is legal
        """
        mPos = self.movePos(p,intMove)
        if(self.inBounds(mPos)!=True):
            return False
        if(p.color != self.whoseTurn):#Can't make move if it's not players pawn
            return False
        if(intMove==0):#to move forward the node must be empty
            return (self.gameState[mPos.get()] == EMPTY)
        else:#to attack the node must have an enemy
            return (self.gameState[mPos.get()] == self.togglePlayer(p.color))
    
    def openMoves(self):
        """
        Gets a list of all available moves
        """
        arr = []
        for y in range(0,HEIGHT):
            for x in range(0,WIDTH):
                t = self.getPawn(x,y)
                if(t!=None):
                    for z in range(-1,2):
                        if(self.legalMove(t,z)):
                            arr.append((x,y,z))
        return arr
    
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
        if(intMove==0):#Move Forward
            gs[p.pos.x,p.pos.y+self.intPlayer(p.color)] = p.color
        elif(intMove==-1):#Attack left
            gs[p.pos.x+self.intPlayer(p.color),p.pos.y+self.intPlayer(p.color)] = p.color
        elif(intMove== 1):#Attack right
            gs[p.pos.x-self.intPlayer(p.color),p.pos.y+self.intPlayer(p.color)] = p.color

        gs[p.pos.get()] = '-'
        return (p,intMove),gs






