class Solution(object):
    def minCostClimbingStairs(self, cost):
        curr = 0
        First = cost[0]
        Second = cost[1]
        length = len(cost)
        if length <= 2:
            return min(First, Second)
        for i in range(2, length):
            curr = min(First, Second) + cost[i]
            First = Second
            Second = curr
        return min(First, Second)


        # prev = 1
        # total = cost[0]
        # add = 0
        # length = len(cost)
        # if length == 2:
        #     if cost[0] > cost[1]:
        #         return cost[1]
        #     else:
        #         return cost[0]
        # if length == 3:
        #     if (cost[0] + cost[2]) >= cost[1]:
        #         return cost[1]
        #     else:
        #         return cost[0] + cost[2]
        # else:
        #     if cost[0] == 0:
        #         add = 1
        #         if (cost[1] + cost[3]) > cost[2]:
        #             total = cost[2]
        #             prev = 2
        #         else:
        #             total = cost[1] + cost[3]
        #             prev = 1
        #     else:
        #         if (cost[0] + cost[2]) >= (cost[1] + cost[2]):
        #             total = cost[1] + cost[2]
        #             prev = 2
        #         else:
        #             total = cost[0] + cost[2]
        #             prev = 2
        #         if total >= (cost[1] + cost[3]):
        #             total = cost[1] + cost[3]
        #             prev = 1
        # for i in range(4, len(cost)):
        #     print(total)
        #     print(prev)
        #     if prev == 1:
        #         prev = 2
        #         continue
        #     else:
        #         if (total + cost[i]) <= (total + cost[i-1]):
        #             prev = 1
        #             total = total + cost[i]
        #         else:
        #             prev = 2
        #             total = total + cost[i-1]
        # return total
        """
        :type cost: List[int]
        :rtype: int
        """
        