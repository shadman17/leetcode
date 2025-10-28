class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        def getsieve(n):
            prime = [1] * n
            prime[0] = prime[1] = 0

            i = 2
            while i * i <= n:
                if prime[i]:
                    for j in range(i * i, n, i):
                        prime[j] = 0

                i += 1
            
            return prime
        
        primearr = getsieve(n)
        count = 0
        for item in primearr:
            if item == 1:
                count += 1
        return count

