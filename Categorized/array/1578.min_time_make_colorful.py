class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        l, r = 0, 1
        ans = 0

        while r < len(colors):
            if colors[l] == colors[r]:
                if neededTime[l] < neededTime[r]:
                    ans += neededTime[l]
                    l = r
                else:
                    ans += neededTime[r]
            else:
                l = r
            r += 1
        return ans