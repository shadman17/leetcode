# Left and right count
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [0] * n
        right = [0] * n
        left[0] = 1
        right[n-1] = 1
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1] + 1
            else:
                left[i] = 1

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right[i] = right[i+1] + 1
            else:
                right[i] = 1
        summ = 0
        for i in range(n):
            summ += max(left[i], right[i])
        
        return summ
    
# Do a slope intuition, O(1) space
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        summ = 1
        i = 1
        while i < n:
            while i < n and ratings[i] == ratings[i-1]:
                summ += 1
                i += 1
                continue
            peak = 1
            while i < n and ratings[i] > ratings[i-1]:
                peak += 1
                summ += peak
                i += 1
            down = 1
            while i < n and ratings[i] < ratings[i-1]:
                summ += down
                i += 1
                down += 1

            if down > peak:
                summ += down - peak
        
        return summ