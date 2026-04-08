class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        n= len(height)
        for i in range(0,n):
            left = max(height[0:i+1])
            right = max(height[i:])
            water += min(left,right)- height[i]
        return water 

        