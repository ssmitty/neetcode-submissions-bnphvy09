class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        sety=set()
        l=0
        sety.add(s[l])
        print(sety)
        r=1
        maxi=1
        while r<len(s):
            while s[r] in sety:
                sety.remove(s[l])
                l+=1
            sety.add(s[r])
            r+=1
            maxi=max(maxi,r-l)
        return maxi

        