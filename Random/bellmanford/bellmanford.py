class Solution:
    def bellmanFord(self, V, edges, src):
        #code here
        INF = 10**8
        dist = [INF] * V
        dist[src] = 0
        
        # Relax v-1 times
        for i in range(V - 1):
            for u, v, w in edges:
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    
        # if edges can be relaxed after v-1 times, that means there is a negative cycle exist!
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                return [-1]
                
        return dist