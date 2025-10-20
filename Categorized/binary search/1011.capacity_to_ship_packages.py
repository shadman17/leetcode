class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def countweight(weights, value):
            count, answer = 0, 1

            for i in range(len(weights)):
                
                count += weights[i]
                if count > value:
                    answer += 1
                    count = weights[i]
            
            return answer

        l = max(weights)
        h = sum(weights)
        ans = -1
        while l <= h:
            mid = (l + h) // 2

            count = countweight(weights, mid)
            if count > days:
                l = mid + 1
                
            else:
                ans = mid
                h = mid - 1
                
        return ans