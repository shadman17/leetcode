class Solution:
    def median(self, mat):
    	
    	def upperBound(arr, target):
            low, high = 0, len(arr) - 1
            answer = len(arr)
            
            while low <= high:
                mid = low + (high - low) // 2
                
                if target < arr[mid]:
                    answer = mid
                    high = mid - 1
                
                else:
                    low = mid + 1
    
            return answer

        def countNumber(mat, r, c, mid):
            count = 0
            for i in range(r):
    	        count += upperBound(mat[i], mid)
            return count
    	
        l = float("inf")
        h = float("-inf")
    	r = len(mat)
    	c = len(mat[0])
    	
    	for i in range(r):
    	    l = min(l, mat[i][0])
    	    h = max(h, mat[i][c-1])
    	    
        req = (r*c) // 2
        
        while l <= h:
            mid = (l + h) // 2
            count = countNumber(mat, r, c, mid)
            if count <= req:
                l = mid + 1
            else:
                h = mid - 1
        
        return l
                