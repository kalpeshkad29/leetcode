# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mystack=[]
        while head:
            mystack.append(head.val)
            head=head.next
        carry=0
        while mystack or carry:
            total=carry
            if mystack:
                total+=mystack.pop()*2
            carry=total//10
            digit=total%10
            node=ListNode(digit)
            node.next=head
            head=node
        return head


        