# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        new = dummy = ListNode(0)
       
        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next
        #while list1 or list2:
        #    dummy.next = list1
        #    list1 = list1.next
        #    dummy.next = list2
        #    list2 = list2.next
        dummy.next = list1 or list2
        return new.next
