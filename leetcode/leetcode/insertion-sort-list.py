# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr:
            new_curr = head
            while new_curr != curr:
                if new_curr.val > curr.val:
                    new_curr.val, curr.val = curr.val, new_curr.val
                new_curr = new_curr.next
            curr = curr.next
        return head
