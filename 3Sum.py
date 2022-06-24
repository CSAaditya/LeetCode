class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        fs = set()
        for i in range(n - 1):
            s = set()
            # Find all pairs with sum 
            # equals to "-arr[i]" 
            for j in range(i + 1, n):
                x = -(nums[i] + nums[j])
                if x in s:
                    l = sorted([x, nums[i], nums[j]])
                    fs.add(tuple(l))
                else:
                    s.add(nums[j])
        return fs
