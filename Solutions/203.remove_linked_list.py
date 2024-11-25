from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        while head and head.val == val:
            head = head.next
        
        a = head

        while a and a.next:
            if a.next.val == val:
                a.next = a.next.next

            else:
                a = a.next

        return head

# class Solution:
#     def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
#         dummy = ListNode(0)
#         dummy.next = head
#         current = dummy
        
#         while current and current.next:
#             if current.next.val == val:
#                 current.next = current.next.next
#             else:
#                 current = current.next
        
#         return dummy.next


def toLinkedList(lst):
    if not lst:
        return None
    
    head = ListNode(lst[0])
    current = head

    for i in range(1, len(lst)):
        current.next = ListNode(lst[i])
        current = current.next

    return head

def toList(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result

s = Solution()
linkedlist1 = toLinkedList([1,1,1,1])
removedlist = s.removeElements(linkedlist1, val = 1)

output = toList(removedlist)
print(output)