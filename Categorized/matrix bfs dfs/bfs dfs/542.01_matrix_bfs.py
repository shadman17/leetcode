class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        queue = deque()
        visited = [[0] * n for i in range(m)]
        dist = [[-1] * n for i in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    visited[i][j] = 1
                    dist[i][j] = 0

        while queue:
            x, y = queue.popleft()
            directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if (
                    0 <= nx < m
                    and 0 <= ny < n
                    and visited[nx][ny] == 0
                    and dist[nx][ny] == -1
                ):
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    dist[nx][ny] = dist[x][y] + 1

        return dist
