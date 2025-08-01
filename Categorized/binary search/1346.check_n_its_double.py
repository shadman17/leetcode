from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        length = len(arr)
        for i in range(length):
            target = 2 * arr[i]
            low, high = 0, length - 1
            while low <= high:
                mid = low + (high - low) // 2

                if arr[mid] == target and mid != i:
                    return True

                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

        return False


s = Solution()
# print(s.checkIfExist(arr=[10, 2, 5, 3]))
# print(s.checkIfExist(arr=[-10, 12, -20, -8, 15]))
print(s.checkIfExist(arr=[-2, 0, 10, -19, 4, 6, -8]))
