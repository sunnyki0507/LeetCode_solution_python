class Solution(object):
    def rotate(self, matrix):
        length = len(matrix)
        for i in range(length):
            for j in range(length):
                matrix[i].append(matrix[length - j - 1][i])
        for i in range(length):
            matrix[i] = matrix[i][length:]
        return
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        