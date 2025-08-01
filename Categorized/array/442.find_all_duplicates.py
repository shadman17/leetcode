class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        dict1 = {}

        for val in nums:
            dict1[val] = dict1.get(val, 0) + 1

        for key, value in dict1.items():
            if value == 2:
                result.append(key)

        return result


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = []
        length = len(nums)
        for i in range(length):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                output.append(index + 1)

            nums[index] *= -1

        return output
