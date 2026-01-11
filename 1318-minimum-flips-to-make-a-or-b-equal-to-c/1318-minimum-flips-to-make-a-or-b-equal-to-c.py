class Solution(object):
    def minFlips(self, a, b, c):
        A = int(bin(a)[2:])
        B = int(bin(b)[2:])
        C = bin(c)[2:]
        # print(A)
        # print(B)
        comb = str(bin(a | b)[2:])
        # comb = str(bin(comb)
        A = str(A)
        B = str(B)
        if len(C) > len(comb):
            comb = comb.zfill(len(C))
            A = A.zfill(len(C))
            B = B.zfill(len(C))
        elif len(C) < len(comb):
            C = C.zfill(len(comb))
            A = A.zfill(len(comb))
            B = B.zfill(len(comb))
        else:
            A = A.zfill(len(comb))
            B = B.zfill(len(comb))
        change = 0
        print(comb)
        print(C)
        print(A)
        print(B)
        for i in range(len(C)):
            if C[i] is not comb[i]:
                if C[i] == '1':
                    change += 1
                else:
                    if A[i] == '1':
                        change += 1
                    if B[i] == '1':
                        change += 1
        return change

        
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        