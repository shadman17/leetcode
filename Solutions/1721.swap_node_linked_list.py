# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = second = head
        for _ in range(1, k):
            first = first.next
        
        new_node = first
        while new_node.next:
            second = second.next
            new_node = new_node.next

        
        first.val, second.val = second.val, first.val

        return head
    
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
q = s.swapNodes(p, 2)
print(linkedlist_to_list(q))