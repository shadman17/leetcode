# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:

        result = ""
        cur = head
        while cur:
            result += str(cur.val)
            cur = cur.next

        print(result)
        decimal = int(result, 2)
        return decimal
