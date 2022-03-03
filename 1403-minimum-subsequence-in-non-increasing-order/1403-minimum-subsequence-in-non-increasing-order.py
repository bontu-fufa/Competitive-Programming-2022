class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) == 1: return nums 
        
        nums.sort()
        nums = nums[::-1]
        total_sum = sum(nums)
        current = 0
        print(nums)
        for i,num in enumerate(nums): 
            if current > total_sum - current:
                return nums[:i]
            current += num
        return nums
        