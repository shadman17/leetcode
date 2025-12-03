from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def addTwoNumbers(
#         self, l1: Optional[ListNode], l2: Optional[ListNode]
#     ) -> Optional[ListNode]:
#         temp1 = l1
#         temp2 = l2
#         s1 = ""
#         s2 = ""

#         while temp1 != None:
#             s1 += str(temp1.val)
#             temp1 = temp1.next

#         while temp2 != None:
#             s2 += str(temp2.val)
#             temp2 = temp2.next

#         s1 = s1[::-1]
#         s2 = s2[::-1]

#         sum1 = int(s1) + int(s2)

#         sum1 = str(sum1)
#         list1 = list(sum1[::-1])

#         for i in range(len(list1)):
#             list1[i] = int(list1[i])

#         head = ListNode(list1[0])
#         current = head

#         for value in list1[1:]:
#             current.next = ListNode(value)
#             current = current.next

#         return head


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


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        cur = dummy = ListNode(0)
        t1, t2 = l1, l2

        while t1 or t2:
            summ = carry
            summ += t1.val if t1 else 0
            summ += t2.val if t2 else 0

            carry = summ // 10
            summ = summ % 10

            cur.next = ListNode(summ)
            cur = cur.next

            t1 = t1.next if t1 else None
            t2 = t2.next if t2 else None

        if carry:
            cur.next = ListNode(carry)

        return dummy.next


l1 = toLinkedList([2, 4, 3])
l2 = toLinkedList([5, 6, 4])
s = Solution()
x = s.addTwoNumbers(l1, l2)
print(toList(x))
