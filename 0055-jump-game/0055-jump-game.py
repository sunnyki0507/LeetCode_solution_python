class Solution(object):
    def canJump(self, nums):
        count = 1
        success = True
        nums.pop()
        while nums:
            i = nums.pop()
            if i >= count:
                count = 1
                success = True
            else:
                count += 1
                success = False
        return success

        """
        :type nums: List[int]
        :rtype: bool
        """
        