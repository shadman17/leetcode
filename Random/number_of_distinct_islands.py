class Solution:
    def numDistinctIslands(self, grid):
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]
        shapes = set()

        def dfs(x, y, base_x, base_y, shape):
            if x < 0 or y < 0 or x >= n or y >= m or visited[x][y] or grid[x][y] == 0:
                return
            visited[x][y] = True
            shape.append((x - base_x, y - base_y))
            dfs(x + 1, y, base_x, base_y, shape)
            dfs(x - 1, y, base_x, base_y, shape)
            dfs(x, y + 1, base_x, base_y, shape)
            dfs(x, y - 1, base_x, base_y, shape)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    shape = []
                    dfs(i, j, i, j, shape)
                    shapes.add(tuple(shape))
        print(shapes)
        return len(shapes)


s = Solution()
print(
    s.numDistinctIslands(
        [[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]]
    )
)


class Solution2:
    def numDistinctIslands2(self, grid):
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]
        shapes = set()

        def dfs(x, y, direction, path):
            # if x < 0 or y < 0 or x >= n or y >= m or visited[x][y] or grid[x][y] == 0:
            #     return
            if (
                x >= 0
                and y >= 0
                and x < n
                and y < m
                and not visited[x][y]
                and grid[x][y] == 1
            ):

                visited[x][y] = True
                path.append(direction)

                dfs(x - 1, y, "U", path)  # up
                dfs(x + 1, y, "D", path)  # down
                dfs(x, y - 1, "L", path)  # left
                dfs(x, y + 1, "R", path)  # right

                path.append("B")  # backtracking marker

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    path = []
                    dfs(i, j, "S", path)  # S = start
                    shapes.add("".join(path))

        print(shapes)
        return len(shapes)


s = Solution2()
print(
    s.numDistinctIslands2(
        [[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 1, 1], [1, 1, 0, 1, 0]]
    )
)
