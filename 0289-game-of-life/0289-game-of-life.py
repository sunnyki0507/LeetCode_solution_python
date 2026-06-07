class Solution(object):
    def gameOfLife(self, board):
        m = len(board)
        n = len(board[0])
        # tmp = [[0]*n for _ in range(m)]
        total = 0
        if m == 1 and n == 1:
            board[0][0] = 0
            return
        for i in range(m):
            for j in range(n):
                total, colS, colE, rowS, rowE = -board[i][j], 0, n-1, 0, m-1
                if j != 0:
                    colS = j - 1
                if j < (n-1):
                    colE = j + 1
                if i != 0:
                    rowS = i - 1
                if i < (m-1):
                    rowE = i + 1
                for r in range(rowS, rowE+1):
                    for c in range(colS, colE+1):
                        total += board[r][c]
                if board[i][j] == 0:
                    if total == 3:
                        board[i].append(1)
                    else:
                        board[i].append(0)

                else:
                    if total < 2 or total > 3:
                        board[i].append(0)
                    else:
                        board[i].append(1)
        for idx in range(m):
            board[idx] = board[idx][n:]
                
                

                # if 0<i<m-1 and 0<j<n-1:

                # elif 0<i<m-1:

                # elif 0<j<n-1:

                # else:
                #     if m == 1 and n == 1:
                #         board = [0]
                #         return
                #     elif 


        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        