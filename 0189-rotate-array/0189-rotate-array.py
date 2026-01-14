class Solution(object):
    def rotate(self, nums, k):
        left = k % len(nums)
        print(left)
        if left<(len(nums)/2):
            for i in range(left):
                add = nums.pop()
                nums.insert(0, add)
        else:
            for i in range(len(nums) - left):
                add = nums.pop(0)
                nums.append(add)


        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        