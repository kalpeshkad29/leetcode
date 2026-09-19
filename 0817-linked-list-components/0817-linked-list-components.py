# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode | None, nums: list[int]) -> int:
        count=0
        curr=head
        num_set=set(nums)
        while curr:
            if curr.val in num_set and (curr.next is None or curr.next.val not in num_set):
                count+=1
            curr=curr.next
        return count

        