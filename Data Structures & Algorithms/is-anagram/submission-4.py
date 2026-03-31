class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        x=sorted(s)
        y=sorted(t)
        for i in range(len(s)):
            if x[i]!=y[i]:
                return False
        return True