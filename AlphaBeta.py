import PWND

def boardValue(node):
    """
    Takes a board and evaluates what it's worth
    """
    dis = 0
    for x in range(0,PWND.WIDTH):
        for y in range(0,PWND.HEIGHT):
            t = node.getPawn(x,y)
            if(t!=None):
                dis+=1
    val = (node.count(node.whoseTurn)-node.count(node.togglePlayer(node.whoseTurn)))*PWND.PAWN_VALUE
    #for y in range(0,PWND.HEIGHT):
    #    for x in range(0,PWND.WIDTH):
    return val+dis