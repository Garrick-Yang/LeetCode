from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        row_0 = []
        col_0 = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_0.append(i)
                    col_0.append(j)
        row_0 = set(row_0)
        col_0 = set(col_0)
        for i in range(m):
            for j in range(n):
                if i in row_0 or j in col_0:
                    matrix[i][j] = 0
        return matrix
    
s = Solution()
print(s.setZeroes([[1,1,1],[1,0,1],[1,1,1]])) # [[1,0,1],[0,0,0],[1,0,1]]
        