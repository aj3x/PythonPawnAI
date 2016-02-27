#def __init__
#__path__.append(os.path.abspath(os.path.dirname(_mypkg_foo.__file__)))

bWidth = 0
bHeight = 0

def start(width,height):
    bWidth = width
    bHeight = height
    board.append(0)
    #board[width*height] =0
    for x in board:
        x = 0

def printBoard(board):
    for x in board:
        print(x)




#if __name__ == "__main__":
#    import sys
#    board=[[]]
#    for x in range(int(sys.argv[1])):
#        for y in range(int(sys.argv[2])):
#            board[x][y]=0
#    printBoard(board)


