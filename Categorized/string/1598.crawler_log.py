class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for x in logs:
            if x == "../":
                count = max(0, count - 1)

            elif x == "./":
                continue

            else:
                count += 1

        return count
