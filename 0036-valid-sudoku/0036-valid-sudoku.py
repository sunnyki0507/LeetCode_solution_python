class Solution(object):
    def isValidSudoku(self, board):
        f = [[] for _ in range(9)]
        s = [[] for _ in range(9)]
        t = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in f[i]:
                    f[i].append(board[i][j])
                else:
                    print(i)
                    print(j)
                    print("1")
                    return False
                if board[i][j] not in s[j]:
                    s[j].append(board[i][j])
                else:
                    print("2")
                    return False
                r = i / 3
                c = j / 3
                if board[i][j] not in t[r*3+c]:
                    t[r*3+c].append(board[i][j])
                else:
                    print("3")
                    return False
        return True

        """
        :type board: List[List[str]]
        :rtype: bool
        """
        