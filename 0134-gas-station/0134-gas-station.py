class Solution(object):
    def canCompleteCircuit(self, gas, cost):

        total,surplus,start = 0,0,0
        length = len(gas)
        for i in range(length):
            total += gas[i] - cost[i]
            surplus += gas[i] - cost[i]
            if surplus < 0:
                surplus = 0
                start = i + 1
        return start if total >= 0 else -1
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        