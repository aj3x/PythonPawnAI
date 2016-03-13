import PWND
import MiniMax

DEPTH_LIMIT = 5
PAWN_VALUE = 20
THREAT_VALUE = 5
transpositionTable = dict()
def alphabeta(node):
    MiniMax.argMax()
    MiniMax.argMin()

def alphaMini(node,depth = 0,end = False):
    """
    :param node:  a Game object responding to the following methods:
        str(): return a unique string describing the state of the game (for use in hash table)
        isTerminal(): checks if the game is at a terminal state
        utility():
        successors(): returns a list of all legal game states that extend this one by one move
                      in this version, the list consists of a move,state pair
        isMinNode(): returns True if the node represents a state in which Min is to move
        isMaxNode(): returns True if the node represents a state in which Max is to move
    :return: a pair, u,m consisting of the minimax utility, and a move that obtains it
    """
    depth+=1
    s= str(node)
    if (s in transpositionTable):
        if(transpositionTable[s][1] != False) :
            return transpositionTable[s]
    if node.isTerminal():
        u = node.utility()
        m = None
    elif depth > DEPTH_LIMIT:
        u = boardValue(node)
        m = False
    else:
        #print(depth)
        vs = [(alphaMini(c,depth)[0],m) for (m,c) in node.successors()]  # strip off the move returned by minimax!
        if node.isMaxNode():
            u,m = MiniMax.argmax(vs)
        elif node.isMinNode():
            u,m = MiniMax.argmin(vs)
        else:
            print("Something went horribly wrong")
            return None
    transpositionTable[s] = u,m  # store the move and the utility in the tpt
    #depth = 0
    return u,m
    
    
def hasMove(pawn,node):
    for z in range(-1,2):
        if node.legalMove(pawn,z):
            return True
    return False
def boardValue(node):
    """
    Takes a board and evaluates what it's worth
    "param node"
    """
    b = dict()
    w = dict()
    threat = 0
    kills = 0
    for x in range(0,PWND.WIDTH):
        for y in range(0,PWND.HEIGHT):
            t = node.getPawn(x,y)
            if(t!=None):
                if (hasMove(t,node) & t.isColor(node.whoseTurn)):#check if it's a move from winning
                    bs = node
                    bs = bs.move(t,0)[1]
                    if bs.winFor(t.color):
                        return 100
                for z in range(-1,2):
                    if((z!=0) & (node.legalMove(t,z))):#can kill
                        kills += PAWN_VALUE*node.intPlayer(node.whoseTurn)
                    m = node.movePos(t,z)
                    if(node.inBounds(m)):
                        if t.color == PWND.WHITE:
                            if str(m) in w:
                                zzz =0
                            else:
                                w[str(m)] = True
                                threat+=THREAT_VALUE
                        else:
                            if str(m) in b:
                                zzz = 0
                            else:
                                b[str(m)] = True
                                threat-=THREAT_VALUE
    pawns = (node.count(PWND.WHITE)-node.count(PWND.BLACK))*PAWN_VALUE
    #for y in range(0,PWND.HEIGHT):
    #    for x in range(0,PWND.WIDTH):
    #print(b)
    #print(w)
    return pawns+threat+kills