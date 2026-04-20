class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red=[]
        green=[]
        blue=[]
        for i in range(len(nums)):
            if nums[i]==0:
                red.append(0)
            elif nums[i]==1:
                green.append(1)
            else: 
                blue.append(2)

        nums[:]= red+green+blue