class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        res = []
        i = 0
        while i < n and intervals[i][1] < newInterval[0]: # Check the portion before the merge
            res.append(intervals[i])
            i += 1
        
        while i < n and intervals[i][0] <= newInterval[1]: # Need to merge the interval
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        
        res.append(newInterval)
        while i < n: # After merging, add the rest of the interval
            res.append(intervals[i])
            i += 1

        return res