class Solution:
    def isValidSudoku(self, board) -> bool:
        
        #test rows
        for row in board:
            if not self.isValidRow(row):
                print("row not valid")
                return False
        
        #test cols
        for i in range(9):
            col = []
            for j in range(9):
                col.append(board[j][i])
            if not self.isValidRow(col):
                print("col not valid")
                return False
        
        #test boxes - 0,0 0,1 0,2 1,0 1,1 1,2 2,0 2,1 2,2
        indexes = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
        for i in range(3):
            for j in range(3):
                box = []
                print("new box")
                for pair in indexes:
                    index_i=pair[0]+i*3
                    index_j=pair[1]+j*3
                    print(index_i,index_j)
                    value = board[index_i][index_j]
                    box.append(value)
                if not self.isValidRow(box):
                    print("box not valid")
                    return False
        
        return True
        
        
                
        
    def isValidRow(self, row)->bool:
        exist = set()
        for x in row:
            if x in exist:
                print("not valid",row)
                return False
            elif x != ".":
                exist.add(x)
        return True


s= Solution()
print(s.isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))