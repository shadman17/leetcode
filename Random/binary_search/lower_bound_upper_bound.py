class Solution:
    def lowerBound(self, arr, target):
        # smallest index where arr[i] >= target
        low, high = 0, len(arr) - 1
        answer = len(arr)
        
        while low <= high:
            mid = low + (high - low) // 2
                
            if target <= arr[mid]:
                answer = mid
                high = mid - 1
                
            else:
                low = mid + 1
                
        return answer

    def upperBound(self, arr, target):
        # smallest index where arr[i] > target

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