class Solution(object):
    def removeDuplicates(self, nums):
        erase = []
        prev = nums[0]
        repeat = 1
        for i in range(1, len(nums)):
            if prev == nums[i]:
                repeat += 1
            else:
                repeat = 1
            prev = nums[i]
            if repeat > 2:
                erase.append(nums[i])
        while erase:
            idx = nums.index(erase.pop())
            nums.pop(idx)
        return len(nums)


        """
        :type nums: List[int]
        :rtype: int
        """
        