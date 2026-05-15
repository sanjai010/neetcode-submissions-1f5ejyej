class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a= sorted(s)
        b= sorted(t)

        if a!=b:
            return False
        return True
        