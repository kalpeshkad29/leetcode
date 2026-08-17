# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        mylist=[]
        temp=head
        while temp:
            mylist.append(temp.val)
            temp=temp.next
        n=len(mylist)
        max_sum=0
        left=0
        right=len(mylist)-1
        while left<right:
            sum=mylist[left]+mylist[right]
            max_sum=max(max_sum,sum)
            left+=1
            right-=1
        return max_sum


       


        