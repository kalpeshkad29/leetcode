# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        arr=[]
        
        temp=head
        while temp:
            arr.append(temp.val)
            temp=temp.next
            
        n=len(arr)
        result=[0]*n
        stack=[]
        for i in range(n):
            while stack and arr[i]>arr[stack[-1]]:
                idx=stack.pop()
                result[idx]=arr[i]
            stack.append(i)
           
                    
        return result
        

        