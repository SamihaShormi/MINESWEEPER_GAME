import random


WIDTH = 800 
HEIGHT = 600
CELL_SIZE = 30 
REVEALED = (97, 179, 250)
HIDDEN = (246, 134, 224)
MARKED = (253,239,150)
OUTLINE = (0,0,0) 
FONT_COLOR = (0, 0, 0)
FONT_SIZE = 20
FONT_NAME = "Arial"
BOMBS = [9, 20 ,40 ]


class GamePlay:

    def __init__(self, ROWS, COLS, ind ):
        self.ROWS = ROWS
        self.COLS = COLS
        self.BOARD = [['-' for _ in range(COLS)] for _ in range(ROWS)]
        self.VISITED = [[False for _ in range(COLS)] for _ in range(ROWS)]
        self.FLAGGED = [[False for _ in range(COLS)] for _ in range(ROWS)]
        self.TOTAL_BOMBS= BOMBS[ind-1]
        # self.TOTAL_BOMBS= 5
        self.CELL_LEFT = (ROWS*COLS)
        
        self.MOVES = [
            [1,0],
            [-1,0],
            [0,1],
            [0,-1],
            [1,1],
            [-1,1],
            [1,-1],
            [-1,-1]
        ]


    def placeBombs(self):
        for _ in range(self.TOTAL_BOMBS):
            y = random.randint(0,self.ROWS-1)
            x = random.randint(0,self.COLS-1)
            
            while(self.BOARD[y][x]=='@'):
                y = random.randint(0,self.ROWS-1)
                x = random.randint(0,self.COLS-1)

            self.BOARD[y][x]='@'

    
    def CountBombs(self):
        for i in range(self.ROWS):
            for j in range(self.COLS):

                if(self.BOARD[i][j]=='@'):
                    continue

                count = 0
                for k in range(8):
                    i1 = i+ self.MOVES[k][0]
                    j1 = j+ self.MOVES[k][1]

                    if(i1<0 or i1>(self.ROWS-1) or j1<0 or j1>(self.COLS-1)):
                        continue
                    
                    if(self.BOARD[i1][j1]=='@'):
                        count+=1
                    
                    self.BOARD[i][j]= str(count)

        
    def dfs(self,i,j):
        if not self.VISITED[i][j] :
            self.VISITED[i][j] = True
            self.CELL_LEFT-=1
        
        if(self.BOARD[i][j]!='0'):
            return
        
        for k in range(4):
            i1 = i+self.MOVES[k][0]        
            j1 = j+self.MOVES[k][1]

            if(i1<0 or i1>(self.ROWS-1) or j1<0 or j1>(self.COLS-1)):
                continue    
            if(not self.VISITED[i1][j1]):
                self.dfs(i1,j1)   

    def get_cell_from_mouse(self,pos):
        x, y = pos
        col = x // CELL_SIZE
        row = y // CELL_SIZE
        return row, col


