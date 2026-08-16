class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        sety={}
        maxi=0
        for r in range(len(s)):
            sety[s[r]]=sety.get(s[r],0)+1
            while r-l+1-max(sety.values())>k:
                sety[s[l]]-=1
                l+=1
            maxi=max(maxi,r-l+1)
        return maxi
            


        