class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=""
        right=""
        i=0
        while i< len(s):
            if s[i].isalnum():
                left+=s[i].lower()
            i+=1
        for j in range(len(s)-1,-1,-1):
            if s[j].isalnum():
                right+=s[j].lower()
        return right==left



