class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_pos(l, h, arr, target):
            ans = -1
            while l <= h:
                mid = (l + h) // 2
                
                if arr[mid] == target:
                    ans = mid
                    h = mid - 1
                elif arr[mid] > target:
                    h = mid - 1
                else:
                    l = mid + 1
            return ans

        def higher_pos(l, h, arr, target):
            ans = -1
            while l <= h:
                mid = (l + h) // 2

                if arr[mid] == target:
                    ans = mid
                    l = mid + 1
                
                elif arr[mid] < target:
                    l = mid + 1

                else:
                    h = mid - 1
            return ans

        low = lower_pos(0, len(nums)-1, nums, target)
        high = higher_pos(0, len(nums)-1, nums, target)
        
        if low == -1 or high == -1:
            return [-1, -1]
        return [low, high]