import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        INF = float("inf")
        dist = [[INF] * COLS for _ in range(ROWS)]
        dist[0][0] = 0

        minHeap = []
        heapq.heappush(minHeap, (0, 0, 0))
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while minHeap:
            w, r, c = heapq.heappop(minHeap)

            if r == ROWS - 1 and c == COLS - 1:
                return w

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    minEffort = max(abs(heights[r][c] - heights[nr][nc]), w)
                    if minEffort < dist[nr][nc]:
                        dist[nr][nc] = minEffort
                        heapq.heappush(minHeap, (minEffort, nr, nc))


# class Solution:
#     def minimumEffortPath(self, heights: List[List[int]]) -> int:
#         ROWS, COLS = len(heights), len(heights[0])
#         visited = set()

#         minHeap = [(0, 0, 0)]
#         directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

#         while minHeap:
#             w, r, c = heapq.heappop(minHeap)

#             if (r, c) in visited:
#                 continue
#             visited.add((r, c))
#             if r == ROWS - 1 and c == COLS - 1:
#                 return w

#             for dr, dc in directions:
#                 nr, nc = r + dr, c + dc

#                 if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited:
#                     minEffort = max(abs(heights[r][c] - heights[nr][nc]), w)
#                     heapq.heappush(minHeap, (minEffort, nr, nc))




