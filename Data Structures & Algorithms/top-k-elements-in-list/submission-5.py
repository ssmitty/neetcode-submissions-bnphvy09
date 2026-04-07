class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets=[[] for _ in range(len(nums)+1)]
        print(buckets)
        sety={}
        for i in range(len(nums)):
            if nums[i] in sety:
                sety[nums[i]]+=1
            else:
                sety[nums[i]]=1
        #at index freq we want the value then iterate backwards to grab top k elements
        for d,c in sety.items():
            buckets[c].append(d)
        print(k)
        newarr=[]
        for i in range(len(buckets)-1,-1,-1):
            for buck in buckets[i]:
                newarr.append(buck)
                print(len(newarr),k)
                if len(newarr)==k:
                    return newarr
        return newarr        






        
        