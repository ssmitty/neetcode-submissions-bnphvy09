class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            rowset={}
            for j in range(9):   
                if board[i][j] in rowset:
                    return False

                if board[i][j]!=".":
                    rowset[board[i][j]]=1
                print(rowset)
        for i in range(9):
            colset={}
            for j in range(9):        
                if board[j][i] in colset:
                    return False
                if board[j][i]!=".":
                    colset[board[j][i]]=1
        for i in range(0,9,3):
            for j in range(0,9,3):
                cubeset={}
                for k in range(3):
                    for l in range(3):
                        if board[i+k][j+l] in cubeset:
                            return False
                        if board[i+k][j+l]!=".":
                            cubeset[board[i+k][j+l]]=1
        return True

