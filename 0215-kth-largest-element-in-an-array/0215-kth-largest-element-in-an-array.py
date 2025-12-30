class Solution(object):
    def findKthLargest(self, nums, k):
        count = 0
        hq = []
        maxNum = nums[0]
        minNum = nums[0]
        arr = None
        for i in range(len(nums)):
            if maxNum < nums[i]:
                maxNum = nums[i]
            if minNum > nums[i]:
                minNum = nums[i]
        if maxNum >= 0:
            maxNum += 1
            arr = [0] * maxNum
        minusArr = None
        if minNum < 0:
            minNum -= 1
            minusArr = [0] * abs(minNum)

        # print(maxNum)
        # print(len(nums))
        for i in range(len(nums)):
            if nums[i] < 0:
                idx = abs(nums[i])
                minusArr[idx] += 1
            else:
                arr[nums[i]] += 1
        
        print(arr)
        prevCount = 0
        for i in range(maxNum - 1, -1, -1):
            count += arr[i]
            if arr[i] > 1:
                if count > k and prevCount < k:
                    return i
            if count == k:
                return i
            prevCount = count
        newMinNum = abs(minNum)
        for i in range(newMinNum):
            count += minusArr[i]
            if minusArr[i] > 1:
                if count > k and prevCount < k:
                    return -i
            if count == k:
                return -i
            prevCount = count
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        