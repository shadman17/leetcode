class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        diff = high - low
        if high % 2 == 1 and low % 2 == 1:
            return math.ceil(diff / 2) + 1
        return math.ceil(diff / 2)