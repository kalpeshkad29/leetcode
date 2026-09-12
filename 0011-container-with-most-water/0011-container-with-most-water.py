class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        left=0
        right=n-1
        maxarea=0
        while  left<right:
            temp=min(height[left],height[right])*(right-left)
            maxarea=max(temp,maxarea)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxarea