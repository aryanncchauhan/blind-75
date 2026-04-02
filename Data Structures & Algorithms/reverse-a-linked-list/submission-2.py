# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
            
        prev = None
        curr = head
        post = curr.next

        while post is not None:            
            curr.next = prev

            prev = curr
            curr = post
            post = curr.next

        curr.next = prev
        
        return curr