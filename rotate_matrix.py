class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print(matrix)

s=Solution()
print(s.rotate([[1,2,3],[4,5,6],[7,8,9]]))