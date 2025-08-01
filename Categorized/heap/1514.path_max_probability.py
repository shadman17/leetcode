class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        visit = set()
        maxHeap = [(-1, start_node)]
        for i in range(len(edges)):
            src, dest = edges[i]
            adj[src].append((dest, succProb[i]))
            adj[dest].append((src, succProb[i]))
        
        while maxHeap:
            prob, cur  = heapq.heappop(maxHeap)
            visit.add(cur)
            if cur == end_node:
                return -prob

            for cur2, prob2 in adj[cur]:
                if cur2 not in visit:
                    heapq.heappush(maxHeap, (prob*prob2, cur2))
        return 0.0

