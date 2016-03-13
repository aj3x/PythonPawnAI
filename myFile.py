#imports
import sys
import PWND
import MiniMax
import AlphaBeta
sys.path.append('C:\\Users\\AJ3X\\Documents\\GitHub\\PythonPawnAI\\Var1')
    
    
#    import boardClass
    
#__path__.append(os.path.abspath(os.path.dirname(_mypkg_foo.__file__)))



    


    
        
        


whites = []
blacks = []
b = PWND.Board(None)
m =MiniMax#.minimax(b)
p = b.getPawn(1,1)
a = AlphaBeta.alphaMini(b)
def nextPawn(mn):
    return mn[1][0]

def nextB(bn,an):
    return bn.move(an[1][0],an[1][1])[1]

def nextM(bn):
    return MiniMax.minimax(bn)

def nextA(bn,an):
    return an.alphaMini(bn)
def nxt():
    bn = nextB(b,m)
    mn = nextM(bn)
    #print(bn.__repr__())
    return bn,mn
def mov(x,y,move):
    bn = nextB(b,m)[1]
    mn = nextM(bn)
    print(bn.__repr__())
    return bn,mn
    
def nt(bn,mn):
    bn = nextB(bn,mn)
    mn = nextM(bn)
    print(bn.__repr__())

class autoTurn:
    def __init__(self,b,a):
        self.b = b
        self.a = a
    def play(self,turns):
        for x in range(0,turns):
            self.b = nextB(self.b,self.a)
            self.a = nextA(self.b)
            print(self.b.__repr__())

test = autoTurn(b,m)
