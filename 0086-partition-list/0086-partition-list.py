# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small=ListNode(0)
        large=ListNode(0)
        smalltail=small
        largetail=large
        temp=head
        while temp:
            if temp.val<x:
                smalltail.next=temp
                smalltail=smalltail.next
            else:
                largetail.next=temp
                largetail=largetail.next
            temp=temp.next
        largetail.next=None
        smalltail.next=large.next
        return small.next
        