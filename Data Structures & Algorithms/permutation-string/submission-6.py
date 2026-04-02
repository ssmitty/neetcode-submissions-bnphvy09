class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        dicy={}
        s2set={}
        for i in range(len(s1)):
            if s1[i] not in dicy:
                dicy[s1[i]]=1
            else:
                dicy[s1[i]]+=1
        l=0
        r=len(s1)-1
        while r< len(s2):
            for i in range(l,r+1,1):
                print(s2[l],s2[r],s2[i])
                if s2[i] not in dicy:
                    break
                else:
                    if s2[i] not in s2set:
                        s2set[s2[i]]=1
                    else:
                        s2set[s2[i]]+=1
                if s2set[s2[i]]>dicy[s2[i]]:
                    s2set.clear()
                    break
            if s2set ==dicy:
                return True
            s2set.clear()
            l+=1
            r+=1
        return False