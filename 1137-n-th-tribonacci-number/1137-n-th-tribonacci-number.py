class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        if n==0: return 0
        elif n==1 or n==2: return 1
        dp[1] = dp[2] = 1
        for i in range(n-2):
            dp[i+3] = dp[i] + dp[i+1] + dp[i+2]
        return dp[n]