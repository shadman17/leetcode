class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return - 1
        minimum, maximum = float('inf'), float("-inf")

        for i in range(len(bloomDay)):
            if bloomDay[i] > maximum:
                maximum = bloomDay[i]
            if bloomDay[i] < minimum:
                minimum = bloomDay[i]

        def makebouquet(arr, day, m, k):
            count, bouquet = 0, 0

            for i in range(len(arr)):
                if arr[i] <= day:
                    count += 1

                else:
                    bouquet += count // k
                    count = 0

            bouquet += count // k
            return bouquet >= m


        l, h, ans = minimum, maximum, maximum

        while (l <= h):
            mid = (l+h) // 2

            if makebouquet(bloomDay, mid, m, k) == True:
                h = mid - 1
                ans = mid
            else:
                l = mid + 1
        
        return ans



