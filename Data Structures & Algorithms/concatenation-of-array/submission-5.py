class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        temp = []
        n=2
        for i in range(n):
            for j in nums:
                temp.append(j)
        return temp