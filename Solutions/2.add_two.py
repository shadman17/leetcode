from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2
        s1 = ''
        s2 = ''

        while temp1 != None:
            s1 += str(temp1.val)
            temp1 = temp1.next

        while temp2 != None:
            s2 += str(temp2.val)
            temp2 = temp2.next

        s1 = s1[::-1]
        s2 = s2[::-1]

        sum1 = int(s1) + int(s2)

        sum1 = str(sum1)
        list1 = list(sum1[::-1])

        for i in range(len(list1)):
            list1[i] = int(list1[i])

        head = ListNode(list1[0])
        current = head

        for value in list1[1:]:
            current.next = ListNode(value)
            current = current.next

        return head
    
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



l1 = toLinkedList([2,4,3])
l2 = toLinkedList([5,6,4])
s = Solution()
print(s.addTwoNumbers(l1, l2))