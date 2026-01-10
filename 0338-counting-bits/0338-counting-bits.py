class Solution(object):
    def countBits(self, n):
        if n == 0:
            return [0]
        if n == 1:
            return [0,1]
        if n == 2:
            return [0,1,1]
        ans = [0,1,1,2]
        num = 3
        while True:
            length = len(ans)
            if num == n:
                break
            for i in range(length):
                if num == n:
                    break
                ans.append(ans[i]+1)
                num = num + 1
        return ans
        """
        :type n: int
        :rtype: List[int]
        """
        # 0,1,10,11,100,101, 110, 111, 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111, 10000, 10001, 10010, 10011, 10100
        # 0,1,| 1,2,| 1,2,2,3 |,1, 2, 2, 3, 2, 3, 3, 4|, 1 , 2, 2, 3, 2