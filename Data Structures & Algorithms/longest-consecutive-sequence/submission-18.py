class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        sety=set(nums)
        maxi=1
        for value in sety:
            if value-1 not in sety:
                length=1
                while value +1 in sety:
                    length+=1
                    value=value+1
                if length> maxi:
                    maxi=length
        return maxi


        