class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1: 
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            previous = list(self.generate(numRows-1))
            lastRow = previous[-1]
            result = [1]
            for x in range(0,len(lastRow)-1):
                sum_elem = lastRow[x]+lastRow[x+1] 
                result.append(sum_elem)
            result.append(1)
            previous.append(result)
            return previous
        
        
