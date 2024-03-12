# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        parts = length//k
        rem = length % k
        res = []
        curr = head
        for i in range(k):
            if i < rem:
                size = parts+1
            else:
                size = parts
            temp=curr
            for j in range(size-1):
                if curr:
                    curr = curr.next
            if curr:
                next_node = curr.next
                curr.next = None
                curr = next_node
            res.append(temp)
        return res