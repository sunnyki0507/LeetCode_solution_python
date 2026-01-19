class Solution(object):
    def trap(self, height):
        length = len(height)
        water = [0] * length
        h = height[0]
        for i in range(1, length):
            if height[i] > h:
                h = height[i]
                continue
            water[i] = h - height[i]
        h = height[length-1]
        water[length-1] = 0
        for i in range(length-2,-1,-1):
            if height[i] > h:
                water[i] = 0
                h = height[i]
                continue
            if water[i] > (h - height[i]):
                water[i] = h - height[i]
        return sum(water)

        """
        :type height: List[int]
        :rtype: int
        """
        