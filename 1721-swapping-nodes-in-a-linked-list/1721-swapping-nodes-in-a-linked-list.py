# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        my_arr=[]
        while head:
            my_arr.append(head.val)
            head=head.next
        n=len(my_arr)
        my_arr[k-1],my_arr[n-k]=my_arr[n-k],my_arr[k-1]
        dummy=ListNode(0)
        curr=dummy
        for num in my_arr:
            curr.next=ListNode(num)
            curr=curr.next
        return dummy.next

        