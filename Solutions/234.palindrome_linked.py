from typing import Optional

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        result = []
        while head:
            result.append(head.val)
            head = head.next
        
        return result == result[::-1]