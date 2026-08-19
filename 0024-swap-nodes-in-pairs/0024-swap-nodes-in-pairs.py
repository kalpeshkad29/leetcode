# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        prev=dummy
        dummy.next=head
        while head and head.next:
            prev.next=head.next
            head.next=head.next.next
            prev.next.next=head

            prev=head
            head=head.next
        return dummy.next

        