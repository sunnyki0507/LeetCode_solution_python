class Solution(object):
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        zerom = set()
        zeron = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zerom.add(i)
                    zeron.add(j)
        while zerom:
            row = zerom.pop()
            matrix[row] = [0] * n
        while zeron:
            col = zeron.pop()
            for i in matrix:
                i[col] = 0
        return
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        