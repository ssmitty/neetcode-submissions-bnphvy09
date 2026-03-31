class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=len(s)-1
        poo=""
        y=0
        q=""
        while x>=0 :
            if s[y] not in "?!.,':":
                if s[y]!=" ":
                    q+=s[y]
                    
            if s[x] not in "?!.,':":
                if s[x]!=" ":
                    poo+=s[x]
            x-=1
            y+=1
        print(poo)
        print(q)
        return poo.lower()==q.lower()
            
