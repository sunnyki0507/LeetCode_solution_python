class Solution(object):
    def candy(self, ratings):
        length = len(ratings)
        candyN = [1] * length
        for i in range(1, length):
            if ratings[i] > ratings[i-1]:
                candyN[i] = candyN[i-1] + 1
        for i in range(length-1,0,-1):
            if ratings[i] < ratings[i-1]:
                if candyN[i] >= candyN[i-1]:
                    candyN[i-1] = candyN[i] + 1
        return sum(candyN)


#1+0+(-1)+(-2)+1+2+3

        #2+1+1+1+2+1+1+2+3+4
        #4+3+2+1+2+1+1+2+3+4
        #1+0+(-1)+(-2)+|(1)+(0)+(-1)+(-2)+|(1)+(2)+(3)+(4)
        #->  4+3+2+1+4+3+2+1+1+2+3+4
        #1+0+(-1)+(-2)+|(-1)+(-2)+(-3)+(-4)+(1)+(2)+(3)+(4)

        #[1, 0, -1, -2, -1, 0, 1]

        #[5,6,7,8,1,2]
        """
        :type ratings: List[int]
        :rtype: int
        """
        