# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge2list(head1, head2):
            dummy = ListNode(-1)
            temp = dummy

            while head1 and head2:
                if head1.val < head2.val:
                    temp.next = head1
                    head1 = head1.next

                else:
                    temp.next = head2
                    head2 = head2.next

                temp = temp.next

            temp.next = head1 if head1 else head2

            return dummy.next

        def findmiddle(head):
            if not head or not head.next:
                return head

            slow = fast = head
            fast = fast.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            return slow

        def mergesort(head):
            if head is None or head.next is None:
                return head

            middle = findmiddle(head)
            lefthead, righthead = head, middle.next

            middle.next = None
            lefthead = mergesort(lefthead)
            righthead = mergesort(righthead)

            return merge2list(lefthead, righthead)

        return mergesort(head)