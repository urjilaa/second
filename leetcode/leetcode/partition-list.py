# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        first = ListNode(0)
        last = ListNode(0)

        before_curr = first
        after_curr = last
        
        while head:
            if head.val < x:
                before_curr.next, before_curr = head, head
            else:
                after_curr.next, after_curr = head, head
            head = head.next
        
        after_curr.next = None
        before_curr.next = last.next
        
        return first.next