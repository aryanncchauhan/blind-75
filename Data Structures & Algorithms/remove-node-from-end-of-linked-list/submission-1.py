# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next

        print(f"size: {size}")

        if size == n:
            return head.next

        curr = head
        i = size - n
        print(f"i: {i}")
        while curr:
            i -= 1
            if i == 0: 
                if curr.next:
                    curr.next = curr.next.next
                break
            curr = curr.next

        return head