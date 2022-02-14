class Solution:
    def maxArea(self, h: int, w: int, hC: List[int], vC: List[int]) -> int:
        max_w = 0
        max_h = 0
        
        hC = [0] + hC + [h]
        vC = [0] + vC + [w]
        
        n,m = len(hC),len(vC)
        hC.sort()
        vC.sort()
        
        for i in range(1,n):
            max_w = max(max_w,hC[i] - hC[i - 1])
        
        for i in range(1,m):
            max_h = max(max_h,vC[i] - vC[i - 1])
        
        # print(hC,vC)
        return (max_w * max_h) % (1000000007)