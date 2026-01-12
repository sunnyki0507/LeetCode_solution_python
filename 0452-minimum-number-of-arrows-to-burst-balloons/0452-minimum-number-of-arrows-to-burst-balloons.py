class Solution(object):
    def findMinArrowShots(self, points):
        length = len(points)
        points.sort(key = lambda x: x[1])
        print(points)
        num = 0
        end = points[0][1]
        print(end)
        for i in range(1,length):
            start = points[i][0]
            if end < start:
                print("hello")
                end = points[i][1]
                num += 1
        num += 1
        return num
        """
        :type points: List[List[int]]
        :rtype: int
        """
        