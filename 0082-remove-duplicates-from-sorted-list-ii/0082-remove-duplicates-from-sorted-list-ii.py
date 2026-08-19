# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        prev=dummy

        dummy.next=head
        
        while head and head.next:
            if head.val==head.next.val:
                dup=head.val
                while head and head.val==dup:
                    head=head.next
                prev.next=head
            else:
                prev=head
                head=head.next
        return dummy.next

        