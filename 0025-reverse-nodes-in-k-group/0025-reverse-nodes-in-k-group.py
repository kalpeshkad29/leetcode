# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        myarr=[]
        while head:
            myarr.append(head.val)
            head=head.next
        n=len(myarr)
        for i in range(0,n,k):
            if i+k<=n:
                myarr[i:i+k]=myarr[i:i+k][::-1]
        dummy=ListNode(0)
        curr=dummy
        for num in myarr:
            curr.next=ListNode(num)
            curr=curr.next
        return dummy.next


        