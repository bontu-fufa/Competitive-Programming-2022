class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums : return []
        if len(nums) == 1: return [str(nums[0])]
        
        def create_range(start , end):
            if start == prev: 
                return str(start)
            return str(start)+'->'+str(prev)
        
        ranges = []
        start = nums[0]
        prev = nums[0]
        
        for i in range(1,len(nums)):
            num = nums[i]
            if not num-1 == prev: 
                range_str = create_range(start,prev)
                ranges.append(range_str)
                start = num
            prev = num
        ranges.append(create_range(start,prev))
        return ranges
            