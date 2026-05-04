class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red=[]
        blue=[]
        white=[]
        for i in range(len(nums)):
            if nums[i]==0:
                red.append(0)
            elif nums[i] ==1:
                blue.append(1)
            else:
                white.append(2)
        nums [:]= red+blue+white
        