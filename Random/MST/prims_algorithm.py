import heapq
class Solution:
    def spanningTree(self, V, edges):
        # code here
        
        adj = [[] for _ in range(V)]
        
        for i in range(len(edges)):
            u, v, wt = edges[i]
            adj[u].append((v, wt))
            adj[v].append((u, wt))
        
        res = 0
        minheap = []
        heapq.heappush(minheap,(0, 0))
        visited = [False] * V
        
        while minheap:
            w, u = heapq.heappop(minheap)
            
            if visited[u]:
                continue
            
            visited[u] = True
            
            res += w
            
            for nei, weight in adj[u]:
                if not visited[nei]:
                    heapq.heappush(minheap, (weight, nei))
                    
        return res