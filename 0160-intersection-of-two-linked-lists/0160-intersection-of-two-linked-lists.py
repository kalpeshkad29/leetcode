# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        myset=set()
        curr=headA
        newcurr=headB
        while curr:
            myset.add(curr)
            curr=curr.next
        while newcurr:
            if newcurr in myset:
                return newcurr
            myset.add(newcurr)
            newcurr=newcurr.next




            


        