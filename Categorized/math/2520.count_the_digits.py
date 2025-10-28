class Solution:
    def countDigits(self, num: int) -> int:
        hashmap = {}
        n = num
        while n != 0:
            remainder = n % 10
            hashmap[remainder] = hashmap.get(remainder, 0) + 1
            n = n // 10
        
        answer = 0
        for key, value in hashmap.items():
            if num % key == 0:
                answer += value

        return answer
