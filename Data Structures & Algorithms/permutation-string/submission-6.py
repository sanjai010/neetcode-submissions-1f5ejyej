from itertools import permutations

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1len = len(s1)
        s2len = len(s2)
        if s1len>s2len:
            return False
        s1count = Counter(s1)
        window_count = Counter(s2[0:s1len])
        if s1count == window_count:
            return True
        for i in range(s1len, s2len):
            window_count[s2[i]]+=1
            window_count[s2[i-s1len]]-=1
            if window_count[s2[i-s1len]]==0:
                del window_count[s2[i-s1len]]

            if s1count== window_count:
                return True
        return False
