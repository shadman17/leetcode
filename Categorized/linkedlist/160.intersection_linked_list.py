from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        a = headA
        b = headB

        while a != b:
            if a is None:
                a = headB
            else:
                a = a.next

            if b in None:
                b = headA
            else:
                b = b.next

        return a


# class Solution:
#     def getIntersectionNode(
#         self, headA: ListNode, headB: ListNode
#     ) -> Optional[ListNode]:
#         hashmap = defaultdict(int)

#         temp = headA
#         while temp:
#             hashmap[temp] = 1
#             temp = temp.next

#         temp2 = headB
#         while temp2:
#             if temp2 in hashmap:
#                 return temp2
#             temp2 = temp2.next

#         return None
