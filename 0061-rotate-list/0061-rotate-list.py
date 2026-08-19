# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        # find length and last node
        temp = head
        count = 1

        while temp.next:
            temp = temp.next
            count += 1

        k = k % count

        if k == 0:
            return head

        # make circular
        temp.next = head

        steps = count - k
        newtail = head

        while steps > 1:
            newtail = newtail.next
            steps -= 1

        newhead = newtail.next
        newtail.next = None

        return newhead

        