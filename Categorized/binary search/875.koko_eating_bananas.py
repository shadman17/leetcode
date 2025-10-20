class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maximum = -1
        for i in range(len(piles)):
            if piles[i] > maximum:
                maximum = piles[i]
        low = 1
        high = maximum
        ans = maximum
        while low <= high:
            mid = (low + high) // 2

            time = 0
            for i in range(len(piles)):
                time += math.ceil(piles[i] / mid)          
            
            if time <= h:
                ans = mid
                high = mid - 1 

            else:
                low = mid + 1

        return ans