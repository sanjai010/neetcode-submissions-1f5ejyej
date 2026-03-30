class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        if not arr:
            return 0
        k=1
        for i in range(1,len(arr)):
            if arr[i]!=arr[i-1]:
                arr[k]=arr[i]
                k+=1
        return k
        


        