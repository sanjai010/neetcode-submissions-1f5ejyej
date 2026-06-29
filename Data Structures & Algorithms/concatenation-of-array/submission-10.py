class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        tem = []
        n=2
        for i in range(n):
            for j in nums:
                tem.append(j)
        return tem

        