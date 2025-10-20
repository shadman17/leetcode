class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1

        while l <= h:
            mid = (l + h) // 2
            if nums[l] == nums[h]:
                return nums[l]

            if nums[mid] == nums[mid - 1]:
                if ((mid - 1 - l) % 2) == 0:
                    l = mid + 1
                else:
                    h = mid - 2
            
            elif nums[mid] == nums[mid + 1]:
                if ((h - mid - 1) % 2) == 0:
                    h = mid - 1
                else:
                    l = mid + 2
            
            else:
                return nums[mid]
