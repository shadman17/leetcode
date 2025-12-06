# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            temp = head
            while temp:
                after = temp.next
                temp.next = prev
                prev = temp
                temp = after
            
            return prev

        def findkthnode(temp, k):
            count = 1
            while temp:
                temp = temp.next
                count += 1
                if count == k:
                    return temp
                elif count > k:
                    return None



        temp = head
        prevnode = None
        while temp:
            kthnode = findkthnode(temp, k)
            if kthnode is None:
                if prevnode:
                    prevnode.next = temp
                break

            nextnode = kthnode.next
            kthnode.next = None
            reverse(temp)

            if temp == head:
                head = kthnode
            
            else:
                prevnode.next = kthnode
            
            prevnode = temp
            temp = nextnode
            
        return head
        
