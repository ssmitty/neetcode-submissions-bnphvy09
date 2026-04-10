class Solution:
    def isValid(self, s: str) -> bool:
        sety=[]
        for i in range(len(s)):
            if s[i]=="[" or s[i]=="(" or s[i]=="{":
                sety.append(s[i])
                print(sety)
            elif s[i]=="]" and len(sety)!=0:
                if sety[-1]=="[":
                    sety.pop()
                else:
                    return False
                print(sety)
            elif s[i]==")" and len(sety)!=0:
                if sety[-1]=="(":
                    sety.pop()
                else:
                    return False
            elif s[i]=="}" and len(sety)!=0:
                if sety[-1]=="{":
                    sety.pop()
                else:
                    return False
            else:
                return False
        if len(sety)==0:
            return True
        return False

        