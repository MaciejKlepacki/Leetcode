class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount+1
        T = [n] * (n)
        T[0] = 0

        for i in range(n):
            for c in coins:
                if i >= c:
                    T[i] = min(T[i], T[i-c] + 1)
        return T[-1] if T[-1] != n else -1