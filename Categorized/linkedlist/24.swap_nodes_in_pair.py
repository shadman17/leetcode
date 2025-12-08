# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prev = dummy
        cur = head

        while cur and cur.next:
            nextpair = cur.next.next
            nextnode = cur.next
            cur.next = nextpair
            nextnode.next = cur

            prev.next = nextnode

            prev = cur
            cur = cur.next

        return dummy.next
        