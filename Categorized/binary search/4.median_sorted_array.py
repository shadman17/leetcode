# Brute Force
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0

        new_arr = []
        while(i < len(nums1) and j < len(nums2)):
            if nums1[i] < nums2[j]:
                new_arr.append(nums1[i])
                i += 1

            else:
                new_arr.append(nums2[j])
                j += 1

        while i < len(nums1):
            new_arr.append(nums1[i])
            i += 1

        while j < len(nums2):
            new_arr.append(nums2[j])
            j += 1

        if len(new_arr) % 2 != 0:
            return new_arr[len(new_arr) // 2]
        else:
            total = new_arr[len(new_arr) // 2 - 1] + new_arr[len(new_arr) // 2]
            return total / 2

# Binary Search
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        n1 = len(A)
        n2 = len(B)
        total = n1 + n2
        left = (n1 + n2 + 1) // 2

        if n1 > n2:
            A, B = B, A

        low, high = 0, len(A)
        while (low <= high):
            mid1 = (low + high) // 2
            mid2 = left - mid1

            l1 = A[mid1 - 1] if mid1 - 1 >= 0 else float("-inf")
            l2 = B[mid2 - 1] if mid2 - 1 >= 0 else float("-inf")
            r1 = A[mid1] if mid1 < len(A) else float("inf")
            r2 = B[mid2] if mid2 < len(B) else float("inf")

            if l1 <= r2 and l2 <= r1:
                if total % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return max(l1, l2)
            
            elif l2 > r1:
                low = mid1 + 1
            else:
                high = mid1 - 1