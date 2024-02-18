# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        #curr = head
        count = 0
        while head:
            count += 1
            head = head.next

        count -= n
        prev = dummy
        for i in range(0, count):
            prev = prev.next
        prev.next = prev.next.next

        return dummy.next