class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        col = len(maze[0])
        row = len(maze)
        visited = [[0] * col for _ in range(row)]
        min = -1
        count = 0

        r = entrance[0]
        c = entrance[1]
        arr = deque()
        visited[r][c] = 1
        if (r + 1) < row:
            if maze[r + 1][c] == '.' and visited[r + 1][c] == 0:
                visited[r + 1][c] == 1
                arr.append([r+1, c, 1])
        if (r - 1) >= 0:
            if maze[r - 1][c] == '.' and visited[r - 1][c] == 0:
                visited[r - 1][c] == 1
                arr.append([r-1, c, 1])
        if (c + 1) < col:
            if maze[r][c + 1] == '.' and visited[r][c + 1] == 0:
                visited[r][c+1] == 1
                arr.append([r, c+1, 1])
        if (c - 1) >= 0:
            if maze[r][c - 1] == '.' and visited[r][c - 1] == 0:
                visited[r][c-1] == 1
                arr.append([r, c-1, 1])

        while arr:
            pos = arr.popleft()
            r = pos[0]
            c = pos[1]
            count = pos[2]
            if (r + 1) == row or (r - 1) == - 1 or (c + 1) == col or (c - 1) == -1:
                if min == -1 or min > count:
                    min = count

            if (r + 1) < row:
                if maze[r + 1][c] == '.' and visited[r + 1][c] == 0:
                    visited[r + 1][c] = 1
                    arr.append([r+1, c, count + 1])
            if (r - 1) >= 0:
                if maze[r - 1][c] == '.' and visited[r - 1][c] == 0:
                    visited[r - 1][c] = 1
                    arr.append([r-1, c, count + 1])
            if (c + 1) < col:
                if maze[r][c + 1] == '.' and visited[r][c + 1] == 0:
                    visited[r][c+1] = 1
                    arr.append([r, c+1, count + 1])
            if (c - 1) >= 0:
                if maze[r][c - 1] == '.' and visited[r][c - 1] == 0:
                    visited[r][c-1] = 1
                    arr.append([r, c-1, count + 1])
        print("Hello")
        return min
            

            




        # def bfs(pos,count):
        #     newR = pos[0]
        #     newC = pos[1]
        #     self.visited[newR][newC] = 1
        #     print(count)
        #     print("row : ", newR)
        #     if (newR + 1) == row or (newR - 1) == - 1 or (newC + 1) == col or (newC - 1) == -1:
        #         if self.min > count and count is not 0:
        #             self.min = count
        #     if (newR + 1) < row :
        #         r1 = newR + 1
        #         c1 = newC
        #         if maze[r1][c1] == '.' and self.visited[r1][c1] == 0:
        #             bfs([r1, c1], count + 1)
        #     if (newR - 1) >= 0:
        #         r2 = newR - 1
        #         c2 = newC
        #         if maze[r2][c2] == '.' and self.visited[r2][c2] == 0:
        #             bfs([r2, c2], count + 1)
        #     if (newC + 1) < col:
        #         r3 = newR
        #         c3 = newC + 1
        #         if maze[r3][c3] == '.' and self.visited[r3][c3] == 0:
        #             bfs([r3, c3], count + 1)
        #     if (newC - 1) >= 0:
        #         r4 = newR
        #         c4 = newC - 1
        #         if maze[r4][c4] == '.' and self.visited[r4][c4] == 0:
        #             bfs([r4, c4], count + 1)

        # bfs(entrance, 0)

        # return -1 if self.min == row * col else self.min