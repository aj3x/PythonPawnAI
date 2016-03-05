import AlphaBeta
DEPTH_LIMIT = 10


transpositionTable = dict()
#(int,(pawn,move))
def minimax(node,depth=0):
    depth+=1
    global transpositionTable
    s= str(node)
    if s in transpositionTable:
        return transpositionTable[s]
    elif node.isTerminal():
        u = node.utility()
        m = None
    # elif depth > DEPTH_LIMIT:
    #     if node.isMaxNode():
            # u,m = argmax([AlphaBeta.boardValue(node),AlphaBeta.boardValue(node)])
        # elif node.isMinNode():
            # u,m = argmin([AlphaBeta.boardValue(node),AlphaBeta.boardValue(node)])
        # else:
            # print("OhNoes")
            # return None
        # return u,m
    else:
        vs = [(minimax(c,depth)[0],m) for (m,c) in node.successors()]  # strip off the move returned by minimax!
        if node.isMaxNode():
            u,m = argmax(vs)
        elif node.isMinNode():
            u,m = argmin(vs)
        else:
            print("Something went horribly wrong")
            return None
    transpositionTable[s] = u,m  # store the move and the utility in the tpt
    return u,m
    
def argmax(ns):
    """
    find the highest utility,move pair
    :param ns: a list of utility,move pairs
    :return:  the utility,move pair with the highest utility
    """
    maxv,maxm = ns[0]
    for v,m in ns:
        if v > maxv:
            maxv,maxm = v,m
    return maxv,maxm


def argmin(ns):
    """
    find the lowest utility,move pair
    :param ns: a list of utility,move pairs
    :return:  the utility,move pair with the lowest utility
    """
    minv,minm = ns[0]
    for v,m in ns:
        if v < minv:
            minv,minm = v,m
    return minv,minm
