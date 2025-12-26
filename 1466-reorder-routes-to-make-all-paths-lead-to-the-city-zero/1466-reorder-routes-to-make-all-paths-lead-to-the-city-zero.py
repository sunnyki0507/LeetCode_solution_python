class Solution(object):
    def minReorder(self, n, connections):
        # vals = deque()
        # count = 0
        # arr = []
        # visited = [0] * n
        # visited[0] = 1
        # used = [0] * (n-1)
        # if n == 0 or n < 0:
        #     return 0

        # for i in range(n - 1):
        #     if used[i] == 1:
        #         continue
        #     arr = connections[i]
        #     if arr[0] == 0:
        #         used[i] = 1
        #         count += 1
        #         vals.append(arr[1])
        #     elif arr[1] == 0:
        #         used[i] = 1
        #         vals.append(arr[0])
        # while vals:
        #     idx = vals.popleft()
        #     visited[idx] = 1
        #     for i in range(n - 1):
        #         if used[i] == 1:
        #             continue
        #         arr = connections[i]
        #         if arr[0] == idx:
        #             used[i] = 1
        #             if visited[arr[1]] == 0:
        #                 vals.append(arr[1])
        #                 count += 1
        #         elif arr[1] == idx:
        #             used[i] = 1
        #             if visited[arr[0]] == 0:
        #                 vals.append(arr[0])
        # return count
        graph = [[] for _ in range(n)]
        for a, b in connections:
            graph[a].append([b, 1])
            graph[b].append([a, 0])

        visited = [False] * n
        visited[0] = True
        q = deque([0])
        count = 0

        while q:
            node = q.popleft()
            for nei, cost in graph[node]:
                if visited[nei] == False:
                    count += cost
                    q.append(nei)
            visited[node] = True
        return count

        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        