# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        countA = 0 
        countB = 0
        currA = headA
        currB = headB
        while currA: #finding the length of headA
            countA += 1
            currA = currA.next
        while currB: #finding the length of headB
            countB += 1
            currB = currB.next
            
        currA1 = headA
        currB1 = headB
        while countA > countB:
            countA -= 1
            currA1 = currA1.next
        while countB > countA:
            countB -= 1
            currB1 = currB1.next
        while currA1 != currB1:
            currA1 = currA1.next
            currB1 = currB1.next

        return currA1
