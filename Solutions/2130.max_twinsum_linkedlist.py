# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:
#     def pairSum(self, head: Optional[ListNode]) -> int:
#         arr = []

#         cur = head
#         while cur:
#             arr.append(cur.val)
#             cur = cur.next


#         i, j = 0, len(arr) - 1
#         result = 2
#         while i < j:
#             result = max(result, arr[i] + arr[j])
#             i += 1
#             j -= 1

#         return result 

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        res = 0
        while prev:
            res = max(res, prev.val + slow.val)
            prev = prev.next
            slow = slow.next
        
        return res


def list_to_linkedlist(values):
    """Convert a list to a linked list."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linkedlist_to_list(head):
    """Convert a linked list back to a list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def test():
    sol = Solution()

    # Test Case 1
    head = list_to_linkedlist([4,2,2,3])
    print(sol.pairSum(head))

test()