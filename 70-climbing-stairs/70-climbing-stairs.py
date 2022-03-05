class Solution:
    def climbStairs(self, n: int) -> int:
        def climbs( n , dp):
            if (dp[n] != 0 ): return dp[n]
            if (n < 2): return 1
            dp[n] = climbs(n-1, dp) + climbs(n-2, dp)
            return dp[n]
        
        dp = [0]*(n+1)
        return climbs(n,dp)
