class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hashet=set()
     
        l=0
        maxstring=0
        #okay we get length for index l then we move up one and set r=l+1
        #we go through array check each element to the right and add to set if it isnt already in the list. Once it is
        # whe shrink list to
        for r in range(len(s)):
            while s[r] in hashet:
                print(hashet)
                hashet.remove(s[l])
                l+=1
            hashet.add(s[r])
            maxstring=max(maxstring,len(hashet))

        return maxstring