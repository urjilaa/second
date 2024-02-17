# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], i: int, j: int) -> Optional[ListNode]:
        if i == j or head == None or head.next == None:
            return head
        
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        
        for _ in range(i - 1):
            prev = prev.next
        current = prev.next
        next_node = current.next

        for _ in range(j - i):
            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
            next_node = current.next
        
        return dummy.next