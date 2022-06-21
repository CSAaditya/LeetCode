class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)    
        l = []
        for i in range(0, n-2):
            for j in range(i+1, n-1):
                for k in range(j+1,n):
                    if (i != j and i != k and j != k) and (nums[i] + nums[j] + nums[k]) == 0:
                        l.append([nums[i],nums[j],nums[k]])
                        
        return list(set(tuple(sorted(i)) for i in l))
                    
