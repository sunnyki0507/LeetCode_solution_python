class Solution(object):
    def orangesRotting(self, grid):
        row = len(grid)
        col = len(grid[0])
        # rotten = [[0] * col for _ in range(row)]
        arr = deque()
        minCount = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    arr.append([i, j, 0])

        while arr:
            orange = arr.popleft()
            r = orange[0]
            c = orange[1]
            print(r)
            print(c)
            step = orange[2]
            minCount = step
            if (r+1) < row:
                if grid[r+1][c] == 1:
                    grid[r+1][c] = 2
                    arr.append([r+1, c, step + 1])
            if (r-1) >= 0:
                if grid[r-1][c] == 1:
                    grid[r-1][c] = 2
                    arr.append([r-1, c, step + 1])
            if (c+1) < col:
                if grid[r][c+1] == 1:
                    grid[r][c+1] = 2
                    arr.append([r, c+1, step + 1])
            if (c-1) >= 0:
                print("Hello")
                if grid[r][c-1] == 1:
                    grid[r][c-1] = 2
                    arr.append([r, c-1, step+1])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1
                
        return minCount
            



        



        """
        :type grid: List[List[int]]
        :rtype: int
        """
        