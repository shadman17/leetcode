class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def get_prime_factor(n):
            primes = []
            i = 2
            while i * i <= n:
                if n % i == 0:
                    primes.append(i)

                    while(n % i == 0):
                        n = n // i
                
                i += 1
            if n > 1: primes.append(n)
            return primes

        hashset = set()
        for i in range(len(nums)):
            x = get_prime_factor(nums[i])
            for val in x:
                hashset.add(val)

        return len(hashset)