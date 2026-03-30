class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        n=len(nums)
        for i in range(0,n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    for l in range(k+1,n):
                        fsum = nums[i]+nums[j]+nums[k]+nums[l]
                        if fsum== target:
                            fsum =[nums[i],nums[j],nums[k],nums[l]]
                            fsum.sort()
                            if fsum not in result:
                                result.append(fsum)
        return result