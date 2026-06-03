class Solution(object):
    def spiralOrder(self, matrix):
        d = 0
        arr = []
        r = len(matrix)
        c = len(matrix[0])
        occu = [[0] * c for _ in range(r)]
        rn = 0
        cn = 0
        while occu[rn][cn] == 0:
            arr.append(matrix[rn][cn])
            occu[rn][cn] = 1
            if d % 4 == 0:
                cn += 1
                if cn >= c or occu[rn][cn] != 0:
                    d += 1
                    cn -= 1
                    rn += 1
                    if rn >= r or occu[rn][cn] != 0:
                        break
            elif d % 4 == 1:
                rn += 1
                if rn >= r or occu[rn][cn] != 0:
                    rn -= 1
                    d += 1
                    cn -= 1
            elif d % 4 == 2:
                cn -= 1
                if cn < 0 or occu[rn][cn] != 0:
                    d += 1
                    cn += 1
                    rn -= 1
            else:
                rn -= 1
                if occu[rn][cn] != 0:
                    rn += 1
                    d += 1
                    cn += 1
        return arr
        
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        