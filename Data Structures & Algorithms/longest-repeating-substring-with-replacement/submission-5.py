class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charset={}
        l=0
        r=0
        res=0
        while r <(len(s)):
            if s[r] not in charset:
                charset[s[r]]=1
            else:
                charset[s[r]]+=1
            while r-l+1-max(charset.values())>k:
                charset[s[l]]-=1
                l+=1  
            res=max(r-l+1,res)
            r+=1 
        return res