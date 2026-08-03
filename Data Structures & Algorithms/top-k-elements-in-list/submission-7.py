class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sety={}
        for i in range(len(nums)):
            if nums[i] in sety:
                sety[nums[i]]+=1
            else:
                sety[nums[i]]=1
        array=[]
        for num,val in sety.items():
            array.append([val,num])
        array.sort()
        res=[]
        while k>len(res):
            res.append(array.pop()[1])
        return res