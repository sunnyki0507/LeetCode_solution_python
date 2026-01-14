class Solution(object):
    def majorityElement(self, nums):
        count = 0
        maxN = nums[0]
        for i in nums:
            if count == 0:
                maxN = i
                count += 1
            elif maxN == i:
                count += 1
            else:
                count -= 1
        return maxN
            

        # dic = {}
        # for i in nums:
        #     if i not in dic:
        #         dic[i] = 0
        #     dic[i] += 1
        # print(dic)
        # maxN = 0
        # idx = -1
        # for k,v in dic.items():
        #     if v > maxN:
        #         maxN = v
        #         idx = k
        #         print(maxN)
        #         print(idx)
        # return idx

        """
        :type nums: List[int]
        :rtype: int
        """
        