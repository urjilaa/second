# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #finding the middle of the list
        slow = fast = head 
        while fast and fast.next: 
            fast = fast.next.next 
            slow = slow.next 

        #reversing the second half
        prev = None 
        while slow: 
            nxt = slow.next 
            slow.next = prev 
            prev = slow
            slow = nxt 

        #check palindrom
        left, right = head, prev 
        while right: 
            if left.val != right.val: 
                return False 
            left = left.next 
            right = right.next 
        return True 