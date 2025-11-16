class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        length = len(s)
        cons, res = 0, 0
        if s[0] == "1":
            cons = 1
            res = 1
        for i in range(1, length):
            if s[i] == "1" and s[i-1] == "1":
                cons += 1
                res += cons % MOD
            elif s[i] == "1" and s[i-1] == "0":
                cons = 1
                res += cons % MOD
            else:
                cons = 0
        return res % MOD
            
            
# Simplified
class Solution:
class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        length = len(s)
        cons, res = 0, 0
        for i in range(length):
            if s[i] == "1":
                cons += 1
                res = (res + cons) % MOD
            else:
                cons = 0
        return res
            
                