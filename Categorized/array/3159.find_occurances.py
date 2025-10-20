class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        
        indices = []
        for i in range(len(nums)):
            if nums[i] == x:
                indices.append(i)
        result = []
        for query in queries:
            if len(indices) < query:
                result.append(-1)
            else:
                result.append(indices[query - 1])

        return result