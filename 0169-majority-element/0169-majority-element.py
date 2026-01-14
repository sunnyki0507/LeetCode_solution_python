class Solution(object):
    def majorityElement(self, nums):
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 0
            dic[i] += 1
        print(dic)
        maxN = 0
        idx = -1
        for k,v in dic.items():
            if v > maxN:
                maxN = v
                idx = k
                print(maxN)
                print(idx)
        return idx

        """
        :type nums: List[int]
        :rtype: int
        """
        