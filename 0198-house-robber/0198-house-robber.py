class Solution(object):
    def rob(self, nums):
        curr = 0
        length = len(nums)
        if length == 1:
            return nums[0]
        elif length == 2:
            return max(nums[0], nums[1])
        elif length == 3:
            return max(nums[0]+nums[2], nums[1])
        first = nums[0]
        second = nums[1]
        third = nums[0]+nums[2]
        for i in range(3, length):
            curr = max(first, second) + nums[i]
            print(curr)
            first = second
            second = third
            third = curr
        return max(first, second, third)
            

        """
        :type nums: List[int]
        :rtype: int
        """
        