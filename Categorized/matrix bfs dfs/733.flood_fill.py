from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:

        m = len(image)
        n = len(image[0])
        x = image[sr][sc]
        if x == color:
            return image

        def dfs(i, j, image):

            if i < 0 or j < 0 or i == m or j == n or image[i][j] != x:
                return

            image[i][j] = color
            print(image[i][j])

            dfs(i + 1, j, image)
            dfs(i - 1, j, image)
            dfs(i, j + 1, image)
            dfs(i, j - 1, image)

        dfs(sr, sc, image)

        return image

#--------------dfs----------------

# class Solution:
#     def floodFill(
#         self, image: List[List[int]], sr: int, sc: int, color: int
#     ) -> List[List[int]]:

#         m = len(image)
#         n = len(image[0])
#         x = image[sr][sc]

#         def dfs(i, j, visited):

#             if (
#                 i < 0
#                 or j < 0
#                 or i == m
#                 or j == n
#                 or image[i][j] != x
#                 or (i, j) in visited
#             ):
#                 return

#             image[i][j] = color
#             visited.add((i, j))
#             dfs(i + 1, j, visited)
#             dfs(i - 1, j, visited)
#             dfs(i, j + 1, visited)
#             dfs(i, j - 1, visited)

#         dfs(sr, sc, set())

#         return image

#--------------bfs----------------

# class Solution:
#     def floodFill(
#         self, image: List[List[int]], sr: int, sc: int, color: int
#     ) -> List[List[int]]:

#         m = len(image)
#         n = len(image[0])
#         image_color = image[sr][sc]
#         if image_color == color:
#             return image
#         queue = deque()
#         queue.append((sr, sc))
#         image[sr][sc] = color

#         def bfs(visited):

#             while queue:
#                 x, y = queue.popleft()

#                 directions = [[0, 1],[0, -1],[-1, 0], [1, 0]]

#                 for dx, dy in directions:
#                     nx = x + dx
#                     ny = y + dy
#                     if 0 <= nx < m and 0 <=ny < n and (nx, ny) not in visited and image[nx][ny] == image_color:
#                         image[nx][ny] = color
#                         visited.add((nx, ny))
#                         queue.append((nx, ny))

#         bfs(set())

#         return image

s = Solution()

print(s.floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, color=2))
