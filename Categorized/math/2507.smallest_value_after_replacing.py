class Solution:
    def smallestValue(self, n: int) -> int:
        def get_prime_factor(n):
            primes = []
            i = 2
            while i * i <= n:
                if n % i == 0:
                    while(n % i == 0):
                        primes.append(i)
                        n = n // i
                
                i += 1
            if n > 1: primes.append(n)
            return primes

        while True:
            x = get_prime_factor(n)
            total = sum(x)
            if total == n:
                return total
            n = total