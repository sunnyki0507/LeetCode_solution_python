class Solution(object):
    def findCircleNum(self, isConnected):
        num = len(isConnected)
        self.visited = [0] * num
        vals = deque()
        # self.visited[0] = 1
        self.count = 0
        total = num
        # for i in range(len(isConnected[0])):
        #     if isConnected[0][i] == 1:
        #         vals.append(i)
        # count = 0
        # while vals:
        def dfs(idx):
            if self.visited[idx] == 1:
                return
            self.visited[idx] = 1
            self.count += 1
            for i in range(num):
                if isConnected[idx][i] == 1:
                    dfs(i)
        index = 0
        numOfPro = 0
        while total > 0 and index < num:
            dfs(index)
            index += 1
            if self.count > 0:
                numOfPro += 1
            total -= self.count
            self.count = 0
        return numOfPro
        






        return 0
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        