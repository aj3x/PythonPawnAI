#imports
import sys
import PWND
import MiniMax
sys.path.append('C:\\Users\\AJ3X\\Documents\\GitHub\\PythonPawnAI\\Var1')
    
    
#    import boardClass
    
#__path__.append(os.path.abspath(os.path.dirname(_mypkg_foo.__file__)))



    


    
        
        


whites = []
blacks = []
b = PWND.Board(None)
m =MiniMax.minimax(b)
p = b.getPawn(1,1)

def nextPawn(mn):
    return mn[1][0]

def nextBoard(bn,mn):
    return bn.move(mn[1][0],mn[1][1])[1]

def nextMinimax(bn):
    return MiniMax.minimax(bn)
def nxt():
    bn = nextBoard(b,m)
    mn = nextMinimax(bn)
    print(bn.__repr__())
    return bn,mn
