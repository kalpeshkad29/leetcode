# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        mid=slow.next
        slow.next=None
        left=self.sortList(head)
        right=self.sortList(mid)
        dummy=ListNode(0)
        prev=dummy
        while left and right:
            if left.val<right.val:
                prev.next=left
                left=left.next
            else:
                prev.next=right
                right=right.next
            prev=prev.next
        if left is not None:
            prev.next=left
        if right is not None :
            prev.next=right
        return dummy.next


        
        