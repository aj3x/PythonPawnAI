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

class pawn:
    def __init__(self,x,y,color):
        self.pos = pos(x,y)
        self.color = color
    def __repr__(self):
        return str(self.pos)+str(self.color)
    def isWhite(self):
        return self.color==WHITE
    def move(self,pos):
        self.pos = pos
        

class board:
    def __init__(self,state,player=WHITE):
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

    #Used for debugging and displaying in user friendly manner
    def __repr__(self):
        s = ""
        for y in range(0,HEIGHT):
            temp=""
            for x in range(0,WIDTH):
                temp = temp+ str(self.gameState[x,y])
            s += temp+"\n"
        return s

    #Used for hash table
    def __str__(self):
        s=""
        for x in range(0,WIDTH):
            for y in range(0,HEIGHT):
                s+=self.gameState[x,y]
        return s

    def isMinNode(self):
        return self.whoseTurn==BLACK
    def isMaxNode(self):
        return self.whoseTurn==WHITE
    
    def getNode(self,x,y):
        if((x<0) | (y<0)):
            return "values are negative"
        if((x+1)*(1+y)>=WIDTH*HEIGHT):
            return "values out of range"
        return self.gameState[x,y]
    def setNode(self,x,y,space):
        if((x<0) | (y<0)):
            return "values are negative"
        if((x+1)*(1+y)>=WIDTH*HEIGHT):
            return "values out of range"
        if((space==WHITE)|(space==BLACK )|(space==EMPTY)):
            self.gameState[x,y] = space
        else:
            return "space must be("+WHITE+","+BLACK+","+EMPTY+")"
        
    #def successors(self):
    #Check if var:player has won
    def winFor(self,player):
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
        if(self.winFor(WHITE)):
            return 1
        elif(self.winFor(BLACK)):
            return -1
        else:
            return 0
    
    def togglePlayer(self,p):
        if(p==WHITE):
            return BLACK
        else:
            return WHITE
    
    def intPlayer(self,p):
        if(p==WHITE):
            return -1
        else:
            return 1
            
    def moves(self):
        for x in range(0,WIDTH):
            for y in range(0,HEIGHT):
                self.gameState[x,y]
    
    
    
    def hasTurnPawn(self,x,y):
        return self.gameState[x,y]==whoseTurn
        
    
    
    #Moves forward relative to player
    def move(self,p):
        gs = self.gameState.copy()
        gs[p.pos.x,p.pos.y+self.intPlayer(p.color)] = p.color
        gs[p.pos.x,p.pos.y] = '-'
        return gs
    #Attacks left relative to player
    def attackL(self, p):
        gs = self.gameState.copy()
        self.gameState[p.pos.x+self.intPlayer(p.color),p.pos.y+self.intPlayer(p.color)] = p.color
        self.gameState[p.pos.x,p.pos.y] = '-'
        return gs
    #Attacks right releative to player
    def attackR(self,p):
        gs = self.gameState.copy()
        self.gameState[p.pos.x-self.intPlayer(p.color),p.pos.y+self.intPlayer(p.color)] = p.color
        self.gameState[p.pos.x,p.pos.y] = '-'
        return gs






