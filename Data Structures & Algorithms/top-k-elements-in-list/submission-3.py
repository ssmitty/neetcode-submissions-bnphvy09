class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        stey={}
        buckets=[[] for i in range(len(nums)+1)]
        
        for i in range(len(nums)):
            if nums[i] in stey:
                stey[nums[i]]+=1
            else:
                stey[nums[i]]=1 
        for i, val in stey.items():
            buckets[val].append(i)
       
        newarr=[]
        for i in range(len(buckets)-1,-1,-1):
            for buck in buckets[i]:
                newarr.append(buck)
                if len(newarr)==k:
                    return newarr
        return newarr




        
        