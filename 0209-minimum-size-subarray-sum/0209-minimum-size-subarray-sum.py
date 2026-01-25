class Solution(object):
    def minSubArrayLen(self, target, nums):


        n = len(nums)
        minN = float("inf")
        right = 0
        left = 0
        s = 0

        for i in range(n):
            s += nums[i]
            right = i
            
            while s >= target:
                if right - left + 1 < minN:
                    minN = right - left + 1
                s -= nums[left]
                left += 1

        return minN if minN != float("inf") else 0


        # n = len(nums)
        # minN = n+1
        # curr = []
        # s = nums[0]
        # i = 1
        # curr.append(nums[0])
        
        # while i < n:
        #     print(s)
        #     if s >= target:
        #         if len(curr) < minN:
        #             minN = len(curr)
        #         s -= curr.pop(0)
        #     else:
        #         curr.append(nums[i])
        #         s += nums[i]
        #         i += 1
        # while curr and s >= target:
        #     print(s)
        #     if s >= target:
        #         if len(curr) < minN:
        #             minN = len(curr)
        #         s -= curr.pop(0)
        # if minN == n+1:
        #     return 0
        # return minN





        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        