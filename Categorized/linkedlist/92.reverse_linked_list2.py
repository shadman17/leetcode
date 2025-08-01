# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        dummy = ListNode(-501)
        dummy.next = head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        temp = prev.next
        # after = temp.next

        for _ in range(right-left):
            after = temp.next
            temp.next = after.next
            after.next = prev.next
            prev.next = after

        return dummy.next
    
def linkedlist_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next

    return result

def list_to_linkedlist(result):
    head = ListNode(result[0])
    current = head

    for val in result[1:]:
        current.next = ListNode(val)
        current = current.next 

    return head   

def print_list(head):
    while head:
        print(head.val)
        head = head.next


s = Solution()
p = list_to_linkedlist([1,2,3,4,5])
q = s.reverseBetween(p, 2,4)
print(linkedlist_to_list(q))