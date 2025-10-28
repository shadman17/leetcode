# Given a number n, find all prime numbers less than or equal to n.
class Solution:
    def sieve(self, n):
        prime = [1] * (n + 1)
        
        p = 2
        
        while p * p <= n:
            if prime[p]:
                for i in range(p * p, n + 1, p):
                    prime[i] = 0
                    
            p += 1
            
        res = []
        for p in range(2, n +1):
            id prime[p]:
                res.append(p)
                
        return res
    
s = Solution
print(s.sieve(35))