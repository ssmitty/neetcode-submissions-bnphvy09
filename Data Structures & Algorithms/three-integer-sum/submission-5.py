class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplet=[]
        n=len(nums)
        for i in range(len(nums)):
            l=i+1
            r=n-1
            if nums[i]==nums[i-1] and i>0:
                continue
            while(l<r):
                if nums[l]+nums[r]> -nums[i]:
                    r-=1
                    continue
                if nums[l]+nums[r]<-nums[i]:
                    l+=1
                    continue
                if nums[l]+nums[r]==-nums[i]:
                    
                    triplet.append([nums[l],nums[r],nums[i]])
                    r-=1
                    l+=1
                    while nums[l]== nums[l-1] and l<r:
                        l+=1
                    while nums[r]== nums[r+1] and r>l:
                        r-=1
                
        return triplet