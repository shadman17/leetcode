import heapq

class Solution:
    def minMaxDist(self, stations, k):
        # Code here
        n = len(stations)
        if n < 2 or k == 0:
            return 0.00 if n < 2 else f"{max(stations[i+1]-stations[i] for i in range(n-1)):.2f}"
        howmany = [0] * (n - 1)
        minHeap = []
        for i in range(n - 1):
            heapq.heappush(minHeap, (-1 * (stations[i+1] - stations[i]), i))
            
        for i in range(k):
            diff, index = heapq.heappop(minHeap)
            howmany[index] += 1
            
            inidiff = stations[index + 1] - stations[index]
            newdiff = inidiff / (howmany[index] + 1)
            heapq.heappush(minHeap, (-1 * (newdiff), index))
        
        ans = -minHeap[0][0]
        return round(ans, 2)