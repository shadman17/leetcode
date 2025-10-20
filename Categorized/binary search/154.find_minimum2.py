class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1
        ans = float('inf')
        while l <= h:
            mid = (l + h) // 2

            if nums[l] == nums[h]:
                ans = min(ans, min(nums[l],nums[mid]))
                l += 1
                h -= 1
                continue

            if nums[l] <= nums[mid]:

                ans = min(ans, nums[l])
                l = mid + 1

            else:
                ans = min(ans, nums[mid])
                h = mid - 1
        return ans
    
    
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        # Early exit if strictly increasing (no rotation in current window)
        if nums[l] < nums[r]:
            return nums[l]

        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                # Min is in [l, mid]
                r = mid
            elif nums[mid] > nums[r]:
                # Min is in (mid, r]
                l = mid + 1
            else:
                # nums[mid] == nums[r]: can't tell; drop a duplicate on the right
                r -= 1
        return nums[l]
