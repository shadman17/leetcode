from typing import List

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,start,end):
        
        combined = list(zip(start, end))
        combined.sort(key=lambda x: (x[1], x[0]))
        
        count = 1
        freetime = combined[0][1]
        for i in range(len(combined)):
            start, end = combined[i]
            
            if start > freetime:
                count += 1
                freetime = end
        return count
        
s = Solution()
print(s.maximumMeetings([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]))
