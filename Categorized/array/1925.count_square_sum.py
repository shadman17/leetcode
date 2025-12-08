class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                result = math.sqrt((i * i) + (j * j))
                if result == int(result) and result <= n:
                    count += 1

        return count 
