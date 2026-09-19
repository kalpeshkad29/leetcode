# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        my_set=set()
        temp1=headA
        temp2=headB
        while temp1:
            my_set.add(temp1)
            temp1=temp1.next
        while temp2:
            if temp2 in my_set:
                return temp2
            else:
                my_set.add(temp2)
            temp2=temp2.next





            


        