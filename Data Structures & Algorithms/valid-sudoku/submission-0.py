class Solution:
    
    def checkSquare(self, row1: int, col1: int, board: List[List[str]]) -> bool:
        listSquare = {}
        for i in range (row1, row1 + 3) :
            for y in range (col1, col1 + 3) :
                temp = board[i][y]
                if temp.isdigit() and temp not in listSquare :
                    listSquare[temp] = 1
                elif temp == '.' :
                    continue
                elif int(temp) > 9 or int(temp) < 0 :
                    return False
                elif temp in listSquare :
                    return False
        return True

    def checkRow (self, board: List[List[str]]) -> bool:
        for i in range(9) :
            listRow = {}
            for y in range (9) :
                temp = board[i][y]
                if temp.isdigit() and temp not in listRow :
                    listRow[temp] = 1
                elif temp == '.' :
                    continue
                elif int(temp) > 9 or int(temp) < 0 :
                    return False
                elif temp in listRow :
                    return False
        return True
    def checkColumn (self, board: List[List[str]]) -> bool :
        for i in range(9) :
            listRow = {}
            for y in range (9) :
                temp = board[y][i]
                if temp.isdigit() and temp not in listRow :
                    listRow[temp] = 1
                elif temp == '.' :
                    continue
                elif int(temp) > 9 or int(temp) < 0 :
                    return False
                elif temp in listRow :
                    return False
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not self.checkRow(board):
            return False
        if not self.checkColumn(board):
            return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.checkSquare(i, j, board):
                    return False
        return True
        