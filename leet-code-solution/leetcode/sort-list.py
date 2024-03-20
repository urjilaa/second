# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        def merge(node1, node2):
            head = None
            if node1.val < node2.val:
                head = node1
                node1 = node1.next
                head.next = None
            else:
                head = node2
                node2 = node2.next
                head.next = None

            tail = head
            while node1 and node2:
                if node1.val < node2.val:
                    tail.next = node1
                    node1 = node1.next
                    tail = tail.next
                    tail.next = None
                else:
                    tail.next = node2
                    node2 = node2.next
                    tail = tail.next
                    tail.next = None
                
            if node1:
                tail.next = node1
            else:
                tail.next = node2
            
            return head

        def div(node):
            if not node.next:
                return node

            if not node.next.next:
                node2 = node.next
                node.next = None
            else:
                fast = slow = node
                while fast and fast.next:
                    slow = slow.next
                    fast = fast.next.next
                node2 = slow.next
                slow.next = None

            left = div(node)
            right = div(node2)

            return merge(left, right)

        return div(head)

