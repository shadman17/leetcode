from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        current = dummy

        while list1 and list2:

            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next

            else:
                current.next = list2
                list2 = list2.next

            current = current.next
        
        current.next = list1 if list1 else list2

        return dummy.next
    

def toLinkedList(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head

    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def toList(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    
    return result

s = Solution()
linkedlist1 = toLinkedList([1,2,4])
linkedlist2 = toLinkedList([1,3,4])
mergedlist = s.mergeTwoLists(linkedlist1, linkedlist2)
output = toList(mergedlist)
print(output)