# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mylist=[]
        while head:
            mylist.append(head.val)
            head=head.next
        mylist2=mylist[::-1]
        if mylist2==mylist:
            return True
        else:
            return False

        