# PythonPawnAI

## Game Rules

Two player game played on a 5x6 board.
Both players pieces are pawns, black or white.

Pawns follow the same rules as chess:
- Pawn may move one space forward if the position is unoccupied
- Pawn may *attack* on the forward diagonals if they are occupied by an opponents piece

#### Starting Board Positions
-|0|1|2|3|4
-|-|-|-|-|-
0|w|w|w|w|w
1| | | | | 
2| | | | | 
3| | | | |
4| | | | |
5|b|b|b|b|b

Players win by getting one of their pieces to the opponents *home row*

---

## AI Implementation

First we require methods of determining if a board is in a terminal state(i.e. one of the players have won or no player can move). From here I developed a MiniMax algorithm and further improved search times by implementing AlphaBeta Pruning.
