class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort based on the end range
        intervals.sort(key=lambda x: (x[1], x[0]))
        n = len(intervals)
        count = 1 # There will be atleast one
        lastrange = intervals[0][1]
        for i in range(n):
            start, end = intervals[i]
            
            if start >= lastrange: # if the next range is less than/equal to the previous one, I can count this range as well
                count += 1
                lastrange = end # end is the last one now
        return n - count # return the ones that can not be taken