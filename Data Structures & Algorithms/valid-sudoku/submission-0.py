class Solution:
    def checkRow(self,board) -> bool:
        rows = len(board)
        cols = len(board[0])

        for row in range(rows):
            rowSet = set()
            for col in range(cols):
                value = board[row][col]
                if value == ".":
                    continue
                
                if value in rowSet:
                    return False
                
                rowSet.add(value)
        return True

    
    def checkColumn(self,board) -> bool:
        rows = len(board)
        cols = len(board[0])

        for col in range(cols):
            colSet = set()
            for row in range(rows):
                value = board[row][col]

                if value == ".":
                    continue
                
                if value in colSet:
                    return False
                
                colSet.add(value)
        
        return True

    def check3x3Board(self,board) -> bool:
        rows = len(board)
        cols = len(board[0])

        for row in range(0,rows,3):
            for col in range(0,cols,3):
                boardSet = set()
                for i in range(row,row+3):
                    for j in range(col,col+3):
                        value = board[i][j]

                        if value == ".":
                            continue
                        
                        if value in boardSet:
                            return False
                        
                        boardSet.add(value)
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (self.checkRow(board) and self.checkColumn(board) and self.check3x3Board(board))
        