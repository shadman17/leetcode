class Solution:
    def aggressiveCows(self, stalls, k):
        # code here
        def can_we_place(arr, dist, cows):
            last = arr[0]
            cowscount = 1
            for i in range(1, len(arr)):
                if arr[i] - last >= dist:
                    cowscount += 1
                    last = arr[i]
                
                if cowscount == cows:
                    return True
                    
            return False
        
        stalls.sort()
        
        low = 0
        high = stalls[-1] - stalls[0]
        
        while low <= high:
            mid = (low + high) // 2
            
            if can_we_place(stalls, mid, k) == True:
                low = mid + 1
            else:
                high = mid - 1
        
        return high
                