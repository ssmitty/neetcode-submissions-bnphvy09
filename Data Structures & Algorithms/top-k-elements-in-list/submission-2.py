class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets=[[] for i in range(len(nums)+1)]
        #needs to be plus one becuase could have frequency of 4 and len of array be 4 becuase lists start at 0
        count={}
        for n in nums:
            count[n]=1 +count.get(n,0)
            #initialize count set as a dict. Holds value and frequency of value. If exists add value at count[n] else add 0
        for n,c in count.items():
            # how we unpack count dict. n is first in for loop so first element in tuple. C is count because comes second in for loop and seocnd in tuple
            # so buckets at index of count is the value of number
            buckets[c].append(n)
        res=[]
        #this the kth element part
        for i in range(len(buckets)-1,0,-1):
            #we go from finsih to start becuase higher elements are at the top.
            # we append eahc result until we have k of them
            for n in buckets[i]:
                res.append(n)
                if len(res)==k:
                    return res
        print(buckets)
        print(count)

        
        