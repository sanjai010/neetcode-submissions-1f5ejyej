class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        n=len(nums)
        for i in range(0,n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    sum = nums[i]+nums[j]+nums[k]
                    if sum==0:
                        sum =[nums[i],nums[j],nums[k]]
                        sum.sort()
                        if sum not in result:
                            result.append(sum)
        return result
        