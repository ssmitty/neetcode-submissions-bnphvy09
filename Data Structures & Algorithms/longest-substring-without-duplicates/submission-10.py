class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        length=0
        l=0
        r=1
        duplicate={}
        duplicate[s[l]]=1
        while r<len(s):
            if s[r] in duplicate:
                print(s[r])
                if length<r-l:
                    print(r-l)
                    length=r-l
                l+=1
                r=l+1
                duplicate={s[l]: 1}
            else:
                duplicate[s[r]]=1
                r+=1
        if r-l>length:
            length=r-l        
        return length
        