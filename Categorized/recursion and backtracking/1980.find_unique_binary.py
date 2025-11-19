class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])

        def backtrack(arr):
            new_string = ""
            if n == len(arr):
                new_string += "".join(arr)
                if new_string not in nums:
                    return new_string

                return

            for i in ["0", "1"]:
                arr.append(i)
                candidate = backtrack(arr)
                if candidate:
                    return candidate
                arr.pop()

        return backtrack([])


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def generate(curr):
            if len(curr) == n:
                if curr not in nums:
                    return curr

                return ""

            add_zero = generate(curr + "0")
            if add_zero:
                return add_zero

            add_one = generate(curr + "1")
            if add_one:
                return add_one

        n = len(nums)
        nums = set(nums)
        return generate("")


s = Solution()
print(s.findDifferentBinaryString(nums=["01", "10"]))
print(s.findDifferentBinaryString(nums=["111", "011", "001"]))
