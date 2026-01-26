class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        res = []
        n = len(arr)
        arr.sort()
        mini = float("inf")

        for i in range(1, n):
            mini = min((arr[i] - arr[i - 1]), mini)

        for i in range(n - 1):
            if arr[i] + mini == arr[i + 1]:
                res.append([arr[i], arr[i + 1]])

        return res
